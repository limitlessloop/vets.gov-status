#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR="."
export GA_SERVICEACCOUNT="serviceaccount.json"

echo Running Google Analytics scripts...
python google_analytics/fetch_transactions.py
# python google_analytics/update_data.py
# python google_analytics/update_counts.py

mv data/all_transactions.csv ../src/_data/
