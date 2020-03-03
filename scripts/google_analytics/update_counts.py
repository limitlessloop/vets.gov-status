"""Pulls in data to update dashboards"""

import datetime
import json
import os

from apiclient.discovery import build
from google.oauth2.service_account import Credentials

from analytics_helpers import make_df

import ruamel.yaml as yaml

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.environ['GA_SERVICEACCOUNT']


def initialize_analyticsreporting():
    """Initializes an analyticsreporting service object.

    Returns:
    analytics an authorized analyticsreporting service object.
    """

    credentials = Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

    # Build the service object.
    analytics_service = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics_service


def get_count_report(analytics_service, view_id, event_name):
    """Use the Analytics Service Object to query Analytics Reporting API.
    """

    # Start on 1 September 2017 which is the cutover date to the unified view
    # Adjustment in the config is the sums from 30 June 2016 (launch of HCA) until
    # 31 August 2017 when the cutover happened.
    startDate = datetime.date(2017, 9, 1).isoformat()
    # Yesterday
    endDate = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

    return analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': startDate,
                                    'endDate': endDate}],
                    'metrics': [{'expression': 'ga:totalEvents'}],
                    'dimensions': [{'name': 'ga:eventLabel'}],
                    "dimensionFilterClauses": [{
                        "filters": [
                            {
                                "dimensionName": "ga:eventLabel",
                                "operator": "EXACT",
                                "expressions": event_name
                            }
                        ]}],
                }
            ],
            "useResourceQuotas": True
        }
    ).execute()


def run_report(analytics_service, details):
    response = get_count_report(analytics_service, details['view'], details['event_name'])
    df = make_df(response['reports'][0])
    return df.at[0, 'ga:totalEvents'] + details['adjustment']


def main():
    analytics_service = initialize_analyticsreporting()

    with open(os.path.join(os.environ['CONFIG_DIR'], 'ga_config.json')) as json_data_file:
        config = json.load(json_data_file)
        counts = config['counts']

    output_file = os.path.join(os.environ['DATA_DIR'], 'counts.yml')
    # with open(output_file, 'r') as output:
    #     output_dict = yaml.load(output, yaml.RoundTripLoader)

    output_dict = {}

    for count in counts:
        total = run_report(analytics_service, counts[count])
        output_dict[count] = "{:,}".format(total)

    with open(output_file, 'w') as output:
        yaml.dump(output_dict, output, Dumper=yaml.RoundTripDumper, default_style='"')


if __name__ == '__main__':
    main()
