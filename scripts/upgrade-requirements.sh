#!/usr/bin/env bash

# Upgrades all dependencies to latest published versions
# Per https://github.com/jazzband/pip-tools
pip-compile --upgrade --generate-hashes requirements.in
pip-compile --upgrade --generate-hashes dev-requirements.in
pip-sync requirements.txt dev-requirements.txt
