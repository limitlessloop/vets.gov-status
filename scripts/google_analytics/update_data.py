"""Pulls in data to update dashboards"""
from analytics_helpers import make_df, initialize_analyticsreporting
from scripts.datehelpers.datetime_utils import find_sunday
import datetime
import json
import numpy as np
import os
import pandas as pd


def get_reports(analytics, view_id, page_filter):
    """Use the Analytics Service Object to query Analytics Reporting API.

    Pulls data from the prior full Sunday to 20 full weeks prior
    """
    startDate = (find_sunday() - datetime.timedelta(days=139)).isoformat()
    endDate = find_sunday().isoformat()

    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': startDate,
                                    'endDate': endDate}],
                    'metrics': [{'expression': 'ga:users'},
                                {'expression': 'ga:newUsers'}],
                    'dimensions': [{'name': 'ga:isoYearIsoWeek'}],
                    "dimensionFilterClauses": [{
                        "filters": [
                            {
                                "dimensionName": "ga:pagePath",
                                "operator": "REGEXP",
                                "expressions": page_filter
                            }
                        ]}],
                },
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': startDate,
                                    'endDate': endDate}],
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:isoYearIsoWeek'},
                                   {'name': 'ga:deviceCategory'}],
                    "dimensionFilterClauses": [{
                        "filters": [
                            {
                                "dimensionName": "ga:pagePath",
                                "operator": "REGEXP",
                                "expressions": page_filter
                            }
                        ]}],
                },
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': startDate,
                                    'endDate': endDate}],
                    'metrics': [{'expression': 'ga:pageviews'}],
                    'dimensions': [{'name': 'ga:isoYearIsoWeek'}],
                    "dimensionFilterClauses": [{
                        "filters": [
                            {
                                "dimensionName": "ga:pagePath",
                                "operator": "REGEXP",
                                "expressions": page_filter
                            }
                        ]}],
                }
            ],
            "useResourceQuotas": True
        }
    ).execute()


def get_click_reports(analytics, view_id):
    """Use the Analytics Service Object to query Analytics Reporting API.

    Pulls data from the prior full Sunday to 20 full weeks prior
    """
    startDate = (find_sunday() - datetime.timedelta(days=139)).isoformat()
    endDate = find_sunday().isoformat()

    return analytics.reports().batchGet(
        body={
            'reportRequests': [{
                'viewId': view_id,
                'dateRanges': [{'startDate': startDate,
                                'endDate': endDate}],
                'metrics': [{'expression': 'ga:totalEvents'}],
                'dimensions': [{'name': 'ga:isoYearIsoWeek'}],
                "dimensionFilterClauses": [{
                    "operator": "OR",
                    "filters": [
                        {
                            "dimensionName": "ga:eventLabel",
                            "operator": "PARTIAL",
                            "expressions": "veteranscrisisline"
                        },
                        {
                            "dimensionName": "ga:eventLabel",
                            "operator": "PARTIAL",
                            "expressions": "sms:838255"
                        },
                        {
                            "dimensionName": "ga:eventLabel",
                            "operator": "PARTIAL",
                            "expressions": "tel:18002738255"
                        },
                        {
                            "dimensionName": "ga:eventAction",
                            "operator": "PARTIAL",
                            "expressions": "veteranscrisisline"
                        },
                        {
                            "dimensionName": "ga:eventAction",
                            "operator": "PARTIAL",
                            "expressions": "sms:838255"
                        },
                        {
                            "dimensionName": "ga:eventAction",
                            "operator": "PARTIAL",
                            "expressions": "tel:18002738255"
                        },
                    ]}],
                "includeEmptyRows": "true",
            }
            ],
            "useResourceQuotas": True
        }
    ).execute()


def add_day_column(raw_df):
    if 'ga:isoYearIsoWeek' in raw_df.columns:
        # Set the day equal to the Sunday that ends that week
        raw_df['day'] = raw_df['ga:isoYearIsoWeek'].apply(
            lambda d: datetime.datetime.strptime(d + '-0', "%Y%W-%w"))
        raw_df['day'] = pd.to_datetime(raw_df['day'])
        raw_df = raw_df.set_index('day')
        del raw_df['ga:isoYearIsoWeek']
    return raw_df


def output_users(df, board):
    """Output a csv from dataframe contents."""

    if not df.empty:
        df.columns = ['new', 'all']
        del df['new']

    filename = os.path.join(os.environ['DATA_DIR'],
                            "{}_users.csv".format(board))
    df.to_csv(filename, date_format="%m/%d/%y")


def output_device(df, board):
    df = df.reset_index()

    if 'ga:deviceCategory' in df.columns:
        mobile = df[df['ga:deviceCategory'] != 'desktop'].groupby('day').agg(np.sum)
        mobile.columns = ['mobile']

        df = df[df['ga:deviceCategory'] == 'desktop'].groupby('day').agg(np.sum)
        df.columns = ['desktop']

        df['mobile'] = mobile['mobile']
        df['all'] = df['desktop'] + df['mobile']
        df['mobile'] = (df['mobile'] / df['all']) * 100
        df['desktop'] = (df['desktop'] / df['all']) * 100

    filename = os.path.join(os.environ['DATA_DIR'],
                            "{}_mobile.csv".format(board))
    df.to_csv(filename, date_format="%m/%d/%y")


def output_pageviews(df, board):
    """Output a csv from dataframe contents."""

    if not df.empty:
        df.columns = ['views']

    filename = os.path.join(os.environ['DATA_DIR'],
                            "{}_views.csv".format(board))
    df.to_csv(filename, date_format="%m/%d/%y")


def run_reports(analytics, board, view_id, page_filter=""):
    response = get_reports(analytics, view_id, page_filter)
    user_df = add_day_column(make_df(response['reports'][0]))
    output_users(user_df, board)
    device_df = add_day_column(make_df(response['reports'][1]))
    output_device(device_df, board)
    pageviews_df = add_day_column(make_df(response['reports'][2]))
    output_pageviews(pageviews_df, board)


def run_click_reports(analytics, board, view_id):
    response = get_click_reports(analytics, view_id)
    vcl_df = add_day_column(make_df(response['reports'][0]))
    output_clicks(vcl_df, board)


def output_clicks(df, board):
    """Output a csv from dataframe contents."""

    df.columns = ["all"]
    filename = os.path.join(os.environ['DATA_DIR'],
                            "{}_clicks.csv".format(board))
    df.to_csv(filename, date_format="%m/%d/%y")


def main():
    analytics = initialize_analyticsreporting()

    with open(os.path.join(os.environ['CONFIG_DIR'], 'ga_config.json')) as json_data_file:
        config = json.load(json_data_file)
        boards = config['charts']
        clicks = config['clicks']

    for board in boards:
        details = boards[board]
        run_reports(analytics, board, details['view'], details['page_filter'])

    for click in clicks:
        details = clicks[click]
        run_click_reports(analytics, click, details['view'])


if __name__ == '__main__':
    main()
