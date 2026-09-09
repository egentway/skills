#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
target_dir="${HOME}/.agents/skills"

mkdir -p -- "$target_dir"

for skill_dir in "$repo_root"/*/; do
  skill_name=${skill_dir%/}
  skill_name=${skill_name##*/}
  ln -sfn -- "$skill_dir" "$target_dir/$skill_name"
done
