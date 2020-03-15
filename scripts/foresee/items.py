
def extract_satisfaction(scores_dict):
    for latent_scores in scores_dict:
        if latent_scores['name'] == 'Satisfaction':
            return latent_scores['score']
    return None


def extract_url_answers(responses):
    for one_response in responses:
        if one_response['name'] == 'url':
            return one_response['answers']
    return []


class MeasureItem:

    def __init__(self, content: {}):
        self.satisfaction = extract_satisfaction(content['latentScores'])
        self.url_answers = extract_url_answers(content['responses'])

    def get_satisfaction_score(self):
        return self.satisfaction

    def get_url_answers(self):
        return self.url_answers
