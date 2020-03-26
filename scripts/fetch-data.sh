#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

# todo: Make credstash credential keys environment variables as well
if [ -n "${CI:-}" ]; then
  credstash --region ${AWS_DEFAULT_REGION} get vagovanalytics.prod.service_account_credentials > ${GA_SERVICEACCOUNT}
  export FORESEE_CREDENTIALS=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.api.credentials`
fi

if [ -z "${INTEGRATION_TEST:-}" ]; then
  echo Running Google Analytics scripts...
  python -m fetch_data
  echo Modifying Last Updated date...
  current_date=$(date "+%B %d, %Y")
  current_time=$(date "+%I:%m %p %Z")
  echo "date: $current_date" > data/last_updated.yml
  echo "time: $current_time" >> data/last_updated.yml
else
  echo Running integration test...
  python -m test.fetch_data_integration_test
fi
