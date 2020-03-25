import google_analytics.analytics_helpers
from google_analytics.analytics_helpers import make_df, make_table, get_totals_from_report, calculate_trend, \
    sort_tools_by_transactions
import pytest
import pandas as pd


def test_make_df_should_throw_error_if_data_empty():
    with pytest.raises(RuntimeError):
        report = {
            'columnHeader': {
                'dimensions': [],
                'metricHeader': {
                    'metricHeaderEntries': []
                }
            },
            'data': {
                'rows': []
            }
        }

        make_df(report)


def test_make_table():
    dim_labels = ['eventCategory', 'month']
    metric_labels = ['visits']
    rows = [
        {
            'dimensions': ['API Calls', 'Jan'],
            'metrics': [{'values': ['12']}]
        },
        {
            'dimensions': ['API Calls', 'Feb'],
            'metrics': [{'values': ['34']}]
        },
        {
            'dimensions': ['Sign-on', 'Jan'],
            'metrics': [{'values': ['56']}]
        },
        {
            'dimensions': ['Sign-on', 'Feb'],
            'metrics': [{'values': ['78']}]
        }
    ]

    expected_table = [
        {
            'eventCategory': 'API Calls',
            'month': 'Jan',
            'visits': 12
        },
        {
            'eventCategory': 'API Calls',
            'month': 'Feb',
            'visits': 34
        },
        {
            'eventCategory': 'Sign-on',
            'month': 'Jan',
            'visits': 56
        },
        {
            'eventCategory': 'Sign-on',
            'month': 'Feb',
            'visits': 78
        }
    ]

    actual_table = make_table(rows, dim_labels, metric_labels)

    assert expected_table == actual_table


def test_get_totals_from_report_with_one_total():
    report = {
        'data': {
            'totals': [{
                'values': ['1234']
            }]
        }
    }

    assert get_totals_from_report(report) == [1234]


def test_get_totals_from_report_with_two_totals():
    report = {
        'data': {
            'totals': [
                {
                    'values': ['1234']
                },
                {
                    'values': ['5678']
                }
            ]
        }
    }

    assert get_totals_from_report(report) == [1234, 5678]


def test_calculate_trend():
    cases = [
        (50, 100, 100),
        (140, 70, -50),
        (100, 105, 5),
        (60, 45, -25)
    ]
    for (previous, recent, expected_trend) in cases:
        assert calculate_trend(previous, recent) == expected_trend


def test_sort_tools_by_transactions():
    tools = [
        {"title": "some-tool-title-1", "transactions": 100},
        {"title": "some-tool-title-2", "transactions": 300},
        {"title": "some-tool-title-3", "transactions": 200},
    ]
    sort_tools_by_transactions(tools)
    assert tools == [
        {"title": "some-tool-title-2", "transactions": 300},
        {"title": "some-tool-title-3", "transactions": 200},
        {"title": "some-tool-title-1", "transactions": 100},
    ]


def test_add_month_column():
    d = {'totalEvents': [123, 456], 'date': ['3/2019', '4/2019']}
    expected_df = pd.DataFrame(data=d)

    d = {'totalEvents': [123, 456], 'yearMonth': ['201903', '201904']}
    df = pd.DataFrame(data=d)
    actual_df = google_analytics.analytics_helpers.add_month_column(df)

    assert actual_df.equals(expected_df)
