#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR="."
export GA_SERVICEACCOUNT="serviceaccount.json"

echo Running Google Analytics scripts...
python google_analytics/fetch_ga_data.py

mv data/all_transactions.csv ../src/_data/
mv data/all_logged_in_users.csv ../src/_data/
