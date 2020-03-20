from os import environ, path
import csv
import requests
import logging
from scripts.datehelpers import find_last_twelve_months

AUTHORIZATION = 'authorization'

CSAT_SCORE = 'csat_score'
MONTH_DATA = 'month_data'
DATE_COLUMN = 'date'


def authenticate():
    url = "https://api.foresee.com/v1/token"

    querystring = {"scope": "r_cx_basic", "grant_type": "client_credentials"}

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': "Basic " + environ.get('FORSEE_CREDENTIALS')
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    if response.status_code != 200:
        raise PermissionError

    return response.json()['access_token']


def get_measure_data(bearer_token, measure, from_date, to_date):
    offset = 0
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"
    headers = {
        'accept': 'application/json',
        AUTHORIZATION: "Bearer " + bearer_token
    }
    querystring = {
        "from": from_date,
        "to": to_date,
        "excludeResponseDetails": "false",
        "excludeMQ": "true",
        "excludeCQ": "true",
        "excludePassedParams": "false",
        "excludeLatentScores": "false",
        "offset": str(offset),
        "limit": "100"
    }
    measure_data = []
    has_more = True

    while has_more:
        logging.info("Downloading page: {:n} ".format(offset))
        response = send_one_request(headers, querystring, url)
        response_json = response.json()
        has_more = response_json['hasMore']
        offset += 1
        querystring['offset'] = str(offset)
        measure_data.extend(response_json['items'])

    logging.debug(measure_data)
    return measure_data


def send_one_request(headers, querystring, url):
    request_counter = 3
    should_try = True
    while should_try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code != 200:
            fail_reason = str(response.status_code) + " " + response.text
            # try for 3 times
            request_counter -= 1
            if request_counter > 0:
                logging.warning("request to foresee failed, trying again. The reason was " + fail_reason)
                renew_token(headers)
                continue
            else:
                raise RuntimeError(fail_reason)
    return response


def renew_token(headers):
    new_token = authenticate()
    headers[AUTHORIZATION] = "Bearer " + new_token


def calculate_average_satisfaction(items):
    extracted_csats = (
        next(latent_score['score']
             for latent_score in item['latentScores'] if latent_score['name'] == 'Satisfaction')
        for item in items
    )
    return round(sum(extracted_csats) / len(items), 2)


def fetch_last_12_months_data():
    last_year_data = []
    last_twelve_months = find_last_twelve_months()

    measure_id = "8847572"
    bearer_token = authenticate()

    # get values for the last 12 months and calculate average for each month
    for start_end_date in last_twelve_months:
        month_data = get_measure_data(bearer_token, measure_id, start_end_date[0].isoformat(),
                                      start_end_date[1].isoformat())
        month_year_text = str(start_end_date[0].month) + '/' + str(start_end_date[0].year)
        one_month_dict = {
            DATE_COLUMN: month_year_text,
            MONTH_DATA: month_data,
            CSAT_SCORE: calculate_average_satisfaction(month_data)
        }
        last_year_data.append(one_month_dict)
        logging.info("Calculated %s average: %.2f", month_year_text, one_month_dict[CSAT_SCORE])
    return last_year_data


def calculate_overall_average_satisfaction(last_year_data):
    all_data = []
    for one_month_data in last_year_data:
        all_data.extend(one_month_data[MONTH_DATA])
    return calculate_average_satisfaction(all_data)


def write_to_csv(twelve_months_scores):
    full_filename = path.join(environ['DATA_DIR'], 'csat_score.csv')
    mode = 'x'
    if path.exists(full_filename):
        mode = 'w'

    with open(full_filename, mode) as csv_file:
        csv_columns = [DATE_COLUMN, CSAT_SCORE]
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(twelve_months_scores)


def update_csat():
    # get dates for last 12 months
    last_year_data = fetch_last_12_months_data()
    # calculate average for the whole period
    overall_average_score = calculate_overall_average_satisfaction(last_year_data)
    write_to_csv(last_year_data)
    return overall_average_score


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    update_csat()


if __name__ == '__main__':
    main()
