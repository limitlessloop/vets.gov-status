import datetime
from unittest import mock
from google_analytics import ga_requests


def test_get_logged_in_users_request_should_substitute_dates(monkeypatch):

    mock_find_last_full_twelve_months = mock.Mock()
    mock_find_last_full_twelve_months.return_value = (datetime.date(2018, 12, 25), datetime.date(2019, 12, 25))

    monkeypatch.setattr(ga_requests, "find_last_full_twelve_months", mock_find_last_full_twelve_months)

    request = ga_requests.get_logged_in_users_request()

    assert len(request["dateRanges"]) == 1
    assert request["dateRanges"][0]["startDate"] == "2018-12-25"
    assert request["dateRanges"][0]["endDate"] == "2019-12-25"


def test_get_last_month_users_request_should_substitute_dates_and_path(monkeypatch):

    mock_find_last_thirty_days = mock.Mock()
    mock_find_last_thirty_days.return_value = (datetime.date(2019, 11, 25), datetime.date(2019, 12, 25))

    mock_one_year_before = mock.Mock()
    mock_one_year_before.side_effects = [datetime.date(2018, 11, 25), datetime.date(2018, 12, 25)]

    monkeypatch.setattr(ga_requests, "find_last_thirty_days", mock_find_last_thirty_days)

    request = ga_requests.get_last_month_users_request("www.foo.gov")

    assert len(request["dateRanges"]) == 2
    assert request["dateRanges"][0]["startDate"] == "2019-11-25"
    assert request["dateRanges"][0]["endDate"] == "2019-12-25"
    assert request["dateRanges"][1]["startDate"] == "2018-11-25"
    assert request["dateRanges"][1]["endDate"] == "2018-12-25"

    assert request["dimensionFilterClauses"][0]["filters"][0]["expressions"][0] == "www.foo.gov"


def test_get_all_transactions_request_should_substitute_dates(monkeypatch):

    mock_find_last_full_twelve_months = mock.Mock()
    mock_find_last_full_twelve_months.return_value = (datetime.date(2018, 12, 25), datetime.date(2019, 12, 25))

    monkeypatch.setattr(ga_requests, "find_last_full_twelve_months", mock_find_last_full_twelve_months)

    request = ga_requests.get_all_transactions_request()

    assert len(request["dateRanges"]) == 1
    assert request["dateRanges"][0]["startDate"] == "2018-12-25"
    assert request["dateRanges"][0]["endDate"] == "2019-12-25"


def test_get_transactions_for_tools_request_should_substitute_dates_and_filters(monkeypatch):

    mock_find_last_thirty_days = mock.Mock()
    mock_find_last_thirty_days.return_value = (datetime.date(2019, 11, 25), datetime.date(2019, 12, 25))

    monkeypatch.setattr(ga_requests, "find_last_thirty_days", mock_find_last_thirty_days)

    tool = {
        "event_category_filter": "some-event-filter",
        "page_path_filter": "some-path-filter"
    }

    request = ga_requests.get_transactions_for_tools_request(tool)

    assert len(request["dateRanges"]) == 1
    assert request["dateRanges"][0]["startDate"] == "2019-11-25"
    assert request["dateRanges"][0]["endDate"] == "2019-12-25"

    filters = request["dimensionFilterClauses"][0]["filters"]
    assert any(
        ga_filter["dimensionName"] == "ga:eventCategory" and ga_filter["expressions"][0] == "some-event-filter"
        for ga_filter in filters
    )
    assert any(
        ga_filter["dimensionName"] == "ga:pagePath" and ga_filter["expressions"][0] == "some-path-filter"
        for ga_filter in filters
    )


def test_transactions_for_tools_request_contains_correct_filters():
    tool = {
        'title': 'Some Title',
        'page_path_filter': '/va.gov',
        'event_category_filter': 'Transactions'
    }

    response = ga_requests.get_transactions_for_tools_request(tool)

    filters = response['dimensionFilterClauses'][0]['filters']

    expected_page_path_filter = {
        'dimensionName': 'ga:pagePath',
        'operator': 'REGEXP',
        'expressions': [tool['page_path_filter']]
    }

    expected_event_category_filter = {
        'dimensionName': 'ga:eventCategory',
        'operator': 'REGEXP',
        'expressions': [tool['event_category_filter']]
    }

    assert expected_page_path_filter in filters
    assert expected_event_category_filter in filters
    assert len(filters) == 2


def test_transactions_for_tools_request_contains_event_action_filter():
    tool = {
        'title': 'Some Title',
        'page_path_filter': '/va.gov',
        'event_category_filter': 'Transactions',
        'event_action_filter': 'Forms'
    }

    response = ga_requests.get_transactions_for_tools_request(tool)

    filters = response['dimensionFilterClauses'][0]['filters']

    expected_event_action_filter = {
        'dimensionName': 'ga:eventAction',
        'operator': 'REGEXP',
        'expressions': [tool['event_action_filter']]
    }

    assert expected_event_action_filter in filters
    assert len(filters) == 3
