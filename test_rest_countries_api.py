import pytest
import requests
import json
import logging
from configurations import base_url
from assertpy import assert_that

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration data
with open('test_config.json', 'r') as f:
    test_data = json.load(f)


# Test API Retrieve All Countries
def test_retrieve_all_countries():
    logging.info(f"Testing endpoint: endpoint - all")
    response = requests.get(f"{base_url}/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    print(f"Number of countries: {len(data)}")


# Create parameterized tests with descriptive names
@pytest.mark.parametrize("config", [pytest.param(
    item, id=item['name']) for item in test_data['endpoints']])
def test_parametrized_endpoints(config):
    name = config['name']
    endpoint = config['endpoint']
    expected_status = config['expected_status']
    expected_type = eval(config['expected_type'])  # Convert string to type
    key_value_pairs = config['key_value_pairs']

    logging.info(f"Testing endpoint: {endpoint} - {name}")

    response = requests.get(f"{base_url}{endpoint}")

    assert response.status_code == expected_status, f"Failed on {name}: Expected status {expected_status}, got {response.status_code}"

    data = response.json()
    assert isinstance(data, expected_type), f"Failed on {name}: Expected type {expected_type}, got {type(data)}"

    if expected_status == 200 and expected_type == list:
        for key, value in key_value_pairs.items():
            if key == 'name':
                assert any(country[key]['common'].lower() == value for country in
                           data), f"Failed on {name}: '{value}' not found in countries."
            else:
                assert any(
                    country[key] == value for country in data), f"Failed on {name}: Expected {key} = {value} not found."
    else:
        for key, value in key_value_pairs.items():
            assert data[key] == value, f"Failed on {name}: Expected {key} = {value}, got {data[key]}"


