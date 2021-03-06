# VA.gov Performance Dashboard

The performance dashboard provides a simple overview of the VA.gov project to external audiences. It is often used in briefings but should be able to stand-alone with enough context offered for a visitor unfamiliar with VA.gov to navigate and understand it.

## Jekyll Structure

This is a static site generated by [Jekyll](https://jekyllrb.com/docs/). Jekyll uses [Liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers) for templating.
 
File and directory names starting with an underscore (`_`) are used by Jekyll. The pages of the website map to `.html` files in `src/`.

Data for the charts comes from `.csv` files and data for the tiles comes from `.yml` files in `src/_data/`, which are generated by python scripts found in `scripts/`. The scripts fetch data from Google Analytics and Foresee.

> Note: file and folder naming is important for Jekyll. Jekyll looks for folders with specific names (ex: `_includes/`) when building the site.

## Site Context and Details

The performance dashboard page is rendered from `index.html`, which includes the other page components.

The "Our North Star" section explains the North Star of VA.gov and how the data on this page is measuring our goal progress.

The "VA.gov at a glance" section provides metrics over the past year for logged in users, user satisfaction, and successful transactions, which match the 3 North Star goals. A set of summary metrics over time are conveyed in series of charts in a tab group. The metrics are presented as monthly data, ending with the last full month, and provide a long-term trend view. The tabs are used to conserve visual space.

The "Performance by service" section includes a breakdown of the different services found at VA.gov in a set of "tiles." These show the total users in the last 30 days and how that's changed from the year before. Then, it displays some of the most popular tools for that service and how many transactions occurred in the last 30 days.

### Design

This site follows the design patterns specified on [design.va.gov](https://design.va.gov) and makes use of JavaScript and stylesheets from [Formation](https://www.npmjs.com/package/@department-of-veterans-affairs/formation). 
This dependency is specified in `package.json`, and it is copied into `src/assets/vendor` after installation.

### Chart Data

The charts are powered by the VA.gov Google Analytics account and Foresee account. The Python scripts in `scripts` pull data from the accounts and create a set of updated CSV files in `src/_data` that are then used by Jekyll to build the actual charts.

Jekyll renders the charts using `at_a_glance.yml` to configure the titles, labels, and data sources for each chart. 
The file `draw_chart.js` uses [`Chart.js`](https://chartjs.org) to render each chart.

Once deployed, the data is static until the next deploy. Because the performance dashboard is meant for external audiences, this ensures that the data is available and can be quality controlled prior to putting it in front of an audience. Once deployed, we do not have to worry about data abnormalities or failures appearing.

### Services Data

The tiles in the "Performance by service" section are generated using `scripts/services.yml`,
which must have the following structure:

```
services:
  - title: 'Health Care'
    page_path_filter: 'www.va.gov/health-care'
    tools:
      - title: 'Apply for health care benefits'
        page_path_filter: '/health-care/apply'
        event_category_filter: 'Transactions'
        event_action_filter: 'Forms'
  - title: 'Disability'
    tools:
      - title: 'Check VA claim or appeal status'
        page_path_filter: 'www.va.gov/track-claims/'
        event_category_filter: 'Transactions'

```

**To add another service**, add an additional item to the `services` list. You can duplicate an existing one and edit its fields.

If you want the tile on the frontend to have a "Total Users" metric for that service, add a `page_path_filter` field
to the entry in the YAML file. The value of this field is used to perform a query to Google Analytics.
This is a required field.

**To add tools for that service**, add items to the `tools` list within each `service` entry. For each tool, it is mandatory
to provide the fields `page_path_filter` and `event_category_filter`, and optional to provide `event_action_filter`.

The values for `page_path_filter`, `event_category_filter`, and `event_action_filter` are used to build queries
for Google Analytics.

## External Integrations

Data for the charts and tiles are pulled from Google Analytics and Foresee when the scripts are executed.

### Google Analytics

The [Google Analytics 360](https://analytics.google.com/analytics/web/) portal can be used to view the raw GA data online.
Use the [GA query explorer](https://ga-dev-tools.appspot.com/query-explorer/) or "Try this API" on
the [batchGet](https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet) documentation
to interactively test queries and validate filters.

We use the [`google-api-python-client`](https://pypi.org/project/google-api-python-client/) to make requests to Google Analytics.

Service account credentials are obtained through credstash.

### Foresee
We use [ForeSee API](https://developer.foresee.com/docs/public-api) to collect CSAT scores.  We pull data for the [VA Main V2](https://cxsuite.foresee.com/client/measures/8847572/analytics/summary) CX survey.
For the API VA Main V2 corresponds to measure id `8847572`.
This means that if for any reason a new survey is created the measure id will change hence the code should change.

The ForeSee API has a 100 record limit per request so multiple API calls are required to obtain all the records for a period.  For example, we have to send 25 requests to fetch all the records
for one month. To fetch one year worth of data it takes around 10 minutes.  The API token might expire between the requests hence the code supports renewing API token. 

To fetch CSAT data locally, you will need to export a `FORESEE_CREDENTIALS` environment variable in order to to generate API token.

The ForeSee service account credentials are obtained through credstash.  


## Getting Started

### Makefile

Most of the commands used in development are in the [Makefile](Makefile). You can get a list of possible commands with:
`$ make`
or
`$ make help`

#### Install Yarn

[Yarn](https://yarnpkg.com/) is used to manage javascript dependencies. You can install it with:

`$ brew install yarn`

Then install dependencies with:

`$ make yarn-install`

### Jekyll

In order to mimic the CI environment, we run Jekyll out of a docker container. We have built helper scripts as follows:

Build jekyll site:

`$ make build`

Start jekyll site and serve it on http://localhost:4000/scorecard/:

`$ make run`

### Testing

The unit tests are written with pytest, and running them will generate a coverage report.

Run all unit tests and ui tests with `make test`.

Run only unit tests with `make unit-test`.

Run only UI tests with `make ui-test`.

### Run Python Scripts

Make sure you have the correct version of python: `pyenv install 3.6.8` (use version in `.python-version`)

Run `make python-install` to install a virtual environment and install the dependencies.

Activate the virtual environment with `source ENV/bin/activate`

Go into the scripts directory and run the scripts with `./fetch-data-local.sh`

### Credentials

The scripts get secrets out of [credstash](https://github.com/fugue/credstash) when running in CI.

When running locally, you can ask a colleague for the `ga-serviceaccount.json` file and place it in `scripts/local_credentials`.

The Foresee credentials can be set locally by exporting the FORESEE_CREDENTIALS variable with valid Foresee credentials.

### Adding new packages to python scripts

Add the package names to `requirements.in` for run-time dependencies, or `dev-requirements.in` for dependencies used during testing. 
Then, you can run `make pip-install` to update the `requirements.txt` or `dev-requirements.txt` files and sync your installed packages.

## Continuous integration and deployment
### CI
`Jenkinsfile` manages several automated checks that are run on every commit pushed to github.
- Unit tests (these currently test the python scripts)
- Flake8 static analysis (of python scripts)
- UI tests (simple smoke tests to confirm the Jekyll build succeeded)
- Integration tests (For now, consists of running the data update scripts to confirm they don't throw errors)

### Deployment
The site is automatically deployed by `Jenkinsfile` when certain branches change, provided the tests pass:

| branch | environment |
|---|---|
| development | https://dev.va.gov/scorecard |
| master | https://staging.va.gov/scorecard |
| production | https://www.va.gov/scorecard |

There are two pathways to getting into production:
1. Merge development branch to master, confirm staging works, then merge master to production. The merging is currently
 a manual process and is used for code updates. (the deploy is automated by `Jenkinsfile`)
2. The `Jenkinsfile.update` script runs nightly, which downloads new data and commits it to `master` 
branch. If this is successful, it triggers the `Jenkinsfile.automerge` script, which will merge the latest from master 
into production. New commits to `production` will trigger `Jenkinsfile` which will run CI and deploy the site. This is 
automated (defined [here](https://github.com/department-of-veterans-affairs/devops/blob/master/ansible/deployment/config/jenkins-vetsgov/seed_job.groovy)).



## Developer Onboarding

More useful developer onboarding documentation can be [found here](dev/onboarding.md).

## Supported Browsers

The current list of supported browsers for scorecard redesign include Chrome 61, Firefox 60, iOS 11, Edge 16, ChromeAndroid 67, Safari 11. This list aligns with the [vets-website list](https://github.com/department-of-veterans-affairs/vets-website/blob/master/.babelrc#L16).

## Previous Dashboards

This repo previously held two now defunct dashboards / 

The first iteration (vets.gov status) is archived as  [release 0.1](https://github.com/department-of-veterans-affairs/vets.gov-status/releases/tag/0.1).

The second iteration (VA.gov scorecard) is archived as [release 1.0](https://github.com/department-of-veterans-affairs/vets.gov-status/releases/tag/1.0).
