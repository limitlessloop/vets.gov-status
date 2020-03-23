#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

# todo: Make credentials key an environment variable as well
credstash --region ${AWS_DEFAULT_REGION} get vagovanalytics.prod.service_account_credentials > ${GA_SERVICEACCOUNT}
export FORESEE_USER=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.odata.username`
export FORESEE_PWD=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.odata.password`

echo Running Google Analytics scripts...
python -m google_analytics.fetch_ga_data

echo Modifying Last Updated date...
current_date=$(date "+%B %d, %Y")
current_time=$(date "+%I:%m %p %Z")
echo "date: $current_date" > data/last_updated.yml
echo "time: $current_time" >> data/last_updated.yml
