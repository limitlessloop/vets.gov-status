from google_analytics.analytics_helpers import make_df, make_table, get_totals_from_report, calculate_trend
import pytest


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
