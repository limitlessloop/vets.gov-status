from re import search, RegexFlag


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

    def __init__(self, item_content):
        self.satisfaction = extract_satisfaction(item_content['latentScores'])
        self.url_answers = extract_url_answers(item_content['responses'])

    def get_satisfaction_score(self):
        return self.satisfaction

    def get_url_answers(self):
        return self.url_answers

    def does_url_contain_pattern(self, pattern):
        for answer in self.url_answers:
            if search(pattern, answer, RegexFlag.IGNORECASE):
                return True
        return False


class ScoreHolder:

    def __init__(self):
        self.measure_item_list = []
        self.satisfaction_score = 0.0

    def add_measure_item(self, measure_item_data_dict):
        measure_item = MeasureItem(measure_item_data_dict)
        self.measure_item_list.append(measure_item)
        self.satisfaction_score += measure_item.get_satisfaction_score()

    def measure_size(self):
        return len(self.measure_item_list)

    def get_satisfaction_score(self):
        return round(self.satisfaction_score / len(self.measure_item_list), 1)

    def geturl_satisfaction_score(self, pattern):
        url_filter_satisfaction_score = 0.0
        url_filter_counter = 0;
        for measure_item in self.measure_item_list:
            if measure_item.does_url_contain_pattern(pattern):
                url_filter_counter += 1
                url_filter_satisfaction_score += measure_item.get_satisfaction_score()
        return round(url_filter_satisfaction_score / url_filter_counter, 1)
