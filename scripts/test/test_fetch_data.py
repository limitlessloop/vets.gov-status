from unittest import mock

import fetch_data


def test_fetch_data_for_service(monkeypatch):
    mock_analytics_service = mock.Mock()

    mock_get_request = mock.Mock()
    mock_get_request.return_value = "some-generated-request"

    mock_get_ga_report = mock.Mock()

    mock_get_totals_from_report = mock.Mock()
    mock_get_totals_from_report.return_value = [1234, 5678]

    mock_calculate_trend = mock.Mock()
    mock_calculate_trend.return_value = -5

    mock_fetch_transactions_for_tool = mock.Mock()
    mock_fetch_transactions_for_tool.side_effect = ["some-tool-data-1", "some-tool-data-2"]

    mock_sort_tools_by_transactions = mock.Mock()

    monkeypatch.setattr(fetch_data, "get_last_month_users_request", mock_get_request)
    monkeypatch.setattr(fetch_data, "get_ga_report", mock_get_ga_report)
    monkeypatch.setattr(fetch_data, "get_totals_from_report", mock_get_totals_from_report)
    monkeypatch.setattr(fetch_data, "calculate_trend", mock_calculate_trend)
    monkeypatch.setattr(fetch_data, "fetch_transactions_for_tool", mock_fetch_transactions_for_tool)
    monkeypatch.setattr(fetch_data, "sort_tools_by_transactions", mock_sort_tools_by_transactions)

    service = {
        "title": "some-title",
        "page_path_filter": "www.foo.com",
        "tools": [
            {
                "title": "some-tool-title-1"
            },
            {
                "title": "some-tool-title-2"
            }
        ]
    }

    service_data = fetch_data.fetch_ga_data_for_service(mock_analytics_service, service)

    mock_get_request.assert_called_with("www.foo.com")
    mock_get_ga_report.assert_called_with(mock_analytics_service, "some-generated-request")

    assert service_data["title"] == "some-title"
    assert service_data["users_total"] == 1234
    assert service_data["users_trend"] == -5

    expected_calls = [
        mock.call(mock_analytics_service, {"title": "some-tool-title-1"}),
        mock.call(mock_analytics_service, {"title": "some-tool-title-2"}),
    ]

    mock_fetch_transactions_for_tool.assert_has_calls(expected_calls)
    mock_sort_tools_by_transactions.assert_called_once()

    assert service_data["tools"] == ["some-tool-data-1", "some-tool-data-2"]


def test_fetch_transactions_for_tool(monkeypatch):
    mock_analytics_service = mock.Mock()

    mock_get_ga_report = mock.Mock()
    mock_get_transactions_for_tools_request = mock.Mock()
    mock_get_transactions_for_tools_request.return_value = "some-generated-request"

    mock_get_total_from_report = mock.Mock()
    mock_get_total_from_report.return_value = 1234

    monkeypatch.setattr(fetch_data, "get_ga_report", mock_get_ga_report)
    monkeypatch.setattr(fetch_data, "get_transactions_for_tools_request", mock_get_transactions_for_tools_request)
    monkeypatch.setattr(fetch_data, "get_total_from_report", mock_get_total_from_report)

    tool = {
        "title": "some-tool-title-1"
    }

    tool_data = fetch_data.fetch_transactions_for_tool(mock_analytics_service, tool)

    assert tool_data["title"] == "some-tool-title-1"
    assert tool_data["transactions"] == 1234

    mock_get_ga_report.assert_called_with(mock_analytics_service, "some-generated-request")


def test_add_csat_data_to_counts(monkeypatch):
    mock_update_csat = mock.Mock()
    mock_update_csat.return_value = 88.0

    mock_fetch_foresee_data_for_services = mock.Mock()
    mock_fetch_foresee_data_for_services.return_value = {
        'Some-Service-1': {
            'csat': 75.0,
            'csat_trend': 20.0
        },
        'Some-Service-2': {
            'csat': 40.0,
            'csat_trend': -40.0
        }
    }

    monkeypatch.setattr(fetch_data, "fetch_foresee_data_for_services", mock_fetch_foresee_data_for_services)
    monkeypatch.setattr(fetch_data, "update_csat", mock_update_csat)

    counts = {
        "services": [
            {
                "title": "Some-Service-1",
                "users_total": 1000,
                "users_trend": 10
            },
            {
                "title": "Some-Service-2"
            }
        ]
    }

    services = [
        {'title': 'Some-Service-1', 'page_path_filter': 'some-url-1'},
        {'title': 'Some-Service-2', 'page_path_filter': 'some-url-2'}
    ]

    fetch_data.add_csat_data_to_counts(counts, services)

    assert counts["services"][0]["csat"] == 75.0
    assert counts["services"][0]["csat_trend"] == 20.0

    assert counts["services"][1]["csat"] == 40.0
    assert counts["services"][1]["csat_trend"] == -40.0

    assert counts["csat_total"] == '88.0%'
