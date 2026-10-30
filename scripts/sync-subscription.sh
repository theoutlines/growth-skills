#!/usr/bin/env bash
# Copy the skills of Subscription Skills (theoutlines/subscription-skills) into this plugin.
# Edit those skills in their own repo, never here. Run before every release, then bump the version.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/plugins/growth-skills/skills"
TMP="$(mktemp -d)"
git clone -q --depth 1 https://github.com/theoutlines/subscription-skills.git "$TMP/sub"
SRC="$TMP/sub/plugins/subscription-skills/skills"
for d in "$SRC"/*/; do
  s="$(basename "$d")"
  rm -rf "${DEST:?}/$s"
  cp -r "$d" "$DEST/$s"
  echo "synced $s"
done
cp "$TMP/sub/LICENSE" "$ROOT/LICENSES/subscription-skills-CC-BY-4.0.txt"
rm -rf "$TMP"
echo "Now bump the version in plugins/growth-skills/.claude-plugin/plugin.json and .claude-plugin/marketplace.json"
