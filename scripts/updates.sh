#!/usr/bin/env bash

cd scripts

for SUBDIR in  */; do
	echo "${SUBDIR}update.sh"
	${SUBDIR}update.sh
done
