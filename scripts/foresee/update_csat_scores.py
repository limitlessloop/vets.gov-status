import requests
import json
import csv
from os import path
from scripts.foresee.items import ScoreHolder

TO_DATE = "to_date"

FROM_DATE = "from_date"

APPLICATION_JSON = "application/json"

BEARER_ = "Bearer "


def foresee_authenticate():
    url = "https://api.foresee.com/v1/token"

    querystring = {"scope": "r_cx_basic", "grant_type": "client_credentials"}

    headers = {
        'accept': APPLICATION_JSON,
        'content-type': APPLICATION_JSON,
        'authorization': "Basic M0QwS2IzS2Q3RGlXM1A5WUdVVHhzWW5QY1YwZVN1bWI6SWQwZ2NCTFhIazk5NkNGNlRQbkY="
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    if response.status_code == 200:
        token_json = json.loads(response.text)
        return token_json['access_token']

    return None


def extract_measure_items(score_holder: ScoreHolder, measure_data):
    for measure_item in measure_data['items']:
        score_holder.add_measure_item(measure_item)


def get_measure_data(bearer_token, measure, from_date, to_date):
    offset = 0;
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    headers = {
        'accept': 'application/json',
        'authorization': BEARER_ + bearer_token
    }

    querystring = {
        "from": from_date,
        "to": to_date,
        "excludeResponseDetails": "false",
        "excludeMQ": "true",
        "excludeCQ": "false",
        "excludePassedParams": "false",
        "excludeLatentScores": "false",
        "offset": str(offset),
        "limit": "100"}

    score_holder = ScoreHolder()
    while True:
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            measure_data = json.loads(response.text)
            extract_measure_items(score_holder, measure_data)

        if measure_data['hasMore'] is not True:
            break
        offset += 1
        querystring['offset'] = str(offset)

    return score_holder


def generate_scores_dict(score_holder: ScoreHolder):
    scores_dict = {
        'overall-scores': score_holder.get_satisfaction_score(),
        'healthscare-scores': score_holder.geturl_satisfaction_score("health-care/apply")
    }
    return scores_dict


def get_dates():
    return {FROM_DATE: "2020-03-01", TO_DATE: "2020-03-15"}


def write_scores_to_csv(csv_file_path, dict_data):
    mode = 'x'
    if path.exists(csv_file_path):
        mode = 'w'

    with open(csv_file_path, mode) as csv_file:
        csv_columns = dict_data.keys()
        writer = csv.writer(csv_file)
        writer.writerow(csv_columns)

        values_row = []
        for one_column in csv_columns:
            values_row.append(dict_data[one_column])

        writer.writerow(values_row)


def main():
    measure_id = "8847572"
    bearer_token = foresee_authenticate()
    measure_dates = get_dates()
    score_holder = get_measure_data(bearer_token, measure_id, measure_dates[FROM_DATE], measure_dates[TO_DATE])
    scores_csv_path = \
        "/Users/samanmoshafi/Documents/va_foresee_measure_" \
        + measure_id + "_" + measure_dates[FROM_DATE] + "_to_" + measure_dates[TO_DATE] + ".csv"
    write_scores_to_csv(scores_csv_path, generate_scores_dict(score_holder))


if __name__ == '__main__':
    main()
