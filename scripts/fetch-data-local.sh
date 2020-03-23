#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR="."
export GA_SERVICEACCOUNT="serviceaccount.json"
export AWS_DEFAULT_REGION=us-east-2
export FORESEE_USER=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.odata.username`
export FORESEE_PWD=`credstash --region ${AWS_DEFAULT_REGION} get foresee.prod.odata.password`

echo Running Google Analytics scripts...
python -m google_analytics.fetch_ga_data

echo Modifying Last Updated date...
current_date=$(date "+%B %d, %Y")
current_time=$(date "+%I:%m %p %Z")
echo "date: $current_date" > data/last_updated.yml
echo "time: $current_time" >> data/last_updated.yml

echo Moving data to new directory...
mv data/* ../src/_data/
echo Done fetching data.