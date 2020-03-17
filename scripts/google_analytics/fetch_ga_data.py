from ruamel import yaml

from analytics_helpers import make_df, initialize_analyticsreporting, get_total_from_report
from datetime_utils import find_last_full_twelve_months, reformat_date
from requests import get_logged_in_users_request, get_all_transactions_request
import os


def get_ga_report(analytics_service, get_request):
    start_date, end_date = find_last_full_twelve_months()

    return analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                get_request(start_date, end_date)
            ],
            "useResourceQuotas": False
        }
    ).execute()


def run_report(analytics_service, get_request):
    response = get_ga_report(analytics_service, get_request)
    report = response['reports'][0]
    df = make_df(report)
    total = get_total_from_report(report)
    return df, total


def add_month_column(raw_df):
    if 'yearMonth' in raw_df.columns:
        raw_df['date'] = raw_df['yearMonth'].apply(
            lambda d: reformat_date(d))
        del raw_df['yearMonth']
    return raw_df


def write_df_to_csv(df, filename):
    full_filename = os.path.join(os.environ['DATA_DIR'], filename)
    df.to_csv(full_filename, date_format="%m/%d/%y")


def main():
    analytics_service = initialize_analyticsreporting()

    df, transactions_total = run_report(analytics_service, get_all_transactions_request)
    df = add_month_column(df)
    write_df_to_csv(df, "all_transactions.csv")

    df, users_total = run_report(analytics_service, get_logged_in_users_request)
    df = add_month_column(df)
    write_df_to_csv(df, "all_logged_in_users.csv")

    totals = {
        "transactions_total": transactions_total,
        "users_total": users_total,
        # TODO: real data please
        "services": [
            {
                "title": "Disability",
                "users": 12345,
                "csat": 76,
                "tools": [
                    {
                        "title": "Apply for Disability",
                        "transactions": 12919
                    },
                    {
                        "title": "Something else",
                        "transactions": 12345
                    }
                ]
            },
            {
                "title": "Health Care",
                "users": 266542,
                "csat": 54,
                "tools": [
                    {
                        "title": "Apply for Health Care",
                        "transactions": 124134
                    }
                ]
            }
        ]
    }

    output_file = os.path.join(os.environ['DATA_DIR'], 'counts.yml')
    with open(output_file, 'w') as output:
        yaml.dump(totals, output, default_flow_style=False)


if __name__ == '__main__':
    main()
