#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR=""
export GA_SERVICEACCOUNT="serviceaccount.json"
export MARKDOWN_DIR="migration_status"

echo Running Google Analytics scripts...
python google_analytics/fetch_transactions.py

mv data/all_transactions.csv ../src/_data/