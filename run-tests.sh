#!/usr/bin/env bash

# Note - not doing a `set -e` because we don't want the script to exit without displaying test failures

export PYTHONWARNINGS="ignore::DeprecationWarning:numpy"

command="python -m pytest \
  --junitxml results/unit/pytest-unit.xml --cov \
  --cov-report html:results/coverage/ \
  --cov-report xml:results/coverage/pytest-coverage.xml"

echo "$command"
eval "$command"

echo
echo Flake8 comments:
flake8 --max-line-length=120 scripts