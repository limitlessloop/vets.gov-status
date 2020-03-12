from scripts.google_analytics.analytics_helpers import format_yearMonth, make_df
import pytest


def test_yearMonth_formatting():
    formatted_date = format_yearMonth("201910")
    assert formatted_date == "10/2019"

    formatted_date = format_yearMonth("202001")
    assert formatted_date == "1/2020"


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
