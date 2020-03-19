from ruamel import yaml

from analytics_helpers import make_df, initialize_analyticsreporting, get_totals_from_report
from datetime_utils import reformat_date
from requests import get_logged_in_users_request, get_all_transactions_request, get_last_month_users_request
import os


def get_ga_report(analytics_service, request):
    return analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                request
            ],
            "useResourceQuotas": False
        }
    ).execute()


def run_report(analytics_service, request):
    response = get_ga_report(analytics_service, request)
    report = response['reports'][0]
    df = make_df(report)
    total = get_totals_from_report(report)[0]
    return df, total


def run_report_and_get_total_with_trend(analytics_service, request):
    response = get_ga_report(analytics_service, request)
    report = response['reports'][0]
    recent_total, previous_total = get_totals_from_report(report)

    trend = ((recent_total - previous_total) / previous_total) * 100

    return recent_total, trend


def add_month_column(raw_df):
    if 'yearMonth' in raw_df.columns:
        raw_df['date'] = raw_df['yearMonth'].apply(
            lambda d: reformat_date(d))
        del raw_df['yearMonth']
    return raw_df


def write_df_to_csv(df, filename):
    full_filename = os.path.join(os.environ['DATA_DIR'], filename)
    df.to_csv(full_filename, date_format="%m/%d/%y")


def fetch_data_for_service(analytics_service, service):
    print("Getting data for '%s'" % service["title"])

    if "page_path_filter" in service:
        users_total, users_trend = run_report_and_get_total_with_trend(analytics_service, get_last_month_users_request(service["page_path_filter"]))
    else:
        users_total = 0
        users_trend = 0

    return {
        "title": service["title"],
        # TODO: get real data for each service
        "csat": 76,
        "csat_trend": 12,
        "users": users_total,
        "users_trend": users_trend,
        "tools": [
            {
                "title": tool["title"],
                "transactions": 49123
            }
            for tool in service["tools"]
        ]
    }


def main():
    analytics_service = initialize_analyticsreporting()

    df, transactions_total = run_report(analytics_service, get_all_transactions_request())
    df = add_month_column(df)
    write_df_to_csv(df, "all_transactions.csv")

    df, users_total = run_report(analytics_service, get_logged_in_users_request())
    df = add_month_column(df)
    write_df_to_csv(df, "all_logged_in_users.csv")

    counts = {
        "transactions_total": transactions_total,
        "users_total": users_total
    }

    services_file_path = os.path.join(os.environ['CONFIG_DIR'], 'services.yml')
    with open(services_file_path, 'r') as services_file:
        services_input = yaml.load(services_file, yaml.RoundTripLoader)
        services = services_input["services"]
        counts["services"] = [
            fetch_data_for_service(analytics_service, service)
            for service in services
        ]

    output_file = os.path.join(os.environ['DATA_DIR'], 'counts.yml')
    with open(output_file, 'w') as output:
        yaml.dump(counts, output, default_flow_style=False)


if __name__ == '__main__':
    main()
