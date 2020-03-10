#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR=""
export GA_SERVICEACCOUNT="serviceaccount.json"
export MARKDOWN_DIR="migration_status"

#python google_analytics/update_data.py
#python google_analytics/update_counts.py
python google_analytics/fetch_transactions.py

#python idme/update_accounts.py

#python /application/prometheus/update_from_prometheus.py

#python migration_status_update.py