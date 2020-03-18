## Overview

These scripts automate updating the data that powers the charts for the dashboard. They pull data from Google Analytics and Foresee to provide updates.

## Running the scripts

The scripts are separated into subdirectories for each data source. Inside each is a simple shell script called
`fetch-data.sh` that will run the script and move the updated data into the `data` directory.

> The Google Analytics needs a `serviceaccount.json` file, which is a Google Service Account with access to the Google 
> Analytics account. There are instructions at https://developers.google.com/identity/protocols/OAuth2ServiceAccount on getting that setup.

### System requirements

You'll need Python >= 3.6 (tested on Python 3.6.8) and pip.

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

We use the shell scripts to automate much of the work each day to update the data and create a PR.
