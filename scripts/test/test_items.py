import unittest
import json
from scripts.foresee.items import MeasureItem


class MeasureItemTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.one_item_str = \
            "{\"id\":\"V185Vop4U5hthwFF5cUdRA4C\",\"responseTime\":\"2020-01-01T07:52:36.000-05:00\"," \
            "\"experienceDate\":\"2020-01-01\",\"latentScores\":[{\"id\":\"ENM006991L0009\",\"name\":\"Primary " \
            "Resource\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100},{\"id\":\"ENM006991L0008\",\"name\":\"Recommend " \
            "Site\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100},{\"id\":\"ENM006991L0007\",\"name\":\"Return\"," \
            "\"type\":\"FUTURE_BEHAVIOR\",\"score\":100},{\"id\":\"ENM006991L0006\",\"name\":\"Satisfaction\"," \
            "\"type\":\"SATISFACTION\",\"score\":100},{\"id\":\"ENM006991L0005\",\"name\":\"Site Information\"," \
            "\"type\":\"ELEMENTS\",\"score\":100},{\"id\":\"ENM006991L0004\",\"name\":\"Information Browsing\"," \
            "\"type\":\"ELEMENTS\",\"score\":99.53539389},{\"id\":\"ENM006991L0003\",\"name\":\"Navigation\"," \
            "\"type\":\"ELEMENTS\",\"score\":100},{\"id\":\"ENM006991L0002\",\"name\":\"Site Performance\"," \
            "\"type\":\"ELEMENTS\",\"score\":99.61908813},{\"id\":\"ENM006991L0001\",\"name\":\"Look and Feel\"," \
            "\"type\":\"ELEMENTS\",\"score\":98.68542663}],\"responses\":[{\"id\":\"CPPAUTOA12079341\"," \
            "\"name\":\"url\",\"phrase\":\"url\",\"type\":\"CPP\",\"label\":\"url\",\"responseType\":\"TEXT_AREA\"," \
            "\"answers\":[\"https://www.va.gov/track-claims/appeals/3118931/status\"]},{\"id\":\"CPPAUTOAd20535641\"," \
            "\"name\":\"window_height\",\"phrase\":\"window_height\",\"type\":\"CPP\",\"label\":\"window_height\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"757\"]}]} "
        self.measure_item = MeasureItem(json.loads(self.one_item_str))

    def test_can_extract_satisfaction_score(self):
        self.assertEqual(100.0, self.measure_item.get_satisfaction_score())

    def test_can_extract_url_cpp(self):
        expected_url_answers = ["https://www.va.gov/track-claims/appeals/3118931/status"]
        self.assertListEqual(expected_url_answers, self.measure_item.get_url_answers())

    def test_can_search_url_lowercase(self):
        self.assertEqual(True, self.measure_item.does_url_contain_pattern("track-claims/appeals"))

    def test_can_search_url_mix_case(self):
        self.assertEqual(True, self.measure_item.does_url_contain_pattern("track-cLaims/Appeals"))

    def test_can_search_url_using_regex(self):
        self.assertEqual(False, self.measure_item.does_url_contain_pattern("track-claims\.appeals"))


if __name__ == '__main__':
    unittest.main()
