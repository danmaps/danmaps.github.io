#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if [[ -x ".secfix-venv/bin/python" ]]; then
  PYTHON_BIN=".secfix-venv/bin/python"
elif [[ -x ".venv/bin/python" ]]; then
  PYTHON_BIN=".venv/bin/python"
fi

"$PYTHON_BIN" freeze.py
touch docs/.nojekyll

# Stage post markdown changes and all generated docs output.
# This intentionally picks up new tag pages and other newly-created frozen files.
git add posts docs

echo "Freeze complete. Staged files:"
git diff --cached --name-only
