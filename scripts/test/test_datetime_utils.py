from scripts.google_analytics.datetime_utils import reformat_date, find_last_day_of_previous_month, \
    find_last_full_twelve_months, find_sunday, find_last_thirty_days, one_year_before
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
        assert end_date == datetime.date(2019, 12, 31)
        assert start_date == datetime.date(2019, 1, 1)

    with freeze_time("2019-11-03"):
        start_date, end_date = find_last_full_twelve_months()
        assert end_date == datetime.date(2019, 10, 31)
        assert start_date == datetime.date(2018, 11, 1)

    with freeze_time("2020-03-19"):
        start_date, end_date = find_last_full_twelve_months()
        assert end_date == datetime.date(2020, 2, 29)
        assert start_date == datetime.date(2019, 3, 1)


def test_one_year_before():
    date = datetime.date(2020, 3, 19)
    assert one_year_before(date) == datetime.date(2019, 3, 19)

    leap_day = datetime.date(2020, 2, 29)
    assert one_year_before(leap_day) == datetime.date(2019, 2, 28)


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


def test_find_last_thirty_days():
    with freeze_time("2019-05-01"):
        start_date, end_date = find_last_thirty_days()
        assert end_date == datetime.date(2019, 4, 30)
        assert start_date == datetime.date(2019, 4, 1)

    with freeze_time("2020-03-19"):
        start_date, end_date = find_last_thirty_days()
        assert end_date == datetime.date(2020, 3, 18)
        assert start_date == datetime.date(2020, 2, 18)
