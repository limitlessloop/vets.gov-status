from google_analytics.analytics_helpers import make_df, make_table, get_totals_from_report, calculate_trend
from google_analytics.fetch_ga_data import add_month_column
import pytest
import pandas as pd
import pprint

def test_add_month_column():
    d = {'totalEvents': [123, 456], 'date': ['3/2019', '4/2019']}
    expected_df = pd.DataFrame(data=d)

    d = {'totalEvents': [123, 456], 'yearMonth': ['201903', '201904']}
    df = pd.DataFrame(data=d)
    actual_df = add_month_column(df)

    assert actual_df.equals(expected_df)
