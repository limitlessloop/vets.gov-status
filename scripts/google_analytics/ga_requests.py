VADOTGOV_VIEW_ID = '176188361'


def get_logged_in_users_request(start_date, end_date):
    return {
        'viewId': VADOTGOV_VIEW_ID,
        'dateRanges': [{'startDate': start_date,
                        'endDate': end_date}],
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


def get_all_transactions_request(start_date, end_date):
    return {
        'viewId': VADOTGOV_VIEW_ID,
        'dateRanges': [{'startDate': start_date,
                        'endDate': end_date}],
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
