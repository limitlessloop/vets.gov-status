import requests
import re

APPLICATION_JSON = "application/json"

BEARER_ = "Bearer "


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

    querystring = {"excludeQuestions": "false", "excludeAnswers": "false"}

    headers = {
        'accept': APPLICATION_JSON,
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def get_measure_data(measure):
    url = "https://api.foresee.com/v1/measures/" + measure + "/data"

    querystring = {"from": "2018-01-02", "to": "2019-01-01", "excludeResponseDetails": "true", "excludeMQ": "false",
                   "excludeCQ": "false", "excludePassedParams": "false", "excludeLatentScores": "false", "offset": "0",
                   "limit": "100"}

    headers = {
        'accept': APPLICATION_JSON,
        'authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def get_projects():
    url = "https://api.foresee.com/v1/projects"

    headers = {
        'accept': '*/*'
        , 'Authorization': BEARER_ + token
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


token = foresee_authenticate()
get_measures()
get_measure_definition("8840868")
get_measure_data("8840868")
# get_projects()
