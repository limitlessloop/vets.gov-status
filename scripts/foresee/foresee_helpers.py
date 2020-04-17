import logging


def make_table_from_foresee_response(response_items):
    score_url_table = []
    for item in response_items:
        url_responses = list(filter(lambda r: r['name'] == 'url', item['responses']))
        if url_responses:
            try:
                score_url_table.append({
                    'Satisfaction': list(filter(lambda ls: ls['name'] == 'Satisfaction', item['latentScores']))[0][
                        'score'],
                    'url': url_responses[0]['answers'][0]
                })
            except LookupError:
                logging.warning("failed to parse " + str(item))
    return score_url_table


def get_average_score(df, url):
    return float(df[df['url'].str.contains(url)].mean(axis=0)['Satisfaction'])
