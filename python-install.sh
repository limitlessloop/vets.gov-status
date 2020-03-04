#!/usr/bin/env bash
# Sets up python environment and installs dependencies

set -e

pip install virtualenv

virtualenv -p ~/.pyenv/shims/python ENV
source ENV/bin/activate
echo shell ENV activated

pip install --require-hashes -r scripts/requirements.txt -r scripts/dev-requirements.txt
# Will sync and also remove any dependencies not included in requirements specs
pip-sync scripts/requirements.txt scripts/dev-requirements.txt

echo Finished install
echo To activate the shell type:
echo source ENV/bin/activate
