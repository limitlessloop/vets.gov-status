#!/usr/bin/env bash

# Build the image for testing
docker build -t scorecard-img -f Dockerfile.test .

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
container_name=scorecard-container-${current_time}

docker run --name ${container_name} scorecard-img
docker cp ${container_name}:/scorecard/results .
docker rm ${container_name}
