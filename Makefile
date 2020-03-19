# Makefile for VA.gov performance dashboard
# Tested with GNU Make 3.8.1
SHELL        	:= /usr/bin/env bash
COMPOSE_UI_TEST := docker-compose -f docker-compose-ui-test.yml

.DEFAULT_GOAL := help

#ENV_ARG      := $(env)
#COMPOSE_DEV  := docker-compose

#BASH_DEV     := $(COMPOSE_DEV) $(BASH) -c
#BASH_TEST    := $(COMPOSE_TEST) $(BASH) --login -c
#LINT    	 := "bin/rails lint"
#DOWN         := down

# cribbed from https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html and https://news.ycombinator.com/item?id=11195539
help:  ## Prints out documentation for available commands
	@awk -F ':|##' \
		'/^[^\t].+?:.*?##/ {\
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
		}' $(MAKEFILE_LIST)

.PHONY: jekyll-build
jekyll-build: yarn.lock  ## Build the Jekyll site
	docker run --rm --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll build --trace

.PHONY: jekyll-serve
jekyll-serve: yarn.lock  ## Build the Jekyll site and start the Jekyll webserver on port 4000
	docker run --rm -p 4000:4000 --volume=${PWD}:/srv/jekyll -it jekyll/jekyll:4.0  jekyll serve --trace

yarn.lock: node_modules package.json
	yarn install --production=false --check-files

#.PHONY: install
#SITE_PACKAGES := $(shell pip show pip | grep '^Location' | cut -f2 -d':')
#install: $(SITE_PACKAGES)

#$(SITE_PACKAGES): requirements.txt
#    pip install -r requirements.txt

.PHONY: unit-test
unit-test:   ## Run python unit tests
	PYTHONWARNINGS='ignore::DeprecationWarning:numpy' \
	python -m pytest -v --cov --cov-report term --cov-report xml --cov-report html

.PHONY: flake8
flake8: 	## Run Flake8 python static style checking and linting
	@echo "Flake8 comments:"
	flake8 --max-line-length=120 --statistics scripts

.PHONY: ui-test

# This is needed to be able to run the command below as Jenkins in CI -
# see https://github.com/moby/buildkit/pull/1180 for a potentially more robust addition
ui-test: export CURRENT_UID := $(shell id -u):$(shell id -g)
ui-test:   ## Run UI tests using selenium / chrome / nightwatch
	$(COMPOSE_UI_TEST) up --abort-on-container-exit --force-recreate --remove-orphans

.PHONY: ci-unit-test
ci-unit-test:  CONTAINER_NAME := dashboard-test-container-$(shell date "+%Y.%m.%d-%H.%M.%S")
ci-unit-test:  ## Run unit tests and flake in a docker container, copy the results back out
	docker build -q -t dashboard-test-img -f Dockerfile.test .
	docker run --name $(CONTAINER_NAME) dashboard-test-img && \
	docker cp $(CONTAINER_NAME):/dashboard/results . && \
	docker rm $(CONTAINER_NAME)

.PHONY: test
test: unit-test flake8 ui-test ## Run unit tests, static analysis and ui tests
	@echo "All tests run"

# .PHONY: docker-clean
# docker-clean:
# 	$(COMPOSE_UI_TEST) down --rmi all --volumes

.PHONY: clean
clean:  ## Delete any directories and files that are auto-generated
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
	@find -depth -type d -name __pycache__ -exec rm -ff {} \;
