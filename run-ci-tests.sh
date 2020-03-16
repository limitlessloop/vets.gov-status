#!/usr/bin/env bash
# Make sure we exit on failure b/c this is run in CI
set -o errexit
# set -x

# Build the image for testing
docker build -t scorecard-test-img -f Dockerfile.test .

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
container_name=scorecard-test-container-${current_time}

docker run --name ${container_name} scorecard-test-img
docker cp ${container_name}:/scorecard/results .
docker rm ${container_name}
