#!/usr/bin/env python3
"""Read-only Git worktree survey for the worktree-scout skill."""

from __future__ import annotations

import argparse
import itertools
import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


class Git:
    def __init__(self, root: Path) -> None:
        self.root = root

    def run(self, *args: str, cwd: Path | None = None) -> CommandResult:
        try:
            completed = subprocess.run(
                ["git", *args],
                cwd=cwd or self.root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        except OSError as error:
            return CommandResult(1, "", str(error))
        return CommandResult(
            completed.returncode,
            completed.stdout.rstrip("\n"),
            completed.stderr.rstrip("\n"),
        )

    def value(self, *args: str, cwd: Path | None = None) -> str | None:
        result = self.run(*args, cwd=cwd)
        return result.stdout if result.returncode == 0 else None


def parse_worktree_porcelain(output: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    entry: dict[str, Any] | None = None

    for line in output.splitlines():
        if not line:
            if entry is not None:
                entries.append(entry)
                entry = None
            continue

        key, _, value = line.partition(" ")
        if key == "worktree":
            if entry is not None:
                entries.append(entry)
            entry = {"path": value}
        elif entry is not None and key in {"HEAD", "branch", "locked", "prunable", "bare"}:
            entry[key.lower()] = value or True

    if entry is not None:
        entries.append(entry)
    return entries


def load_worktrunk(root: Path) -> list[dict[str, Any]] | None:
    try:
        completed = subprocess.run(
            ["wt", "list", "--format=json"],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        return None

    if completed.returncode != 0:
        return None
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, list) else None


def worktrunk_default_branch(entries: list[dict[str, Any]] | None) -> str | None:
    if entries is None:
        return None
    for entry in entries:
        repo = entry.get("repo")
        if isinstance(repo, dict) and isinstance(repo.get("default_branch"), str):
            return repo["default_branch"]
    return None


def worktrunk_metadata(entries: list[dict[str, Any]] | None) -> dict[str, dict[str, Any]]:
    if entries is None:
        return {}

    fields = (
        "kind",
        "main_state",
        "is_main",
        "is_current",
        "is_previous",
        "remote",
        "working_tree",
        "statusline",
        "symbols",
    )
    metadata: dict[str, dict[str, Any]] = {}
    for entry in entries:
        path = entry.get("path")
        if not isinstance(path, str):
            continue
        metadata[os.path.realpath(path)] = {
            field: entry[field] for field in fields if field in entry
        }
    return metadata


def resolve_ref(git: Git, branch: str | None) -> str | None:
    if not branch:
        return None
    normalized = branch.removeprefix("refs/heads/").removeprefix("refs/remotes/")
    for ref in (f"refs/heads/{normalized}", f"refs/remotes/origin/{normalized}", normalized):
        if git.value("rev-parse", "--verify", "--quiet", ref) is not None:
            return ref
    return None


def baseline(git: Git, inventory: list[dict[str, Any]], worktrunk: list[dict[str, Any]] | None) -> dict[str, Any]:
    primary = inventory[0] if inventory else None
    ref = resolve_ref(git, worktrunk_default_branch(worktrunk))
    source = "Worktrunk default branch" if ref else None

    if ref is None:
        origin_head = git.value("symbolic-ref", "--quiet", "refs/remotes/origin/HEAD")
        if origin_head:
            ref = origin_head
            source = "refs/remotes/origin/HEAD"

    if ref is None and primary and isinstance(primary.get("branch"), str):
        ref = primary["branch"]
        source = "primary worktree branch"

    if ref is not None:
        head = git.value("rev-parse", ref)
        if head is not None:
            return {"ref": ref, "head": head, "source": source}

    if primary and isinstance(primary.get("head"), str):
        return {"ref": "primary HEAD", "head": primary["head"], "source": "primary worktree HEAD"}
    return {"ref": None, "head": None, "source": None}


def parse_status(output: str) -> dict[str, list[str]]:
    state = {"staged": [], "unstaged": [], "untracked": [], "conflicts": []}
    records = output.split("\0")
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record or record.startswith("# ") or record.startswith("! "):
            continue
        if record.startswith("? "):
            state["untracked"].append(record[2:])
            continue

        kind = record[:1]
        if kind == "1":
            parts = record.split(" ", 8)
            xy, path = parts[1], parts[8]
        elif kind == "2":
            parts = record.split(" ", 9)
            xy, path = parts[1], parts[9]
            index += 1  # The following NUL record is the original path.
        elif kind == "u":
            parts = record.split(" ", 10)
            xy, path = parts[1], parts[10]
            state["conflicts"].append(path)
        else:
            continue

        if xy[0] != ".":
            state["staged"].append(path)
        if xy[1] != ".":
            state["unstaged"].append(path)
    return state


def in_progress_operations(git: Git, path: Path) -> list[str]:
    git_dir = git.value("rev-parse", "--git-dir", cwd=path)
    if git_dir is None:
        return ["Git directory unavailable"]
    directory = Path(git_dir)
    if not directory.is_absolute():
        directory = path / directory

    markers = {
        "rebase-merge": "rebase",
        "rebase-apply": "rebase/apply",
        "MERGE_HEAD": "merge",
        "CHERRY_PICK_HEAD": "cherry-pick",
        "REVERT_HEAD": "revert",
        "BISECT_LOG": "bisect",
    }
    return [label for marker, label in markers.items() if (directory / marker).exists()]


def diff_details(git: Git, left: str, right: str, cwd: Path) -> dict[str, Any]:
    diff_range = f"{left}...{right}"
    stat = git.value("diff", "--stat", diff_range, cwd=cwd)
    paths = git.value("diff", "--name-only", diff_range, cwd=cwd)
    return {
        "stat": stat.splitlines() if stat else [],
        "summary": stat.splitlines()[-1].strip() if stat else "no file diff",
        "paths": paths.splitlines() if paths else [],
    }


def capture_worktree(
    git: Git,
    entry: dict[str, Any],
    baseline_head: str | None,
    wt_metadata: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    path = Path(entry["path"])
    branch_ref = entry.get("branch")
    branch = branch_ref.removeprefix("refs/heads/") if isinstance(branch_ref, str) else None
    record: dict[str, Any] = {
        "path": str(path),
        "branch": branch,
        "detached": branch is None,
        "locked": entry.get("locked"),
        "prunable": entry.get("prunable"),
        "bare": bool(entry.get("bare")),
        "worktrunk": wt_metadata.get(os.path.realpath(path)),
    }

    head = git.value("rev-parse", "HEAD", cwd=path)
    if head is None:
        record["unavailable"] = git.run("rev-parse", "HEAD", cwd=path).stderr
        return record

    subject_date = git.value("show", "-s", "--format=%s%x00%cI", head, cwd=path)
    subject, _, date = (subject_date or "").partition("\0")
    status_result = git.run("status", "--porcelain=v2", "--branch", "-z", cwd=path)
    record.update(
        {
            "head": head,
            "short_head": head[:12],
            "subject": subject,
            "date": date,
            "status": parse_status(status_result.stdout) if status_result.returncode == 0 else None,
            "status_error": status_result.stderr if status_result.returncode else None,
            "operations": in_progress_operations(git, path),
        }
    )

    if branch:
        record["description"] = git.value("config", "--get", f"branch.{branch}.description", cwd=path)

    if baseline_head is not None:
        counts = git.value("rev-list", "--left-right", "--count", f"{baseline_head}...{head}", cwd=path)
        if counts:
            behind, ahead = map(int, counts.split())
            commits = git.value("log", "--format=%H%x00%s", f"{baseline_head}..{head}", cwd=path)
            record["main_divergence"] = {
                "ahead": ahead,
                "behind": behind,
                "diff": diff_details(git, baseline_head, head, path),
                "branch_commits": [
                    {"sha": item.partition("\0")[0], "subject": item.partition("\0")[2]}
                    for item in (commits or "").splitlines()
                    if item
                ],
            }
        else:
            record["main_divergence_error"] = git.run(
                "rev-list", "--left-right", "--count", f"{baseline_head}...{head}", cwd=path
            ).stderr
    return record


def shared_ancestry(git: Git, records: list[dict[str, Any]], baseline_head: str | None) -> list[dict[str, Any]]:
    if baseline_head is None:
        return []

    available = [record for record in records if record.get("head")]
    relationships: list[dict[str, Any]] = []
    for left, right in itertools.combinations(available, 2):
        merge_base = git.value("merge-base", left["head"], right["head"])
        if merge_base is None or merge_base == baseline_head:
            continue
        if git.run("merge-base", "--is-ancestor", baseline_head, merge_base).returncode != 0:
            continue

        left_beyond = git.value("rev-list", "--count", f"{merge_base}..{left['head']}")
        right_beyond = git.value("rev-list", "--count", f"{merge_base}..{right['head']}")
        pair_counts = git.value("rev-list", "--left-right", "--count", f"{left['head']}...{right['head']}")
        left_only, right_only = map(int, (pair_counts or "0 0").split())
        relationships.append(
            {
                "left": {"path": left["path"], "branch": left["branch"], "head": left["head"]},
                "right": {"path": right["path"], "branch": right["branch"], "head": right["head"]},
                "merge_base": {
                    "sha": merge_base,
                    "short_sha": merge_base[:12],
                    "subject": git.value("show", "-s", "--format=%s", merge_base),
                },
                "commits_beyond_base": {
                    "left": int(left_beyond or 0),
                    "right": int(right_beyond or 0),
                },
                "exclusive_commits": {"left": left_only, "right": right_only},
                "diff": diff_details(git, left["head"], right["head"], git.root),
            }
        )
    return relationships


def duplicate_candidates(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        if record.get("head"):
            groups.setdefault(record["head"], []).append(record)

    candidates = []
    for head, members in groups.items():
        if len(members) < 2:
            continue
        if any(
            member.get("status") is None
            or any(member["status"][state] for state in ("staged", "unstaged", "untracked", "conflicts"))
            for member in members
        ):
            continue
        candidates.append(
            {
                "head": head,
                "members": [
                    {
                        "path": member["path"],
                        "branch": member["branch"],
                        "detached": member["detached"],
                        "locked": member["locked"],
                        "prunable": member["prunable"],
                    }
                    for member in members
                ],
            }
        )
    return candidates


def survey(repository: Path) -> dict[str, Any]:
    root_result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=repository,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if root_result.returncode != 0:
        raise RuntimeError(root_result.stderr.rstrip("\n") or "not a Git worktree")

    root = Path(root_result.stdout.strip())
    git = Git(root)
    inventory_result = git.run("worktree", "list", "--porcelain")
    if inventory_result.returncode != 0:
        raise RuntimeError(inventory_result.stderr or "git worktree list failed")

    inventory = parse_worktree_porcelain(inventory_result.stdout)
    worktrunk = load_worktrunk(root)
    base = baseline(git, inventory, worktrunk)
    metadata = worktrunk_metadata(worktrunk)
    records = [
        capture_worktree(git, entry, base["head"], metadata)
        for entry in inventory
    ]
    return {
        "schema_version": 1,
        "repository": str(root),
        "baseline": base,
        "worktrunk_available": worktrunk is not None,
        "worktrees": records,
        "shared_ancestry": shared_ancestry(git, records, base["head"]),
        "duplicate_candidates": duplicate_candidates(records),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository or worktree to survey")
    parser.add_argument("--indent", type=int, default=2, help="JSON indentation; use 0 for compact JSON")
    args = parser.parse_args()

    try:
        result = survey(args.repo)
    except RuntimeError as error:
        print(json.dumps({"schema_version": 1, "error": str(error)}))
        return 2

    print(json.dumps(result, indent=args.indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
