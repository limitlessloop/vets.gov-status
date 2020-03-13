import requests
import re
import json
import csv
from os import path

APPLICATION_JSON = "application/json"

BEARER_ = "Bearer "


def convert_to_json(text):
    return json.loads(text)


def parse_json(data_dict):
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
        mode = 'a'

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
        'authorization': "Basic M0QwS2IzS2Q3RGlXM1A5WUdVVHhzWW5QY1YwZVN1bWI6SWQwZ2NCTFhIazk5NkNGNlRQbkY="
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


def get_measure_definition(measure, file_path):
    url = "https://api.foresee.com/v1/measures/" + measure + "/definition"

    querystring = {"excludeQuestions": "false", "excludeAnswers": "true"}

    headers = {
        'accept': APPLICATION_JSON,
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    mode = 'x'
    if path.exists(file_path):
        mode = 'w'

    with open(file_path, mode) as outfile:
        outfile.write(response.text)
    print(response.text)


def get_measure_data(measure: str):
    get_measure_data_by_page(measure, 0)


def get_measure_data_by_page(measure: str, offset: int):
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    querystring = {"from": from_date, "to": to_date, "excludeResponseDetails": "true", "excludeMQ": "false",
                   "excludeCQ": "true", "excludePassedParams": "true", "excludeLatentScores": "false", "offset": str(offset),
                   "limit": "100"}

    headers = {
        'accept': 'application/json',
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data_dict = convert_to_json(response.text)
    page_data = parse_json(data_dict)
    write_all_to_csv(all_csv_path, page_data)
    if data_dict['hasMore'] is True:
        get_measure_data_by_page(measure, offset+1)


def get_measure_data2(measure: str):
    offset = 0;
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    headers = {
        'accept': 'application/json',
        'authorization': BEARER_ + token
    }

    querystring = {"from": from_date, "to": to_date, "excludeResponseDetails": "true", "excludeMQ": "false",
                   "excludeCQ": "true", "excludePassedParams": "false", "excludeLatentScores": "false",
                   "offset": str(offset),
                   "filter": "url co healthcare",
                   "limit": "100"}

    while True:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data_dict = convert_to_json(response.text)
        page_data = parse_json(data_dict)
        write_all_to_csv(all_csv_path, page_data)
        if data_dict['hasMore'] is not True:
            break
        offset += 1
        querystring['offset'] = str(offset)


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
measure_id = "8847572"
all_csv_path = "/Users/samanmoshafi/Documents/va_foresee_measure_" + measure_id + "_all.csv"
# average_csv_path = "/Users/samanmoshafi/Documents/va_foresee_measure_" + measure_id + "_average.csv"
# get_measure_definition(measure_id,
#                        "/Users/samanmoshafi/Documents/va_foresee_measure_" + measure_id + "_definition.json")
from_date = "2020-01-01"
to_date = "2020-03-11"
get_measure_data2(measure_id)
# write_average_to_csv(average_csv_path, measure_dict)
# write_all_to_csv(all_csv_path, measure_dict)
# get_measure_data(measure_id, "2015-01-02", "2016-01-01")
# get_measure_data(measure_id, "2016-01-02", "2017-01-01")
# get_measure_data(measure_id, "2017-01-02", "2018-01-01")
# get_measure_data(measure_id, "2018-01-02", "2019-01-01")
# get_measure_data(measure_id, "2019-01-02", "2020-01-01")
# get_projects()
