#!/usr/bin/env bash
docker run --rm --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll build --trace
