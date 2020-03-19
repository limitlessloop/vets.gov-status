#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR="."
export GA_SERVICEACCOUNT="serviceaccount.json"

echo Running Google Analytics scripts...
python google_analytics/fetch_ga_data.py

echo Modifying Last Updated date...
current_date=$(date "+%B %d, %Y")
current_time=$(date "+%I:%m %p %Z")
echo "date: $current_date" > data/last_updated.yml
echo "time: $current_time" >> data/last_updated.yml

echo Moving data to new directory...
mv data/* ../src/_data/
echo Done fetching data.