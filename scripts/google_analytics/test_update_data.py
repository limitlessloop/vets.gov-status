import update_data
from freezegun import freeze_time
import datetime


def test_find_sunday():
    # Wednesday after New Year
    with freeze_time("2020-01-01"):
        sun = update_data.find_sunday()
        assert sun == datetime.date(2019, 12, 29)

    # Sat Feb 29
    with freeze_time("2020-02-29"):
        sun = update_data.find_sunday()
        assert sun == datetime.date(2020, 2, 23)

    # Sunday in November
    with freeze_time("2019-11-03"):
        sun = update_data.find_sunday()
        assert sun == datetime.date(2019, 10, 27)
