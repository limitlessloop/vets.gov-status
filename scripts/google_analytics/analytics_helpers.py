import pandas as pd
from credstash import getSecret
import json
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']


def initialize_analyticsreporting():
    """Initializes an analyticsreporting service object.

    Returns:
    analytics an authorized analyticsreporting service object.
    """

    secret_json = getSecret("serviceaccount", region="us-east-2")
    credentials = Credentials.from_service_account_info(json.loads(secret_json), scopes=SCOPES)

    # Build the service object.
    analytics_service = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics_service


def make_df(report):
    """Turn a single report from a Google Analytics response into dataframe"""

    dim_labels = [dim_label.split(':')[-1]
                  for dim_label
                  in report['columnHeader']['dimensions']]
    metric_labels = [entry['name'].split(':')[-1]
                     for entry
                     in report['columnHeader']['metricHeader']['metricHeaderEntries']]

    rows = report['data'].get('rows', [])
    if not rows:
        raise RuntimeError('Error in Google Analytics response.')

    output = []
    for row in rows:
        current_data = {}

        for k, v in zip(dim_labels, row['dimensions']):
            current_data[k] = v

        metric_values = [d['values'] for d in row['metrics']]
        metric_values = [item for sublist in metric_values for item in sublist]
        for k, v in zip(metric_labels, metric_values):
            current_data[k] = int(v)

        output.append(current_data)

    return pd.DataFrame(output)
