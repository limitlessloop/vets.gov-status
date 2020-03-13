from analytics_helpers import make_df, initialize_analyticsreporting
from datetime_utils import find_last_full_twelve_months, reformat_date
import os

VADOTGOV_VIEWID = '176188361'


def get_transactions_report(analytics_service):
    start_date, end_date = find_last_full_twelve_months()

    return analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VADOTGOV_VIEWID,
                    'dateRanges': [{'startDate': start_date,
                                    'endDate': end_date}],
                    'metrics': [{'expression': 'ga:totalEvents'}],
                    'dimensions': [
                        {'name': 'ga:yearMonth'}
                    ],
                    'dimensionFilterClauses': [
                        {
                            'operator': 'AND',
                            'filters': [
                                {
                                    'dimensionName': 'ga:eventCategory',
                                    'operator': 'EXACT',
                                    'expressions': ['Transactions']
                                },
                                {
                                    'dimensionName': 'ga:pagePath',
                                    'operator': 'REGEXP',
                                    'expressions': ['www.va.gov/']
                                }
                            ]
                        }
                    ],
                }
            ],
            "useResourceQuotas": False
        }
    ).execute()


def run_report(analytics_service):
    response = get_transactions_report(analytics_service)
    report = response['reports'][0]
    df = make_df(report)
    return df


def add_month_column(raw_df):
    if 'yearMonth' in raw_df.columns:
        raw_df['date'] = raw_df['yearMonth'].apply(
            lambda d: reformat_date(d))
        del raw_df['yearMonth']
    return raw_df


def write_df_to_csv(df):
    filename = os.path.join(os.environ['DATA_DIR'], "all_transactions.csv")
    df.to_csv(filename, date_format="%m/%d/%y")


def main():
    analytics_service = initialize_analyticsreporting()

    df = run_report(analytics_service)
    df = add_month_column(df)

    write_df_to_csv(df)


if __name__ == '__main__':
    main()
