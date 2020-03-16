#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

# Build the image for testing
docker build -t dashboard-fetch-img .

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
container_name=dashboard-fetch-container-${current_time}

echo "Fetching data via docker image"
# Note: The credstash invocation inside Jenkins fails with an SSL error if run while using a Jenkins Docker pipeline step
# such as dockerImage.inside(). Invoking the container directly here seems to work however.
# Creating a memory-only filesystem mount to store credentials out of credstash
docker run --name ${container_name} --tmpfs /var/tmp --env AWS_DEFAULT_REGION --env GA_SERVICEACCOUNT --env CI dashboard-fetch-img
docker cp ${container_name}:/application/data/. ../src/_data
docker rm ${container_name}
echo "Done fetching data"
