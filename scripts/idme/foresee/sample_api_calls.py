import requests
import re
import json
import csv
from os import path

APPLICATION_JSON = "application/json"

BEARER_ = "Bearer "


def convert_to_json(text):
    return json.loads(text)


def parse_json(text):
    data_dict = convert_to_json(text)
    graph_data = {}
    for item in data_dict['items']:
        parse_one_item(item, graph_data)
    return graph_data


def parse_one_item(item, graph_data):
    latent_scores = item['latentScores']
    for one_score in latent_scores:
        add_to_dict(one_score['name'], one_score['score'], graph_data)


def add_to_dict(key, value, graph_data):
    if key not in graph_data:
        graph_data[key] = []
    graph_data[key].append(value)


def write_all_to_csv(csv_file_path, dict_data):
    mode = 'x'
    if path.exists(csv_file_path):
        mode = 'w'

    with open(csv_file_path, mode) as csv_file:
        csv_columns = dict_data.keys()
        writer = csv.writer(csv_file)
        writer.writerow(csv_columns)

        columnar_data = []
        for one_column in csv_columns:
            columnar_data.append(dict_data[one_column])
        all_rows = list(zip(*columnar_data))

        for one_row in all_rows:
            writer.writerow(one_row)


def get_average_score(key, data_dict):
    score_list = data_dict[key]
    return sum(score_list) / len(score_list)


def write_average_to_csv(csv_file_path, dict_data):
    mode = 'x'
    if path.exists(csv_file_path):
        mode = 'w'

    with open(csv_file_path, mode) as csv_file:
        csv_columns = dict_data.keys()
        writer = csv.writer(csv_file)
        writer.writerow(csv_columns)
        score_list = []

        for one_column in csv_columns:
            score_list.append(get_average_score(one_column, dict_data))
        writer.writerow(score_list)


def foresee_authenticate():
    url = "https://api.foresee.com/v1/token"

    querystring = {"scope": "r_cx_basic", "grant_type": "client_credentials"}

    headers = {
        'accept': APPLICATION_JSON,
        'content-type': APPLICATION_JSON,
        'authorization': "Basic akhGY0VGN3h4UzRnU1pTNjZ0aldCcTFzblh6UzA4dDg6aGsyQmF2YmJZQ0xpMTNscE5hUXk"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    pattern = "\"access_token\":\"(.*?)\","

    return re.search(pattern, response.text).group(1)


def get_measures():
    url = "https://api.foresee.com/v1/measures"

    headers = {
        'accept': APPLICATION_JSON
        , 'Authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def get_measure_definition(measure):
    url = "https://api.foresee.com/v1/measures/" + measure + "/definition"

    querystring = {"excludeQuestions": "false", "excludeAnswers": "true"}

    headers = {
        'accept': APPLICATION_JSON,
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def get_measure_data(measure, from_date, to_date):
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    querystring = {"from": from_date, "to": to_date, "excludeResponseDetails": "true", "excludeMQ": "false",
                   "excludeCQ": "false", "excludePassedParams": "false", "excludeLatentScores": "false", "offset": "0",
                   "limit": "100"}

    headers = {
        'accept': 'application/json',
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return parse_json(response.text)


def get_projects():
    url = "https://api.foresee.com/v1/projects"

    headers = {
        'accept': '*/*'
        , 'Authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


token = foresee_authenticate()
# get_measures()
measure_id = "8843006"
# get_measure_definition(measure_id)
measure_dict = get_measure_data(measure_id, "2014-01-02", "2015-01-01")
write_average_to_csv("/Users/samanmoshafi/Documents/foresee_measure_8843006_average.csv", measure_dict)
write_all_to_csv("/Users/samanmoshafi/Documents/foresee_measure_8843006_all.csv", measure_dict)
# get_measure_data(measure_id, "2015-01-02", "2016-01-01")
# get_measure_data(measure_id, "2016-01-02", "2017-01-01")
# get_measure_data(measure_id, "2017-01-02", "2018-01-01")
# get_measure_data(measure_id, "2018-01-02", "2019-01-01")
# get_measure_data(measure_id, "2019-01-02", "2020-01-01")
# get_projects()
