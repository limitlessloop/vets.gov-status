import requests
import re
import json
import csv
from os import path
from requests.auth import HTTPBasicAuth

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
        'authorization': "Basic <basic token>"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    pattern = "\"access_token\":\"(.*?)\","

    return re.search(pattern, response.text).group(1)


def get_measures(token):
    url = "https://api.foresee.com/v1/measures"

    headers = {
        'accept': APPLICATION_JSON
        , 'Authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def get_measure_definition(measure, file_path, token):
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


def get_measure_data(token, measure, from_date, to_date):
    offset = 0;
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    headers = {
        'accept': 'application/json',
        'authorization': BEARER_ + token
    }

    querystring = {
        "from": from_date,
        "to": to_date,
        "excludeResponseDetails": "false",
        "excludeMQ": "false",
        "excludeCQ": "false",
        "excludePassedParams": "false",
        "excludeLatentScores": "false",
        "offset": str(offset),
        "limit": "100"}

    while True:
        response = requests.request("GET", url, headers=headers, params=querystring)
        measure_data = convert_to_json(response.text)
        page_data = parse_json(measure_data)
        write_all_to_csv(all_csv_path, page_data)
        if measure_data['hasMore'] is not True:
            break
        offset += 1
        querystring['offset'] = str(offset)


def get_measure_data_using_odata(measure, from_date, to_date):
    respondents_scores_url = "https://api.foresee.com/v1/bi/cxmeasure/odata.svc/Measures(" \
          + measure \
          + ")/RespondentsScores?$filter=responseTime gt 2020-03-01 and latentName eq 'Satisfaction'"

    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", respondents_scores_url,
                                headers=headers,
                                auth=HTTPBasicAuth('saman.moshafi@va.gov', '1f35d458-69dd-4d2f-a45e-937f8e9c9efd'))
    mode = 'x'
    respondents_scores_file = "respondents_scores.json"
    if path.exists(respondents_scores_file):
        mode = 'w'
    with open(respondents_scores_file, mode) as json_file:
        json_file.write(response.text)

    responses_url = "https://api.foresee.com/v1/bi/cxmeasure/odata.svc/Measures(" \
                             + measure \
                             + ")/Responses?$filter=responseTime gt 2020-03-01 and questionName eq 'url'"
    response = requests.request("GET", responses_url,
                                headers=headers,
                                auth=HTTPBasicAuth('saman.moshafi@va.gov', '1f35d458-69dd-4d2f-a45e-937f8e9c9efd'))
    responses_file = "responses.json"
    mode = 'x'
    if path.exists(responses_file):
        mode = 'w'
    with open(responses_file, mode) as json_file:
        json_file.write(response.text)


measure_id = "8847572"
f_date = "2020-01-01"
t_date = "2020-03-17"
all_csv_path = \
    "/Users/samanmoshafi/Documents/va_foresee_measure_" \
    + measure_id + "_" + f_date + "_to_" + t_date + ".csv"
average_csv_path = "/Users/samanmoshafi/Documents/va_foresee_measure_" + measure_id + "_average.csv"

get_measure_data_using_odata(measure_id, f_date, t_date)

