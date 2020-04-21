import json
from unittest import mock
import pytest
import pandas as pd
import foresee.foresee as foresee
import foresee.foresee_helpers as foresee_helpers

response_str: str = \
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


def test_calculates_average_satisfaction_score():
    json_response = json.loads(response_str)
    assert 85.0 == foresee.calculate_average_satisfaction(json_response['items'])


def test_calculate_average_satisfaction_of_all_data():
    one_set_of_data = json.loads(response_str)
    multiple_data_items = [
        {foresee.MONTH_DATA: one_set_of_data['items']},
        {foresee.MONTH_DATA: one_set_of_data['items']},
        {foresee.MONTH_DATA: one_set_of_data['items']}
    ]
    assert 85.0 == foresee.calculate_overall_average_satisfaction(multiple_data_items)


def test_fetch_foresee_data_for_services(monkeypatch):
    recent_data = [
        {'Satisfaction': 80.0, 'url': 'some-url-1'},
        {'Satisfaction': 70.0, 'url': 'some-url-1'},
        {'Satisfaction': 40.0, 'url': 'some-url-2'},
    ]
    recent_df = pd.DataFrame(recent_data)

    last_year_data = [
        {'Satisfaction': 60.0, 'url': 'some-url-1'},
        {'Satisfaction': 50.0, 'url': 'some-url-1'},
        {'Satisfaction': 80.0, 'url': 'some-url-2'},
    ]
    last_year_df = pd.DataFrame(last_year_data)

    mock_get_foresee_items_for_services = mock.Mock()
    mock_get_foresee_items_for_services.return_value = (recent_df, last_year_df)

    mock_get_average_score = mock.Mock()
    mock_get_average_score.side_effect = [75.0, 55.0, 40.0, 80.0]

    mock_calculate_trend = mock.Mock()
    mock_calculate_trend.side_effect = [10.0, -10.0]

    monkeypatch.setattr(foresee, "get_foresee_items_for_services", mock_get_foresee_items_for_services)
    monkeypatch.setattr(foresee_helpers, "get_average_score", mock_get_average_score)
    monkeypatch.setattr(foresee, "calculate_trend", mock_calculate_trend)

    services = [
        {'title': 'Some-Service-1', 'page_path_filter': 'some-url-1'},
        {'title': 'Some-Service-2', 'page_path_filter': 'some-url-2'}
    ]

    expected_result = {
        'Some-Service-1': {
            'csat': 75.0,
            'csat_trend': 10.0
        },
        'Some-Service-2': {
            'csat': 40.0,
            'csat_trend': -10.0
        }
    }

    assert expected_result == foresee.fetch_foresee_data_for_services(services)


def test_send_one_request_fail_all_attempts(monkeypatch):
    mock_response = mock.Mock()
    mock_response.status_code = 401
    mock_response.text = "for testing"

    mock_request = mock.Mock()
    mock_request.return_value = mock_response

    mock_authenticate = mock.Mock()
    mock_authenticate.return_value = "anything"

    monkeypatch.setattr("requests.request", mock_request)
    monkeypatch.setattr(foresee, "authenticate", mock_authenticate)
    with pytest.raises(RuntimeError) as ex:
        foresee.send_one_request({'h1': 'h1'}, 'query', 'url')

    assert str(ex.value) == "401 for testing"


def test_send_one_request_success_after_one_attempt(monkeypatch):
    mock_authenticate = mock.Mock()
    mock_authenticate.return_value = "anything"
    counter_dict = {"counter": 0}

    def mock_request_attr(method, url, **kwargs):
        counter_dict["counter"] += 1
        mock_response = mock.Mock()
        mock_response.status_code = 401 if counter_dict["counter"] == 1 else 200
        mock_response.text = "for testing"
        return mock_response

    monkeypatch.setattr("requests.request", mock_request_attr)
    monkeypatch.setattr(foresee, "authenticate", mock_authenticate)

    response = foresee.send_one_request({'h1': 'h1'}, 'query', 'url')

    assert response.status_code == 200


def test_authenticate_failure(monkeypatch):
    mock_response = mock.Mock()
    mock_response.status_code = 401

    mock_request = mock.Mock()
    mock_request.return_value = mock_response

    monkeypatch.setattr("requests.request", mock_request)
    monkeypatch.setenv("FORESEE_CREDENTIALS", "dummy credentials")

    with pytest.raises(PermissionError):
        foresee.authenticate()


def test_authenticate_success(monkeypatch):
    mock_response = mock.Mock()
    mock_response.status_code = 200

    mock_request = mock.Mock()
    mock_request.return_value = mock_response

    monkeypatch.setattr(mock_response, 'json', lambda: {'access_token': 'dummy token'})
    monkeypatch.setattr('requests.request', mock_request)
    monkeypatch.setenv('FORESEE_CREDENTIALS', 'dummy credentials')

    token = foresee.authenticate()

    assert token == 'dummy token'


def test_get_measure_data(monkeypatch):
    mock_send_one_request_response = mock.Mock()

    mock_send_one_request = mock.Mock()
    mock_send_one_request.return_value = mock_send_one_request_response

    monkeypatch.setattr(mock_send_one_request_response, 'json', lambda: {'hasMore': False, 'items': []})
    monkeypatch.setattr(foresee, "send_one_request", mock_send_one_request)

    actual_return_items = foresee.get_measure_data('None', 'None', 'None')

    assert actual_return_items == []
