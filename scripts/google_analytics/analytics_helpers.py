from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
import pandas as pd

from scripts.google_analytics.datetime_utils import reformat_date


def initialize_analyticsreporting():
    """Initializes an analyticsreporting service object.

    Returns:
    analytics an authorized analyticsreporting service object.
    """
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

    credentials = Credentials.from_service_account_file(os.environ['GA_SERVICEACCOUNT'], scopes=SCOPES)

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

    table = make_table(rows, dim_labels, metric_labels)

    return pd.DataFrame(table)


def get_totals_from_report(report):
    return [int(total['values'][0]) for total in report['data']['totals']]


def make_table(rows, dim_labels, metric_labels):
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

    return output


def calculate_trend(previous_total, recent_total):
    return ((recent_total - previous_total) / previous_total) * 100


def add_month_column(raw_df):
    if 'yearMonth' in raw_df.columns:
        raw_df['date'] = raw_df['yearMonth'].apply(
            lambda d: reformat_date(d))
        del raw_df['yearMonth']
    return raw_df
