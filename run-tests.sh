#!/usr/bin/env bash
# Make sure we exit on failure b/c this is run in CI
set -o errexit

export PYTHONWARNINGS="ignore::DeprecationWarning:numpy"

python -m pytest -v --cov --cov-report term --cov-report xml --cov-report html

echo "Flake8 comments:"
flake8 --max-line-length=120 scripts
