import pandas as pd

import foresee.foresee_helpers as foresee_helpers


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

    assert expected_table == foresee_helpers.make_table_from_foresee_response(response_items)


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

    assert foresee_helpers.make_table_from_foresee_response(response_items) == []


def test_make_table_from_foresee_response_should_not_raise_error_when_no_satisfaction():
    response_items = [
        {
            'id': 'some-id-0',
            'latentScores': [
                {
                    "id": "ENM006991L0005",
                    "name": "Site Information",
                    "type": "ELEMENTS",
                    "score": 78.98988035
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

    assert foresee_helpers.make_table_from_foresee_response(response_items) == []


def test_get_average_score():
    data = [
        {'Satisfaction': 80.0, 'url': 'some-url-1'},
        {'Satisfaction': 70.0, 'url': 'some-url-1'},
        {'Satisfaction': 40.0, 'url': 'some-url-2'},
    ]
    df = pd.DataFrame(data)

    score = foresee_helpers.get_average_score(df, 'some-url-1')
    assert isinstance(score, float)
    assert score == 75.0
