import datetime
from dateutil.relativedelta import relativedelta


def reformat_date(year_month):
    year = year_month[:4]
    month = year_month[-2:]
    if month[0] == '0':
        month = month[1]
    formatted_date = month + '/' + year
    return formatted_date


def find_last_day_of_previous_month(date):
    first = date.replace(day=1)
    return first - datetime.timedelta(days=1)


def find_last_full_twelve_months():
    end_date = find_last_day_of_previous_month(datetime.date.today())

    # relativedelta supports leap year calculation
    start_date = end_date - relativedelta(months=12) + relativedelta(days=1)
    return start_date, end_date


def one_year_before(date):
    if date.month == 2 and date.day == 29:
        return date.replace(year=date.year-1, day=28)
    return date.replace(year=date.year-1)


def find_last_thirty_days():
    today = datetime.date.today()
    end_date = today - datetime.timedelta(days=1)
    start_date = end_date - datetime.timedelta(days=29)
    return start_date, end_date


def find_sunday():
    """Finds the prior Sunday to ensure a full week of data

    returns a datetime representing that Sunday"""

    today = datetime.date.today()

    # Monday is 1 and Sunday is 7 for isoweekday()
    days_after_sunday = datetime.timedelta(days=today.isoweekday())
    return today - days_after_sunday


def find_last_twelve_months():
    current_date = datetime.datetime.now().date()
    previous_twelve_months = [
        find_last_day_of_previous_month(current_date - relativedelta(months=m)) for m in range(0, 12)
    ]
    month_time_ranges = [(last_day_of_month.replace(day=1), last_day_of_month)
                         for last_day_of_month in previous_twelve_months]
    month_time_ranges.reverse()
    return month_time_ranges
