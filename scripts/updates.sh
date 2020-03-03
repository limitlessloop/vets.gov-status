#!/usr/bin/env bash

python google_analytics/update_data.py
python google_analytics/update_counts.py

python idme/update_accounts.py

#python /application/prometheus/update_from_prometheus.py

python migration_status_update.py