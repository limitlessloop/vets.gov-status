import unittest
import json
from scripts.foresee.items import MeasureItem, ScoreHolder


class JsonTextTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.response_str = \
            "{\"hasMore\":true,\"total\":5221,\"items\":[{\"id\":\"V185Vop4U5hthwFF5cUdRA4C\"," \
            "\"responseTime\":\"2020-01-01T07:52:36.000-05:00\",\"experienceDate\":\"2020-01-01\",\"latentScores\":[{" \
            "\"id\":\"ENM006991L0009\",\"name\":\"Primary Resource\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0008\",\"name\":\"Recommend Site\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0007\",\"name\":\"Return\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0006\",\"name\":\"Satisfaction\",\"type\":\"SATISFACTION\",\"score\":100}," \
            "{\"id\":\"ENM006991L0005\",\"name\":\"Site Information\",\"type\":\"ELEMENTS\",\"score\":100}," \
            "{\"id\":\"ENM006991L0004\",\"name\":\"Information Browsing\",\"type\":\"ELEMENTS\"," \
            "\"score\":99.53539389},{\"id\":\"ENM006991L0003\",\"name\":\"Navigation\",\"type\":\"ELEMENTS\"," \
            "\"score\":100},{\"id\":\"ENM006991L0002\",\"name\":\"Site Performance\",\"type\":\"ELEMENTS\"," \
            "\"score\":99.61908813},{\"id\":\"ENM006991L0001\",\"name\":\"Look and Feel\",\"type\":\"ELEMENTS\"," \
            "\"score\":98.68542663}],\"responses\":[{\"id\":\"CPPAUTOA12079341\",\"name\":\"url\",\"phrase\":\"url\"," \
            "\"type\":\"CPP\",\"label\":\"url\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"https://www.va.gov/health-care/apply\"]},{\"id\":\"CPPAUTOAd20535641\",\"name\":\"window_height\"," \
            "\"phrase\":\"window_height\",\"type\":\"CPP\",\"label\":\"window_height\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"757\"]}]},{\"id\":\"V185Vop4U5hthwFF5cUdRA4D\"," \
            "\"responseTime\":\"2020-01-01T08:52:36.000-05:00\",\"experienceDate\":\"2020-01-01\",\"latentScores\":[{" \
            "\"id\":\"ENM006991L0009\",\"name\":\"Primary Resource\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0008\",\"name\":\"Recommend Site\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0007\",\"name\":\"Return\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0006\",\"name\":\"Satisfaction\",\"type\":\"SATISFACTION\",\"score\":70}," \
            "{\"id\":\"ENM006991L0005\",\"name\":\"Site Information\",\"type\":\"ELEMENTS\",\"score\":100}," \
            "{\"id\":\"ENM006991L0004\",\"name\":\"Information Browsing\",\"type\":\"ELEMENTS\"," \
            "\"score\":99.53539389},{\"id\":\"ENM006991L0003\",\"name\":\"Navigation\",\"type\":\"ELEMENTS\"," \
            "\"score\":100},{\"id\":\"ENM006991L0002\",\"name\":\"Site Performance\",\"type\":\"ELEMENTS\"," \
            "\"score\":99.61908813},{\"id\":\"ENM006991L0001\",\"name\":\"Look and Feel\",\"type\":\"ELEMENTS\"," \
            "\"score\":98.68542663}],\"responses\":[{\"id\":\"CPPAUTOA12079341\",\"name\":\"url\",\"phrase\":\"url\"," \
            "\"type\":\"CPP\",\"label\":\"url\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"https://www.va.gov/burials-and-memorials/application/3118931/status\"]},{\"id\":\"CPPAUTOAd20535641\"," \
            "\"name\":\"window_height\",\"phrase\":\"window_height\",\"type\":\"CPP\",\"label\":\"window_height\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"757\"]}]}]} "
        json_response = json.loads(self.response_str)
        self.score_holder = ScoreHolder()
        for item in json_response['items']:
            self.score_holder.add_measure_item(item)

    def test_can_extract_all_items(self):
        self.assertEqual(2, self.score_holder.measure_size())

    def test_correct_average_satisfaction_score(self):
        self.assertEqual(85.0, self.score_holder.get_satisfaction_score())

    def test_correct_average_satisfaction_score_for_url(self):
        self.assertEqual(70.0, self.score_holder.geturl_satisfaction_score("burials-and-memorials/Application"))


if __name__ == '__main__':
    unittest.main()
