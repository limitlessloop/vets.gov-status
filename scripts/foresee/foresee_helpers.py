def make_table_from_foresee_response(response_items):
    score_url_table = []
    for item in response_items:
        score_url_table.append({
            'Satisfaction': list(filter(lambda ls: ls['name'] == 'Satisfaction', item['latentScores']))[0]['score'],
            'url': list(filter(lambda r: r['name'] == 'url', item['responses']))[0]['answers'][0]
        })
    return score_url_table
