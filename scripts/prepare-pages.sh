#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

rsync -a \
  --exclude='.git/' \
  --exclude='.gitignore' \
  --exclude='.github/' \
  --exclude='.wrangler/' \
  --exclude='node_modules/' \
  --exclude='dist/' \
  --exclude='scripts/' \
  --exclude='package.json' \
  --exclude='package-lock.json' \
  --exclude='README.md' \
  --exclude='PROJECT_STATUS_MASTER.md' \
  --exclude='docs/' \
  --exclude='.DS_Store' \
  "$ROOT_DIR/" "$DIST_DIR/"
