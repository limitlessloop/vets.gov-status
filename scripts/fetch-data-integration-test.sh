#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

if [ -n "${CI:-}" ]; then
  credstash --region ${AWS_DEFAULT_REGION} get vagovanalytics.prod.service_account_credentials > ${GA_SERVICEACCOUNT}
  export FORESEE_CREDENTIALS=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.api.credentials`
else
  export CONFIG_DIR="."
  export GA_SERVICEACCOUNT="local_credentials/ga-serviceaccount.json"
fi

echo Running data fetch integration test...
python -m fetch_data_integration_test