from google_analytics.datetime_utils import find_last_thirty_days, one_year_before, find_last_full_twelve_months

VADOTGOV_VIEW_ID = '176188361'


def get_logged_in_users_request():
    start_date, end_date = find_last_full_twelve_months()

    return {
        'viewId': VADOTGOV_VIEW_ID,
        'dateRanges': [{'startDate': start_date.isoformat(),
                        'endDate': end_date.isoformat()}],
        'metrics': [{'expression': 'ga:users'}],
        'segments': [{'segmentId': 'sessions::condition::ga:dimension22=@1,ga:dimension22=@3'}],
        'dimensions': [
            {'name': 'ga:yearMonth'},
            {'name': 'ga:segment'}
        ],
        'dimensionFilterClauses': [
            {
                'filters': [
                    {
                        'dimensionName': 'ga:pagePath',
                        'operator': 'REGEXP',
                        'expressions': ['www.va.gov/']
                    }
                ]
            }
        ]
    }


def get_last_month_users_request(page_path):
    start_date, end_date = find_last_thirty_days()

    return {
        "viewId": VADOTGOV_VIEW_ID,
        "dateRanges": [
            {
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat()
            },
            {
                "startDate": one_year_before(start_date).isoformat(),
                "endDate": one_year_before(end_date).isoformat()
            }
        ],
        "metrics": [
            {
                "expression": "ga:users"
            }
        ],
        "dimensionFilterClauses": [
            {
                "filters": [
                    {
                        "dimensionName": "ga:pagePath",
                        "operator": "REGEXP",
                        "expressions": [
                            page_path
                        ]
                    }
                ]
            }
        ]
    }


def get_all_transactions_request():
    start_date, end_date = find_last_full_twelve_months()

    return {
        'viewId': VADOTGOV_VIEW_ID,
        'dateRanges': [{'startDate': start_date.isoformat(),
                        'endDate': end_date.isoformat()}],
        'metrics': [{'expression': 'ga:totalEvents'}],
        'dimensions': [
            {'name': 'ga:yearMonth'}
        ],
        'dimensionFilterClauses': [
            {
                'operator': 'AND',
                'filters': [
                    {
                        'dimensionName': 'ga:eventCategory',
                        'operator': 'EXACT',
                        'expressions': ['Transactions']
                    },
                    {
                        'dimensionName': 'ga:pagePath',
                        'operator': 'REGEXP',
                        'expressions': ['www.va.gov/']
                    }
                ]
            }
        ]
    }


def get_transactions_for_tools_request(tool):
    start_date, end_date = find_last_thirty_days()

    return {
        'viewId': VADOTGOV_VIEW_ID,
        'dateRanges': [{'startDate': start_date.isoformat(),
                        'endDate': end_date.isoformat()}],
        'metrics': [{'expression': 'ga:totalEvents'}],
        'dimensionFilterClauses': [
            {
                'operator': 'AND',
                'filters': [
                    {
                        'dimensionName': 'ga:eventCategory',
                        'operator': 'REGEXP',
                        'expressions': [tool['event_category_filter']]
                    },
                    {
                        'dimensionName': 'ga:pagePath',
                        'operator': 'REGEXP',
                        'expressions': [tool['page_path_filter']]
                    }
                ]
            }
        ]
    }
