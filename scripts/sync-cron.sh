#!/usr/bin/env bash
set -euo pipefail

SRC="/home/msands/.openclaw/cron/"
DST="/home/msands/.openclaw/workspace/cron-sync/"

mkdir -p "$DST"
rsync -a --delete "$SRC" "$DST"

echo "Synced $SRC -> $DST"