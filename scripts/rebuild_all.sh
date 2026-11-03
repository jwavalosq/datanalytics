#!/bin/bash
# Rebuild this project from scratch, in order.
# Run from the project root: bash scripts/rebuild_all.sh
# Needs: python3 with the packages in requirements.txt, or the .venv in this folder.
set -e
cd "$(dirname "$0")/.."
PY="python3"
if [ -x ".venv/bin/python" ]; then PY=".venv/bin/python"; fi
echo "Using Python: $PY"
"$PY" scripts/build_processed.py
for nb in notebooks/*.ipynb; do
  echo "Executing $nb"
  "$PY" -m jupyter nbconvert --to notebook --execute "$nb" --output "$(basename "$nb")" --allow-errors --ExecutePreprocessor.timeout=600
done
cp charts/*.png docs/charts/ 2>/dev/null || true
echo "Done. Charts are in charts/ and docs/charts/."
echo "Check for the banned em dash character (excluding .venv):"
if grep -rP "\x{2014}" notebooks README.md BUILD_REPORT.md docs/index.html data/raw/PROVENANCE.md scripts; then
  echo "WARNING: em dash found above."
else
  echo "No em dash found."
fi
