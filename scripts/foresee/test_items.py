import unittest
import json
from scripts.foresee.items import MeasureItem


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.one_item_str = \
            "{\"id\":\"V185Vop4U5hthwFF5cUdRA4C\",\"responseTime\":\"2020-01-01T07:52:36.000-05:00\"," \
            "\"experienceDate\":\"2020-01-01\",\"latentScores\":[{\"id\":\"ENM006991L0009\"," \
            "\"name\":\"Primary Resource\",\"type\":\"FUTURE_BEHAVIOR\",\"score\":100}," \
            "{\"id\":\"ENM006991L0008\",\"name\":\"Recommend Site\",\"type\":\"FUTURE_BEHAVIOR\"," \
            "\"score\":100},{\"id\":\"ENM006991L0007\",\"name\":\"Return\",\"type\":\"FUTURE_BEHAVIOR\"," \
            "\"score\":100},{\"id\":\"ENM006991L0006\",\"name\":\"Satisfaction\"," \
            "\"type\":\"SATISFACTION\",\"score\":100},{\"id\":\"ENM006991L0005\",\"name\":\"Site " \
            "Information\",\"type\":\"ELEMENTS\",\"score\":100},{\"id\":\"ENM006991L0004\"," \
            "\"name\":\"Information Browsing\",\"type\":\"ELEMENTS\",\"score\":99.53539389}," \
            "{\"id\":\"ENM006991L0003\",\"name\":\"Navigation\",\"type\":\"ELEMENTS\",\"score\":100}," \
            "{\"id\":\"ENM006991L0002\",\"name\":\"Site Performance\",\"type\":\"ELEMENTS\"," \
            "\"score\":99.61908813},{\"id\":\"ENM006991L0001\",\"name\":\"Look and Feel\"," \
            "\"type\":\"ELEMENTS\",\"score\":98.68542663}],\"responses\":[{\"id\":\"ENM006991Q00210\"," \
            "\"name\":\"How likely are you to use this site as your primary resource for obtaining " \
            "information about Veterans Affairs?\",\"phrase\":\"How likely are you to use this site as " \
            "your primary resource for obtaining information about Veterans Affairs?\",\"type\":\"MQ\"," \
            "\"label\":\"Primary Resource\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]}," \
            "{\"id\":\"ENM006991Q00010\",\"name\":\"Please rate the visual appeal of this site.\"," \
            "\"phrase\":\"Please rate the visual appeal of this site.\",\"type\":\"MQ\",\"label\":\"Look " \
            "and Feel - Appeal\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]}," \
            "{\"id\":\"ENM006991Q00030\",\"name\":\"Please rate the readability of the pages on this site. " \
            "\",\"phrase\":\"Please rate the readability of the pages on this site. \",\"type\":\"MQ\"," \
            "\"label\":\"Look and Feel - Readability\",\"responseType\":\"MEASURED_QUESTION\"," \
            "\"answers\":[\"10\"]},{\"id\":\"CPPAUTOAd14367241\",\"name\":\"GA_UID\"," \
            "\"phrase\":\"GA_UID\",\"type\":\"CPP\",\"label\":\"GA_UID\",\"responseType\":\"TEXT_AREA\"," \
            "\"answers\":[\"1656533593.1576678971\"]},{\"id\":\"CPPAUTOA12083541\"," \
            "\"name\":\"GovDelivery\",\"phrase\":\"GovDelivery\",\"type\":\"CPP\"," \
            "\"label\":\"GovDelivery\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"N\"]}," \
            "{\"id\":\"CPPAUTOAd13415941\",\"name\":\"OI&T\",\"phrase\":\"OI&T\",\"type\":\"CPP\"," \
            "\"label\":\"OI&T\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]}," \
            "{\"id\":\"CPPAUTOA12078241\",\"name\":\"Section_Compensation\"," \
            "\"phrase\":\"Section_Compensation\",\"type\":\"CPP\",\"label\":\"Section_Compensation\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]},{\"id\":\"CPPAUTOA12085441\"," \
            "\"name\":\"Section_Education\",\"phrase\":\"Section_Education\",\"type\":\"CPP\"," \
            "\"label\":\"Section_Education\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]}," \
            "{\"id\":\"CPPAUTOA12081241\",\"name\":\"Section_HomeLoans\",\"phrase\":\"Section_HomeLoans\"," \
            "\"type\":\"CPP\",\"label\":\"Section_HomeLoans\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"no\"]},{\"id\":\"CPPAUTOA12085041\",\"name\":\"Section_LifeIns\"," \
            "\"phrase\":\"Section_LifeIns\",\"type\":\"CPP\",\"label\":\"Section_LifeIns\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]},{\"id\":\"CPPAUTOA12079041\"," \
            "\"name\":\"Section_Pension\",\"phrase\":\"Section_Pension\",\"type\":\"CPP\"," \
            "\"label\":\"Section_Pension\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]}," \
            "{\"id\":\"CPPAUTOA12074341\",\"name\":\"Section_SpecialGrp\"," \
            "\"phrase\":\"Section_SpecialGrp\",\"type\":\"CPP\",\"label\":\"Section_SpecialGrp\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]},{\"id\":\"CPPAUTOA12088841\"," \
            "\"name\":\"Section_VocRehab\",\"phrase\":\"Section_VocRehab\",\"type\":\"CPP\"," \
            "\"label\":\"Section_VocRehab\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"no\"]}," \
            "{\"id\":\"CPPAUTOAd18395841\",\"name\":\"TriggerMethod\",\"phrase\":\"TriggerMethod\"," \
            "\"type\":\"CPP\",\"label\":\"TriggerMethod\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"Traditional\"]},{\"id\":\"CPPAUTOA12469941\",\"name\":\"brand_name\"," \
            "\"phrase\":\"brand_name\",\"type\":\"CPP\",\"label\":\"brand_name\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"Google\"]},{\"id\":\"CPPAUTOA12088041\"," \
            "\"name\":\"browser\",\"phrase\":\"browser\",\"type\":\"CPP\",\"label\":\"browser\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"Chrome 79\"]},{\"id\":\"CPPAUTOA12083941\"," \
            "\"name\":\"browser_name\",\"phrase\":\"browser_name\",\"type\":\"CPP\"," \
            "\"label\":\"browser_name\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"Chrome\"]}," \
            "{\"id\":\"CPPAUTOA12081141\",\"name\":\"browser_version\",\"phrase\":\"browser_version\"," \
            "\"type\":\"CPP\",\"label\":\"browser_version\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"79\"]},{\"id\":\"CPPAUTOAd13414341\",\"name\":\"code\",\"phrase\":\"code\"," \
            "\"type\":\"CPP\",\"label\":\"code\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"19.11.1\"]},{\"id\":\"CPPAUTOAd20534941\",\"name\":\"device_height\"," \
            "\"phrase\":\"device_height\",\"type\":\"CPP\",\"label\":\"device_height\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"900\"]},{\"id\":\"CPPAUTOAd17159541\"," \
            "\"name\":\"device_type\",\"phrase\":\"device_type\",\"type\":\"CPP\"," \
            "\"label\":\"device_type\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"Desktop\"]}," \
            "{\"id\":\"CPPAUTOAd17158941\",\"name\":\"device_version\",\"phrase\":\"device_version\"," \
            "\"type\":\"CPP\",\"label\":\"device_version\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"Google Chrome\"]},{\"id\":\"CPPAUTOAd20535341\",\"name\":\"device_width\"," \
            "\"phrase\":\"device_width\",\"type\":\"CPP\",\"label\":\"device_width\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"1600\"]},{\"id\":\"CPPAUTOAd13415841\"," \
            "\"name\":\"dn\",\"phrase\":\"dn\",\"type\":\"CPP\",\"label\":\"dn\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"default\"]},{\"id\":\"CPPAUTOAd20535541\"," \
            "\"name\":\"dpr\",\"phrase\":\"dpr\",\"type\":\"CPP\",\"label\":\"dpr\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"1\"]},{\"id\":\"CPPAUTOAd18395941\"," \
            "\"name\":\"dt\",\"phrase\":\"dt\",\"type\":\"CPP\",\"label\":\"dt\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"classicdesktop\"]}," \
            "{\"id\":\"CPPAUTOA12469141\",\"name\":\"dual_orientation\",\"phrase\":\"dual_orientation\"," \
            "\"type\":\"CPP\",\"label\":\"dual_orientation\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"false\"]},{\"id\":\"CPPAUTOAd16827241\",\"name\":\"env\",\"phrase\":\"env\"," \
            "\"type\":\"CPP\",\"label\":\"env\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"prd\"]}," \
            "{\"id\":\"CPPAUTOAd15897941\",\"name\":\"fs_renderer\",\"phrase\":\"fs_renderer\"," \
            "\"type\":\"CPP\",\"label\":\"fs_renderer\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"legacy\"]},{\"id\":\"CPPAUTOAd20534741\",\"name\":\"invite_presented_interval\"," \
            "\"phrase\":\"invite_presented_interval\",\"type\":\"CPP\"," \
            "\"label\":\"invite_presented_interval\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"60.527\"]},{\"id\":\"CPPAUTOA12474941\",\"name\":\"is_tablet\",\"phrase\":\"is_tablet\"," \
            "\"type\":\"CPP\",\"label\":\"is_tablet\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"false\"]},{\"id\":\"CPPAUTOA12080241\",\"name\":\"locale\",\"phrase\":\"locale\"," \
            "\"type\":\"CPP\",\"label\":\"locale\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"en\"]}," \
            "{\"id\":\"CPPAUTOA12468541\",\"name\":\"model_name\",\"phrase\":\"model_name\"," \
            "\"type\":\"CPP\",\"label\":\"model_name\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"Google Chrome\"]},{\"id\":\"CPPAUTOA12088141\",\"name\":\"os\",\"phrase\":\"os\"," \
            "\"type\":\"CPP\",\"label\":\"os\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"Windows " \
            "10\"]},{\"id\":\"CPPAUTOA12474241\",\"name\":\"os_name\",\"phrase\":\"os_name\"," \
            "\"type\":\"CPP\",\"label\":\"os_name\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"Windows\"]},{\"id\":\"CPPAUTOA12474041\",\"name\":\"os_version\",\"phrase\":\"os_version\"," \
            "\"type\":\"CPP\",\"label\":\"os_version\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"10\"]},{\"id\":\"CPPAUTOA12473241\",\"name\":\"pointing_method\"," \
            "\"phrase\":\"pointing_method\",\"type\":\"CPP\",\"label\":\"pointing_method\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"mouse\"]},{\"id\":\"CPPAUTOAd18293641\"," \
            "\"name\":\"product_type\",\"phrase\":\"product_type\",\"type\":\"CPP\"," \
            "\"label\":\"product_type\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"web sdk\"]}," \
            "{\"id\":\"CPPAUTOA12077141\",\"name\":\"pv\",\"phrase\":\"pv\",\"type\":\"CPP\"," \
            "\"label\":\"pv\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"5\"]}," \
            "{\"id\":\"CPPAUTOA12088341\",\"name\":\"sid\",\"phrase\":\"sid\",\"type\":\"CPP\"," \
            "\"label\":\"sid\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"browse-va_main-en\"]}," \
            "{\"id\":\"CPPAUTOA12081841\",\"name\":\"site\",\"phrase\":\"site\",\"type\":\"CPP\"," \
            "\"label\":\"site\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"va.gov\"]}," \
            "{\"id\":\"CPPAUTOAd15034541\",\"name\":\"sitekey\",\"phrase\":\"sitekey\",\"type\":\"CPP\"," \
            "\"label\":\"sitekey\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"va-gov\"]}," \
            "{\"id\":\"CPPAUTOA12081341\",\"name\":\"survey_presentation\"," \
            "\"phrase\":\"survey_presentation\",\"type\":\"CPP\",\"label\":\"survey_presentation\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"desktop\"]},{\"id\":\"CPPAUTOAd18293741\"," \
            "\"name\":\"tz\",\"phrase\":\"tz\",\"type\":\"CPP\",\"label\":\"tz\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[\"-360\"]},{\"id\":\"CPPAUTOA12079341\"," \
            "\"name\":\"url\",\"phrase\":\"url\",\"type\":\"CPP\",\"label\":\"url\"," \
            "\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"https://www.va.gov/track-claims/appeals/3118931/status\"]},{\"id\":\"CPPAUTOAd20535641\"," \
            "\"name\":\"window_height\",\"phrase\":\"window_height\",\"type\":\"CPP\"," \
            "\"label\":\"window_height\",\"responseType\":\"TEXT_AREA\",\"answers\":[\"757\"]}," \
            "{\"id\":\"CPPAUTOAd20534841\",\"name\":\"window_width\",\"phrase\":\"window_width\"," \
            "\"type\":\"CPP\",\"label\":\"window_width\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"1600\"]},{\"id\":\"CPPAUTOA12075741\",\"name\":\"wurfl_id\",\"phrase\":\"wurfl_id\"," \
            "\"type\":\"CPP\",\"label\":\"wurfl_id\",\"responseType\":\"TEXT_AREA\",\"answers\":[" \
            "\"google_chrome_79\"]},{\"id\":\"ENM006991Q00090\",\"name\":\"Please rate how well the site " \
            "layout helps you find what you need.\",\"phrase\":\"Please rate how well the site layout " \
            "helps you find what you need.\",\"type\":\"MQ\",\"label\":\"Navigation - Layout\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00070\"," \
            "\"name\":\"Please rate how well the site is organized.\",\"phrase\":\"Please rate how well " \
            "the site is organized.\",\"type\":\"MQ\",\"label\":\"Navigation - Organized\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00060\"," \
            "\"name\":\"Please rate how completely the page content loads on this site.\"," \
            "\"phrase\":\"Please rate how completely the page content loads on this site.\"," \
            "\"type\":\"MQ\",\"label\":\"Site Performance - Completeness\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00040\"," \
            "\"name\":\"Please rate how quickly pages load on this site.\",\"phrase\":\"Please rate how " \
            "quickly pages load on this site.\",\"type\":\"MQ\",\"label\":\"Site Performance - Loading\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00120\"," \
            "\"name\":\"Please rate how well the features on the site help you find the information you " \
            "need.\",\"phrase\":\"Please rate how well the features on the site help you find the " \
            "information you need.\",\"type\":\"MQ\",\"label\":\"Information Browsing - Features\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00100\"," \
            "\"name\":\"Please rate the ability to sort information by criteria that are important to you " \
            "on this site.\",\"phrase\":\"Please rate the ability to sort information by criteria that are " \
            "important to you on this site.\",\"type\":\"MQ\",\"label\":\"Information Browsing - Sort\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00170\"," \
            "\"name\":\"How well does this site meet your expectations?\",\"phrase\":\"How well does this " \
            "site meet your expectations?\",\"type\":\"MQ\",\"label\":\"Satisfaction - Expectations\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00180\"," \
            "\"name\":\"How does this site compare to your idea of an ideal website?\",\"phrase\":\"How " \
            "does this site compare to your idea of an ideal website?\",\"type\":\"MQ\"," \
            "\"label\":\"Satisfaction - Ideal\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[" \
            "\"10\"]},{\"id\":\"ENM006991Q00160\",\"name\":\"What is your overall satisfaction with this " \
            "site?\",\"phrase\":\"What is your overall satisfaction with this site?\",\"type\":\"MQ\"," \
            "\"label\":\"Satisfaction - Overall\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[" \
            "\"10\"]},{\"id\":\"ENM006991Q00150\",\"name\":\"Please rate how well the site’s information " \
            "provides answers to your questions.\",\"phrase\":\"Please rate how well the site’s " \
            "information provides answers to your questions.\",\"type\":\"MQ\",\"label\":\"Site " \
            "Information - Answers\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]}," \
            "{\"id\":\"ENM006991Q00130\",\"name\":\"Please rate the thoroughness of information provided " \
            "on this site.\",\"phrase\":\"Please rate the thoroughness of information provided on this " \
            "site.\",\"type\":\"MQ\",\"label\":\"Site Information - Thoroughness\"," \
            "\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]},{\"id\":\"ENM006991Q00200\"," \
            "\"name\":\"How likely are you to recommend this site to someone else?\",\"phrase\":\"How " \
            "likely are you to recommend this site to someone else?\",\"type\":\"MQ\"," \
            "\"label\":\"Recommend Site\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[\"10\"]}," \
            "{\"id\":\"HAJ6991Q021\",\"name\":\"Please select your age range.\",\"phrase\":\"Please select " \
            "your age range.\",\"type\":\"CQ\",\"label\":\"Age\"," \
            "\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"6\"]}," \
            "{\"id\":\"HAJ6991Q002\",\"name\":\"Which of the following describe you? Please select all " \
            "that apply.\",\"phrase\":\"Which of the following describe you? Please select all that " \
            "apply.\",\"type\":\"CQ\",\"label\":\"Best describes you\"," \
            "\"responseType\":\"CHECKBOX_ONE_UP_VERTICAL\",\"answers\":[\"1\"]},{\"id\":\"HAJ6991Q005\"," \
            "\"name\":\"Did you serve in a combat role during your period of service?\",\"phrase\":\"Did " \
            "you serve in a combat role during your period of service?\",\"type\":\"CQ\"," \
            "\"label\":\"CombatService\",\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[" \
            "\"2\"]},{\"id\":\"LAB6991Q028\",\"name\":\"What Disability and Compensation information or " \
            "services were you looking for today?\",\"phrase\":\"What Disability and Compensation " \
            "information or services were you looking for today?\",\"type\":\"CQ\",\"label\":\"Disability " \
            "Info\",\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"2\"]}," \
            "{\"id\":\"HAJ6991Q022\",\"name\":\"Please select your gender.\",\"phrase\":\"Please select " \
            "your gender.\",\"type\":\"CQ\",\"label\":\"Gender\"," \
            "\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"2\"]}," \
            "{\"id\":\"LAB6991Q024\",\"name\":\"Which category best describes the kind of information or " \
            "services you were primarily looking for today?\",\"phrase\":\"Which category best describes " \
            "the kind of information or services you were primarily looking for today?\",\"type\":\"CQ\"," \
            "\"label\":\"Kind of Information\",\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\"," \
            "\"answers\":[\"2\"]},{\"id\":\"HOP0276933\",\"name\":\"During your visit today, " \
            "did you notice the redesign of the va.gov site?\",\"phrase\":\"During your visit today, " \
            "did you notice the redesign of the va.gov site?\",\"type\":\"CQ\",\"label\":\"New Site Notice " \
            "Redesign\",\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"2\"]}," \
            "{\"id\":\"HAJ6991Q010\",\"name\":\"Where do you live?\",\"phrase\":\"Where do you live?\"," \
            "\"type\":\"CQ\",\"label\":\"Reside\",\"responseType\":\"SELECT_ONE_DROPDOWN\",\"answers\":[" \
            "\"21\"]},{\"id\":\"HAJ6991Q013\",\"name\":\"Did you find what you were looking for today?\"," \
            "\"phrase\":\"Did you find what you were looking for today?\",\"type\":\"CQ\",\"label\":\"Task " \
            "Accomplishment\",\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"1\"]}," \
            "{\"id\":\"LAB6991Q023\",\"name\":\"Did you visit any other Department of Veterans Affairs " \
            "websites today? (Please select all that apply.)\",\"phrase\":\"Did you visit any other " \
            "Department of Veterans Affairs websites today? (Please select all that apply.)\"," \
            "\"type\":\"CQ\",\"label\":\"VA Websites\",\"responseType\":\"CHECKBOX_ONE_UP_VERTICAL\"," \
            "\"answers\":[\"8900\"]},{\"id\":\"HAJ6991Q004\",\"name\":\"Please check the conflict(s) in " \
            "which you served.\",\"phrase\":\"Please check the conflict(s) in which you served.\"," \
            "\"type\":\"CQ\",\"label\":\"Veteran Era\",\"responseType\":\"CHECKBOX_ONE_UP_VERTICAL\"," \
            "\"answers\":[\"8900\"]},{\"id\":\"HAJ6991Q001\",\"name\":\"How often do you visit the " \
            "Veterans Affairs website (www.va.gov)?\",\"phrase\":\"How often do you visit the Veterans " \
            "Affairs website (www.va.gov)?\",\"type\":\"CQ\",\"label\":\"Visit Frequency\"," \
            "\"responseType\":\"RADIO_BUTTON_ONE_UP_VERTICAL\",\"answers\":[\"4\"]}," \
            "{\"id\":\"ENM006991Q00190\",\"name\":\"How likely are you to return to this site in the next " \
            "90 days?\",\"phrase\":\"How likely are you to return to this site in the next 90 days?\"," \
            "\"type\":\"MQ\",\"label\":\"Return\",\"responseType\":\"MEASURED_QUESTION\",\"answers\":[" \
            "\"10\"]}]} "

    def test_can_extract_satisfaction_score(self):
        measure_item = MeasureItem(json.loads(self.one_item_str))
        self.assertEqual(100.0, measure_item.get_satisfaction_score())

    def test_can_extract_url_cpp(self):
        measure_item = MeasureItem(json.loads(self.one_item_str))
        expected_url_answers = ["https://www.va.gov/track-claims/appeals/3118931/status"]
        self.assertListEqual(expected_url_answers, measure_item.get_url_answers())


if __name__ == '__main__':
    unittest.main()
