import datetime


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
    start_date = end_date - datetime.timedelta(days=364)
    return start_date.isoformat(), end_date.isoformat()


def find_sunday():
    """Finds the prior Sunday to ensure a full week of data

    returns a datetime representing that Sunday"""

    today = datetime.date.today()

    # Monday is 1 and Sunday is 7 for isoweekday()
    days_after_sunday = datetime.timedelta(days=today.isoweekday())
    return today - days_after_sunday
