from scripts.google_analytics.analytics_helpers import format_yearMonth


def test_yearMonth_formatting():
    formatted_date = format_yearMonth("201910")
    assert formatted_date == "10/2019"

    formatted_date = format_yearMonth("202001")
    assert formatted_date == "1/2020"

