#!/bin/bash

set -e

mkdir -p src/assets/vendor/jquery
cp node_modules/jquery/dist/jquery.min.js src/assets/vendor/jquery/

mkdir -p src/assets/vendor/chart.js
cp node_modules/chart.js/dist/Chart.bundle.min.js src/assets/vendor/chart.js/

mkdir -p src/assets/vendor/formation
cp -r node_modules/@department-of-veterans-affairs/formation/dist/ src/assets/vendor/formation/
