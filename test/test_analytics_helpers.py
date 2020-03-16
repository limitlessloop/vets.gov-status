from scripts.google_analytics.analytics_helpers import make_df, make_table
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
