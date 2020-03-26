import logging
import os
import datetime
from ruamel import yaml

from fetch_data import get_ga_report
from foresee.foresee import get_measure_data, authenticate
from google_analytics.analytics_helpers import initialize_analyticsreporting
from google_analytics.ga_requests import get_all_transactions_request


def main():
    analytics_service = initialize_analyticsreporting()

    logging.info("Loading services.yml...")
    services_file_path = os.path.join(os.environ['CONFIG_DIR'], 'services.yml')
    with open(services_file_path, 'r') as services_file:
        yaml.load(services_file, yaml.RoundTripLoader)

    logging.info("Fetching transactions from Google Analytics...")
    get_ga_report(analytics_service, get_all_transactions_request())

    logging.info("Fetching CSAT scores from ForeSee...")
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    get_measure_data(authenticate(), yesterday.isoformat(), yesterday.isoformat())


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
