from google_analytics.analytics_helpers import make_df, initialize_analyticsreporting, get_totals_from_report, \
    calculate_trend
from google_analytics.datetime_utils import reformat_date
from google_analytics.requests import get_logged_in_users_request, get_all_transactions_request, \
    get_last_month_users_request, get_transactions_for_tools_request
from ruamel import yaml
from tenacity import retry, wait_fixed, stop_after_attempt
import os


@retry(wait=wait_fixed(10), stop=stop_after_attempt(5))
def get_ga_report(analytics_service, request):
    response = analytics_service.reports().batchGet(
        body={
            'reportRequests': [
                request
            ],
            "useResourceQuotas": False
        }
    ).execute()

    return response['reports'][0]


def run_report(analytics_service, request):
    report = get_ga_report(analytics_service, request)
    df = make_df(report)
    total = get_totals_from_report(report)[0]
    return df, total


def run_report_and_get_total_with_trend(analytics_service, request):
    report = get_ga_report(analytics_service, request)
    recent_total, previous_total = get_totals_from_report(report)

    trend = calculate_trend(previous_total, recent_total)

    return recent_total, trend


def run_report_and_get_total(analytics_service, request):
    report = get_ga_report(analytics_service, request)
    total = get_totals_from_report(report)[0]
    return total


def add_month_column(raw_df):
    if 'yearMonth' in raw_df.columns:
        raw_df['date'] = raw_df['yearMonth'].apply(
            lambda d: reformat_date(d))
        del raw_df['yearMonth']
    return raw_df


def write_df_to_csv(df, filename):
    full_filename = os.path.join(os.environ['DATA_DIR'], filename)
    df.to_csv(full_filename, date_format="%m/%d/%y")


def fetch_transactions_for_tool(analytics_service, tool):
    total_transactions = run_report_and_get_total(
        analytics_service,
        get_transactions_for_tools_request(tool)
    )
    return {
        "title": tool["title"],
        "transactions": total_transactions
    }


def fetch_data_for_service(analytics_service, service):
    print("Getting data for '%s'" % service["title"])

    users_total, users_trend = run_report_and_get_total_with_trend(
        analytics_service,
        get_last_month_users_request(service["page_path_filter"])
    )

    service_data = {
        "title": service["title"],
        "users_total": users_total,
        "users_trend": users_trend,
        "csat": 76,
        "csat_trend": 12,
        "tools": [
            fetch_transactions_for_tool(analytics_service, tool)
            for tool in service["tools"]
        ]
    }

    return service_data


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
