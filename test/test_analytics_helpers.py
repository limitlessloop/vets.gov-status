from scripts.google_analytics.analytics_helpers import make_df
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
