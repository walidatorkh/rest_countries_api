import requests
import json
from cerberus import Validator
from configurations import base_url
from assertpy import assert_that
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def load_test_data():
    logging.info(f"Testing schema countries: Load test data")
    with open('test_json_schema.json', 'r', encoding='utf-8') as file:
        return json.load(file)[0]


def test_schema_countries_api():
    logging.info(f"Testing schema countries: send request to https://restcountries.com/v3.1/alpha/US")
    response = requests.get(f"{base_url}/alpha/US")
    assert_that(response.status_code).is_equal_to(200)
    logging.info(f"Testing schema countries: valid response code 200 ")
    data = response.json()[0]
    schema = {
        'name': {
            'type': 'dict',
            'schema': {
                'common': {'type': 'string'},
                'official': {'type': 'string'},
                'nativeName': {'type': 'dict'},
            }
        },
        'tld': {'type': 'list', 'schema': {'type': 'string'}},
        'cca2': {'type': 'string'},
        'ccn3': {'type': 'string'},
        'cca3': {'type': 'string'},
        'cioc': {'type': 'string'},
        'independent': {'type': 'boolean'},
        'status': {'type': 'string'},
        'unMember': {'type': 'boolean'},
        'currencies': {'type': 'dict'},
        'idd': {'type': 'dict'},
        'capital': {'type': 'list', 'schema': {'type': 'string'}},
        'altSpellings': {'type': 'list', 'schema': {'type': 'string'}},
        'region': {'type': 'string'},
        'subregion': {'type': 'string'},
        'languages': {'type': 'dict'},
        'translations': {'type': 'dict'},
        'latlng': {'type': 'list', 'schema': {'type': 'float'}},
        'landlocked': {'type': 'boolean'},
        'borders': {'type': 'list', 'schema': {'type': 'string'}},
        'area': {'type': 'float'},
        'demonyms': {'type': 'dict'},
        'flag': {'type': 'string'},
        'maps': {'type': 'dict'},
        'population': {'type': 'integer'},
        'gini': {'type': 'dict'},
        'fifa': {'type': 'string'},
        'car': {'type': 'dict'},
        'timezones': {'type': 'list', 'schema': {'type': 'string'}},
        'continents': {'type': 'list', 'schema': {'type': 'string'}},
        'flags': {'type': 'dict'},
        'coatOfArms': {'type': 'dict'},
        'startOfWeek': {'type': 'string'},
        'capitalInfo': {'type': 'dict'},
        'postalCode': {'type': 'dict'},
    }

    validator = Validator(schema)
    assert validator.validate(data), validator.errors
    logging.info(f"Testing schema countries: validate(data) pass ")

    expected_data = load_test_data()
    assert_that(data).is_equal_to(expected_data)
    logging.info(f"Testing schema countries: data == expected_data ")
