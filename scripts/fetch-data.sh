#!/usr/bin/env bash
set -o errexit
set -o nounset
set -x

# todo: Make credentials key an environment variable as well
printenv
credstash --region ${AWS_DEFAULT_REGION} get vagovanalytics.prod.service_account_credentials > ${GA_SERVICEACCOUNT}
python google_analytics/update_data.py
python google_analytics/update_counts.py

#python /application/prometheus/update_from_prometheus.py
