# Makefile for VA.gov performance dashboard
# Tested with GNU Make 3.8.1
SHELL        	:= /usr/bin/env bash -e
COMPOSE_UI_TEST := docker-compose -f docker-compose-ui-test.yml
CI_ARG      	:= $(CI)

.DEFAULT_GOAL := help

# cribbed from https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html and https://news.ycombinator.com/item?id=11195539
help:  ## Prints out documentation for available commands
	@awk -F ':|##' \
		'/^[^\t].+?:.*?##/ {\
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
		}' $(MAKEFILE_LIST)

### Yarn / Node / etc.

# Yarn install doesn't always change node_modules, but we touch the directory so it shows as up to date
node_modules: yarn.lock package.json
ifeq ($(CI_ARG), true)
	yarn install --frozen-lockfile --non-interactive
else
	yarn install --check-files
endif
	touch node_modules

.PHONY: copy-node-dependencies
copy-node-dependencies: node_modules
	mkdir -p src/assets/vendor/jquery
	cp node_modules/jquery/dist/jquery.min.js src/assets/vendor/jquery/
	mkdir -p src/assets/vendor/chart.js
	cp node_modules/chart.js/dist/Chart.bundle.min.js src/assets/vendor/chart.js/
	mkdir -p src/assets/vendor/formation/sass
	# The "*" after /dist/ is important here, as BSD vs GNU treats the semantics differently if you don't have the *
	cp -r node_modules/@department-of-veterans-affairs/formation/dist/* src/assets/vendor/formation/
	cp -r node_modules/@department-of-veterans-affairs/formation/sass/* src/assets/vendor/formation/sass/

.PHONY: yarn-install
yarn-install: node_modules copy-node-dependencies ## Install npm dependencies using yarn

### Jekyll
.PHONY: build
build: yarn-install  ## Build the Jekyll site
	docker run --rm --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll build --trace

.PHONY: run
run: yarn-install  ## Build the Jekyll site and start the Jekyll webserver on port 4000
	docker run --rm -p 4000:4000 --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll serve --trace

## Pip / Python
.PHONY: python-install
python-install:  ## Sets up your python environment for the first time (only need to run once)
	pip install virtualenv
	virtualenv -p ~/.pyenv/shims/python ENV
	source ENV/bin/activate
	@echo shell ENV activated
	pip install --require-hashes -r scripts/requirements.txt -r scripts/dev-requirements.txt
	# Will sync and also remove any dependencies not included in requirements specs
	pip-sync scripts/requirements.txt scripts/dev-requirements.txt
	@echo Finished install
	@echo To activate the shell type:
	@echo source ENV/bin/activate

SITE_PACKAGES := $(shell pip show pip | grep '^Location' | cut -f2 -d':')
.PHONY: pip-install
pip-install: $(SITE_PACKAGES)

$(SITE_PACKAGES): scripts/requirements.txt scripts/dev-requirements.txt
ifeq ($(CI_ARG), true)
	@echo "Do nothing; assume python dependencies were installed by Dockerfile.test already"
else
	pip-sync scripts/requirements.txt scripts/dev-requirements.txt
	touch $(SITE_PACKAGES)
endif

scripts/requirements.txt: scripts/requirements.in
	pip-compile --upgrade --generate-hashes scripts/requirements.in --output-file scripts/requirements.txt

scripts/dev-requirements.txt: scripts/dev-requirements.in
	pip-compile --upgrade --generate-hashes scripts/dev-requirements.in --output-file scripts/dev-requirements.txt

## Test targets
.PHONY: unit-test
unit-test: pip-install  ## Run python unit tests
	PYTHONWARNINGS='ignore::DeprecationWarning:numpy' \
	python -m pytest -v --cov --cov-report term --cov-report xml --cov-report html

.PHONY: flake8
flake8: $(SITE_PACKAGES)	## Run Flake8 python static style checking and linting
	@echo "flake8 comments:"
	flake8 --max-line-length=120 --statistics scripts

.PHONY: ci-unit-test
ci-unit-test:  CONTAINER_NAME := dashboard-test-container-$(shell date "+%Y.%m.%d-%H.%M.%S")
ci-unit-test:  ## Run unit tests and flake in a docker container, copy the results back out
	docker build -q -t dashboard-test-img -f Dockerfile.test .
	docker run --name $(CONTAINER_NAME) --env CI=$(CI_ARG) dashboard-test-img && \
	docker cp $(CONTAINER_NAME):/dashboard/results . && \
	docker rm $(CONTAINER_NAME)

.PHONY: ui-test
# CURRENT_UID needed to be able to run the command below as Jenkins in CI -
# see https://github.com/moby/buildkit/pull/1180 for a potentially a future more robust addition to make docker fail if
# a variable isn't set
ui-test: export CURRENT_UID := $(shell id -u):$(shell id -g)
ui-test:   ## Run UI tests using selenium / chrome / nightwatch
	$(COMPOSE_UI_TEST) up --abort-on-container-exit --force-recreate --remove-orphans

.PHONY: test
test: unit-test flake8 ui-test ## Run unit tests, static analysis and ui tests
	@echo "All tests passed."  # This should only be printed if all of the other targets succeed

# .PHONY: docker-clean
# docker-clean:
# 	$(COMPOSE_UI_TEST) down --rmi all --volumes

.PHONY: clean
clean:  ## Delete any directories, files or logs that are auto-generated
	rm -rf node_modules
	rm -rf target
	rm -rf results
	rm -rf .pytest_cache
	rm -rf _site
	rm -f .coverage
	rm -rf src/.jekyll-cache
	rm -rf src/assets/vendor
	rm -rf test/ui/logs
	rm -rf test/node_modules
	find scripts -name '__pycache__' -type d | xargs rm -rf
