#!/usr/bin/env bash

export DATA_DIR="data"
export CONFIG_DIR="."
export GA_SERVICEACCOUNT="local_credentials/ga-serviceaccount.json"

echo Fetching data...
./fetch-data.sh

cp -r data/* ../src/_data/
