## Overview

These scripts automate updating the data that powers the charts for the scorecard. They pull data from Google Analytics, Prometheus, and ID.me to provide updates.

## Running the scripts

The scripts are separated into subdirectories for each data source. Inside each is a simple shell script called
`update.sh` that will run the script and move the updated data into the `_data` directory.

>The Google Analytics needs a `serviceaccount.p12` file, which is a Google Service Account with access to the Google Analytics account. There are instructions at https://developers.google.com/identity/protocols/OAuth2ServiceAccount on getting that setup.
>
>The Prometheus script expects access to Prometheus (via SOCKS), and the addresses of both the environment-specific and utility prometheus instance API endpoints, defined as `PROMETHEUS_API_SITE` and `PROMETHEUS_API_UTILITY` environment variables. This will change
 when running of the scripts is moved to Jenkins (which has direct access to the Prometheus endpoints).

### System requirements

You'll need Python >= 3.5 (tested on Python 3.5.2) and pip.

The update shell scripts create virtual environments that install all other necessary dependencies.

## Configuration

### Google Analytics

Edit `ga_config.json` to update the data that is pulled.

The `charts` section has entries that match the following:

```
"file_prefix": {
    "view": "12345678",
    "page_filter": ""
  }
```

- `file_prefix` must match the `charts` entry in the board's YAML front matter so that the data is pulled into the charts.
- `view` is the View ID in the Google Analytics Admin view. Select the view, then click View Settings. View ID will be listed at the top as an eight digit number.
- `page_filter` is a Google Analytics REGEX statement for a subset of page URLs to match. Use an empty string to match the whole view.

The `clicks` sections has entries that match the following:

```
"file_prefix": {
    "view": "12345678"
  }
```

`file_prefix` and `view` have the same meaning as in the `boards` section.

## Automation

We use the shell scripts to automate much of the work each week to update the data and create a PR. These scripts are tailored to our environment and expect a GitHub API token to be configured in the `gitconfig` file. You will need to modify this to meet your own needs if you wish to use them.

We intend to transition from these shell scripts (currently invoked by cron) to a Jenkins-based system in the future.
