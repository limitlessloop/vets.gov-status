from foresee.foresee_helpers import make_table_from_foresee_response


def test_make_table_from_foresee_response():
    response_items = [
        {
            'id': 'some-id-0',
            'latentScores': [
                {
                    "id": "ENM006991L0005",
                    "name": "Site Information",
                    "type": "ELEMENTS",
                    "score": 78.98988035
                },
                {
                    "id": "ENM006991L0006",
                    "name": "Satisfaction",
                    "type": "SATISFACTION",
                    "score": 85.15640191
                }
            ],
            'responses': [
                {
                    "id": "CPPAUTOA12079341",
                    "name": "url",
                    "phrase": "url",
                    "type": "CPP",
                    "label": "url",
                    "responseType": "TEXT_AREA",
                    "answers": ["https://www.va.gov/my-va/"]
                },
                {
                    "id": "CPPAUTOAd20535641",
                    "name": "window_height",
                    "phrase": "window_height",
                    "type": "CPP",
                    "label": "window_height",
                    "responseType": "TEXT_AREA",
                    "answers": ["788"]
                }
            ]
        }
    ]

    expected_table = [
        {
            'Satisfaction': 85.15640191,
            'url': 'https://www.va.gov/my-va/'
        }
    ]

    assert expected_table == make_table_from_foresee_response(response_items)


def test_make_table_from_foresee_response_should_not_include_items_without_urls():
    response_items = [
        {
            'id': 'some-id-0',
            'latentScores': [
                {
                    "id": "ENM006991L0005",
                    "name": "Site Information",
                    "type": "ELEMENTS",
                    "score": 78.98988035
                },
                {
                    "id": "ENM006991L0006",
                    "name": "Satisfaction",
                    "type": "SATISFACTION",
                    "score": 85.15640191
                }
            ],
            'responses': [
                {
                    "id": "CPPAUTOAd20535641",
                    "name": "window_height",
                    "phrase": "window_height",
                    "type": "CPP",
                    "label": "window_height",
                    "responseType": "TEXT_AREA",
                    "answers": ["788"]
                }
            ]
        }
    ]

    assert make_table_from_foresee_response(response_items) == []
