import os

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

from analytics_helpers import make_df

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.environ['GA_SERVICEACCOUNT']
SERVICE_ACCOUNT_EMAIL = 'analytics@inductive-voice-142915.iam.gserviceaccount.com'


def initialize_analytics_service():
    credentials = Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

    # Build the service object.
    analytics_service = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics_service


def get_transactions_report(analytics_service, view_id):
    return analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': '90daysAgo',
                                    'endDate': 'yesterday'}],
                    'metrics': [{'expression': 'ga:totalEvents'}],
                    'segments': [
                        {'segmentId': 'sessions::condition::ga:dimension22=@1,ga:dimension22=@3'}
                    ],
                    'dimensions': [
                        {'name': 'ga:segment'},
                        {'name': 'ga:isoYearIsoWeek'}
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
    view_id_vadotgov = "176188361"
    response = get_transactions_report(analytics_service, view_id_vadotgov)
    report = response['reports'][0]
    print(report['data']['rowCount'])
    print('total', report['data']['totals'][0]['values'])
    df = make_df(report)
    return df


def write_df_to_csv(df):
    filename = os.path.join(os.environ['DATA_DIR'], "all_transactions.csv")
    df.to_csv(filename, date_format="%m/%d/%y")


def main():
    analytics_service = initialize_analytics_service()

    df = run_report(analytics_service)

    write_df_to_csv(df)


if __name__ == '__main__':
    main()
