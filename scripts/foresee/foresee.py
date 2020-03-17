from os import environ
import requests
import logging
from scripts.datehelpers import find_last_twelve_months


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
        'authorization': "Bearer " + bearer_token
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
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code != 200:
            raise RuntimeError()
        response_json = response.json()
        has_more = response_json['hasMore']
        offset += 1
        querystring['offset'] = str(offset)
        measure_data.extend(response_json['items'])

    logging.debug(measure_data)
    return measure_data


def calculate_average_satisfaction(items):
    extracted_csats = (next(latent_score['score'] for latent_score in item['latentScores'] if latent_score['name'] == 'Satisfaction') for item in items)
    return sum(extracted_csats) / len(items)


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
            'month': month_year_text,
            'month_data': month_data,
            'csat_score': calculate_average_satisfaction(month_data)
        }
        last_year_data.append(one_month_dict)
        logging.info("Calculated %s average: %.2f", month_year_text, one_month_dict['cast_score'])
    return last_year_data


def calculate_overall_average_satisfaction(last_year_data):
    all_data = []
    for one_month_data in last_year_data:
        all_data.extend(one_month_data['month_data'])
    return calculate_average_satisfaction(all_data)


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    # get dates for last 12 months
    fetch_last_12_months_data()
    # calculate average for the whole period


if __name__ == '__main__':
    main()