#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCOPE="user"
DEST=""
FORCE=0
PACKAGE=""

usage() {
  cat <<'EOF'
Usage: ./install.sh [options]

  --scope user|project|custom   Neutral installation scope (default: user)
  --dest PATH                   Required for project/custom scope
  --force                       Backup and replace an existing installation
  --package PATH                Create a portable .skill archive instead
  -h, --help                    Show help
EOF
}

while (($#)); do
  case "$1" in
    --scope) SCOPE="${2:?Missing value for --scope}"; shift 2 ;;
    --dest) DEST="${2:?Missing value for --dest}"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --package) PACKAGE="${2:?Missing value for --package}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ -n "$PACKAGE" ]]; then
  python3 "$ROOT/scripts/package_skill.py" --output "$PACKAGE"
  exit 0
fi

args=(--scope "$SCOPE")
[[ -n "$DEST" ]] && args+=(--dest "$DEST")
(( FORCE )) && args+=(--force)
python3 "$ROOT/scripts/install_skill.py" "${args[@]}"
