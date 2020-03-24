#!/usr/bin/env bash
set -o errexit
set -o nounset
# set -x

# Build the image for testing
docker build -t dashboard-fetch-img .

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
container_name=dashboard-fetch-container-${current_time}

# Note: The credstash invocation inside Jenkins fails with an SSL error if run while using a Jenkins Docker pipeline step
# such as dockerImage.inside() { }. Invoking the container directly here seems to work however.
echo "Fetching data via docker image"
docker run --name ${container_name} --env AWS_DEFAULT_REGION dashboard-fetch-img
docker cp ${container_name}:/application/data/. ../src/_data
docker rm ${container_name}
echo "Done fetching data"
