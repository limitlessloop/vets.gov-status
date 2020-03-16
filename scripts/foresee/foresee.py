from os import environ
import requests
import logging

def authenticate():
    url = "https://api.foresee.com/v1/token"

    querystring = {"scope": "r_cx_basic", "grant_type": "client_credentials"}

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': "Basic "+ environ.get('FORSEE_CREDENTIALS')
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
        "excludeResponseDetails": "true",
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
    
    return measure_data

def calculate_average_satisfaction(items):
    extracted_csats =  (next(latent_score['score'] for latent_score in item['latentScores'] if latent_score['name'] == 'Satisfaction') for item in items)
    return sum(extracted_csats) / len(items)
    

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    measure_id = "8847572"
    bearer_token = authenticate()
    data = get_measure_data(bearer_token, measure_id, "2020-03-01", "2020-03-15")
    avg = calculate_average_satisfaction(data)
    logging.info("Calculated average: {}".format(avg))

if __name__ == '__main__':
    main()