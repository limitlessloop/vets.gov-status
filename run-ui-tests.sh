#!/usr/bin/env bash
# Make sure we exit on failure b/c this is run in CI
set -o errexit

CURRENT_UID=$(id -u):$(id -g) docker-compose up --abort-on-container-exit --force-recreate --remove-orphans
