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


def fetch_data_for_services(services):
    return [
        {
            "title": service["title"],
            # TODO: get real data for each service
            "csat": 76,
            "csat_trend": 12,
            "users": 2926183,  # make some query using service["page_path_filter"]
            "users_trend": -9,
            "tools": [
                {
                    "title": tool["title"],
                    "transactions": 49123
                }
                for tool in service["tools"]
            ]
        }
        for service in services
    ]


def main():
    analytics_service = initialize_analyticsreporting()

    df, transactions_total = run_report(analytics_service, get_all_transactions_request)
    df = add_month_column(df)
    write_df_to_csv(df, "all_transactions.csv")

    df, users_total = run_report(analytics_service, get_logged_in_users_request)
    df = add_month_column(df)
    write_df_to_csv(df, "all_logged_in_users.csv")

    counts = {
        "transactions_total": transactions_total,
        "users_total": users_total
    }

    services_file_path = os.path.join(os.environ['CONFIG_DIR'], 'services.yml')
    with open(services_file_path, 'r') as services_file:
        services_input = yaml.load(services_file, yaml.RoundTripLoader)
        counts["services"] = fetch_data_for_services(services_input["services"])

    output_file = os.path.join(os.environ['DATA_DIR'], 'counts.yml')
    with open(output_file, 'w') as output:
        yaml.dump(counts, output, default_flow_style=False)


if __name__ == '__main__':
    main()
