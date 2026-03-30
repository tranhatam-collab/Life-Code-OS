#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:-production}"
BRANCH="main"

if [ "$MODE" = "preview" ]; then
  BRANCH="preview"
fi

COMMIT_HASH="$(git -C "$ROOT_DIR" rev-parse HEAD 2>/dev/null || true)"

if [ -z "$COMMIT_HASH" ]; then
  COMMIT_HASH="local-$(date +%Y%m%d%H%M%S)"
fi

COMMIT_MESSAGE="Life Code OS ${MODE} deploy"

bash "$ROOT_DIR/scripts/prepare-pages.sh"
cd "$ROOT_DIR"

./node_modules/.bin/wrangler pages deploy dist \
  --project-name=life-code-os \
  --branch="$BRANCH" \
  --commit-hash="$COMMIT_HASH" \
  --commit-message="$COMMIT_MESSAGE" \
  --commit-dirty=true
