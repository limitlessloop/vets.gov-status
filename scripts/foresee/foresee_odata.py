from os import environ, path
import csv
import requests
from requests.auth import HTTPBasicAuth
import logging
from itertools import zip_longest
import pandas as pd
from scripts.datehelpers import find_last_twelve_months

COMMON_KEY = 'respondentId'


def get_measure_data(measure, from_date, to_date):
    headers = {
        'accept': 'application/json'
    }
    basic_filter = \
        "responseTime gt " + from_date + " and responseTime lt " + to_date
    scores_items = get_score_items(headers, basic_filter, measure)

    responses_items = get_responses_items(basic_filter, headers, measure)

    return merge_item_lists(responses_items, scores_items)


def merge_item_lists(responses_items, scores_items):
    # return [{**left, **right} for left, right in
    #         zip_longest(sorted(scores_items, key=lambda item: item['respondentId']),
    #                     sorted(responses_items, key=lambda item: item['respondentId']), fillvalue={})]
    responses_df = pd.DataFrame(responses_items).set_index(COMMON_KEY)
    scores_df = pd.DataFrame(scores_items).set_index(COMMON_KEY)
    merged_df = responses_df.merge(scores_df, left_index=True, right_index=True)
    return list(merged_df.T.to_dict().values())


def get_responses_items(basic_filter, headers, measure):
    responses_url = \
        "https://api.foresee.com/v1/bi/cxmeasure/odata.svc/Measures(" \
        + measure \
        + ")/Responses?$filter=" + basic_filter + " and questionName eq 'url'"
    response = requests.request("GET", responses_url,
                                headers=headers,
                                auth=HTTPBasicAuth('saman.moshafi@va.gov', '1f35d458-69dd-4d2f-a45e-937f8e9c9efd'))
    if response.status_code != 200:
        raise RuntimeError(str(response.status_code) + " " + response.text)
    return response.json()['value']


def get_score_items(headers, basic_filter, measure):
    respondents_scores_url = \
        "https://api.foresee.com/v1/bi/cxmeasure/odata.svc/Measures(" \
        + measure \
        + ")/RespondentsScores?$filter=" + basic_filter + " and latentName eq 'Satisfaction'"

    response = requests.request("GET", respondents_scores_url,
                                headers=headers,
                                auth=HTTPBasicAuth(environ.get('USERID'), environ.get('USERPWD')))
    if response.status_code != 200:
        raise RuntimeError(str(response.status_code) + " " + response.text)
    return response.json()['value']


def calculate_average_satisfaction(items):
    extracted_csats = [item['latentScore'] for item in items]
    return round(sum(extracted_csats) / len(items), 2)


def fetch_last_12_months_data():
    last_year_data = []
    last_twelve_months = find_last_twelve_months()

    measure_id = "8847572"

    # get values for the last 12 months and calculate average for each month
    for start_end_date in last_twelve_months:
        month_data = get_measure_data(measure_id, start_end_date[0].isoformat(),
                                      start_end_date[1].isoformat())
        month_year_text = str(start_end_date[0].month) + '/' + str(start_end_date[0].year)
        one_month_dict = {
            'month': month_year_text,
            'month_data': month_data,
            'csat_score': calculate_average_satisfaction(month_data)
        }
        last_year_data.append(one_month_dict)
        logging.info("Calculated %s average: %.2f", month_year_text, one_month_dict['csat_score'])

    last_year_data.reverse()
    return last_year_data


def calculate_overall_average_satisfaction(last_year_data):
    all_data = []
    for one_month_data in last_year_data:
        all_data.extend(one_month_data['month_data'])
    return calculate_average_satisfaction(all_data)


def write_to_csv(twelve_months_scores):
    full_filename = path.join(environ['DATA_DIR'], 'csat_score.csv')
    mode = 'x'
    if path.exists(full_filename):
        mode = 'w'

    with open(full_filename, mode) as csv_file:
        csv_columns = ['csat_score', 'month']
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(twelve_months_scores)


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    # get dates for last 12 months
    last_year_data = fetch_last_12_months_data()
    # calculate average for the whole period
    calculate_overall_average_satisfaction(last_year_data)
    write_to_csv(last_year_data)


if __name__ == '__main__':
    main()
