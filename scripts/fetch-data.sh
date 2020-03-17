#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

# todo: Make credentials key an environment variable as well
credstash --region ${AWS_DEFAULT_REGION} get vagovanalytics.prod.service_account_credentials > ${GA_SERVICEACCOUNT}
#python /application/google_analytics/update_data.py
#python /application/google_analytics/update_counts.py
#python /application/prometheus/update_from_prometheus.py

echo Running Google Analytics scripts...
python /application/google_analytics/fetch_ga_data.py

echo Modifying Last Updated date...
current_date=$(date "+%B %d, %Y")
echo "last_updated: $current_date" > application/data/last_updated.yml
