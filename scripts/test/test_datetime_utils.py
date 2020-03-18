from scripts.google_analytics.datetime_utils import reformat_date, find_last_day_of_previous_month, \
    find_last_full_twelve_months, find_sunday
import datetime
from freezegun import freeze_time


def test_yearMonth_formatting():
    formatted_date = reformat_date("201910")
    assert formatted_date == "10/2019"

    formatted_date = reformat_date("202001")
    assert formatted_date == "1/2020"


def test_find_last_day_of_previous_month():
    day = find_last_day_of_previous_month(datetime.date(2020, 3, 12))
    assert day == datetime.date(2020, 2, 29)


def test_find_last_full_twelve_months():
    with freeze_time("2020-01-01"):
        start_date, end_date = find_last_full_twelve_months()
        assert end_date == datetime.date(2019, 12, 31).isoformat()
        assert start_date == datetime.date(2019, 1, 1).isoformat()

    with freeze_time("2019-11-03"):
        start_date, end_date = find_last_full_twelve_months()
        assert end_date == datetime.date(2019, 10, 31).isoformat()
        assert start_date == datetime.date(2018, 11, 1).isoformat()


def test_find_sunday():
    # Wednesday after New Year
    with freeze_time("2020-01-01"):
        sun = find_sunday()
        assert sun == datetime.date(2019, 12, 29)

    # Sat Feb 29
    with freeze_time("2020-02-29"):
        sun = find_sunday()
        assert sun == datetime.date(2020, 2, 23)

    # Sunday in November
    with freeze_time("2019-11-03"):
        sun = find_sunday()
        assert sun == datetime.date(2019, 10, 27)
