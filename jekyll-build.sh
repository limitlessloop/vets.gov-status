#!/usr/bin/env bash
docker run --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll build --trace
