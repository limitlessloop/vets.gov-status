from unittest import mock

import pandas as pd

from google_analytics import fetch_ga_data


def test_add_month_column():
    d = {'totalEvents': [123, 456], 'date': ['3/2019', '4/2019']}
    expected_df = pd.DataFrame(data=d)

    d = {'totalEvents': [123, 456], 'yearMonth': ['201903', '201904']}
    df = pd.DataFrame(data=d)
    actual_df = fetch_ga_data.add_month_column(df)

    assert actual_df.equals(expected_df)


def test_fetch_data_for_service(monkeypatch):
    mock_analytics_service = mock.Mock()

    mock_get_request = mock.Mock()
    mock_get_request.return_value = "some-generated-request"

    mock_run_report = mock.Mock()
    mock_run_report.return_value = 100, -5

    monkeypatch.setattr(fetch_ga_data, "get_last_month_users_request", mock_get_request)
    monkeypatch.setattr(fetch_ga_data, "run_report_and_get_total_with_trend", mock_run_report)

    service = {
        "title": "some-title",
        "page_path_filter": "www.foo.com",
        "tools": []
    }

    service_data = fetch_ga_data.fetch_data_for_service(mock_analytics_service, service)

    mock_get_request.assert_called_with("www.foo.com")
    mock_run_report.assert_called_with(mock_analytics_service, "some-generated-request")

    assert service_data["title"] == "some-title"
    assert service_data["users_total"] == 100
    assert service_data["users_trend"] == -5


def test_fetch_data_for_service_fetches_data_for_each_tool(monkeypatch):
    mock_analytics_service = mock.Mock()

    mock_fetch_data_for_tool = mock.Mock()
    # mock return values for multiple calls
    mock_fetch_data_for_tool.side_effect = ["some-tool-data-1", "some-tool-data-2"]

    monkeypatch.setattr(fetch_ga_data, "fetch_data_for_tool", mock_fetch_data_for_tool)

    service = {
        "title": "some-title",
        "tools": [
            {
                "title": "some-tool-title-1"
            },
            {
                "title": "some-tool-title-2"
            }
        ]
    }

    service_data = fetch_ga_data.fetch_data_for_service(mock_analytics_service, service)

    expected_calls = [
        mock.call({"title": "some-tool-title-1"}),
        mock.call({"title": "some-tool-title-2"}),
    ]

    mock_fetch_data_for_tool.assert_has_calls(expected_calls)

    assert service_data["tools"] == ["some-tool-data-1", "some-tool-data-2"]
