"""
Test cases for GET /fact
"""
from datetime import timedelta
import requests

base_link = "https://catfact.ninja/fact"


def test_get_fact_positive_response():
    """
    Positive response.
    """
    response = requests.get(base_link)
    assert response.status_code == 200


def test_get_fact_good_response_time():
    """
    Response under 3 seconds.
    """
    response = requests.get(base_link)
    assert response.elapsed < timedelta(seconds=3)


def test_get_fact_check_content_type_equals_json():
    """
    Content type is application/json.
    """
    response = requests.get(base_link)
    assert response.headers["Content-Type"] == "application/json"


def test_get_fact_is_valid_json():
    """
    Is response a valid JSON.
    """
    response = requests.get(base_link)
    assert response.json()


def test_get_fact_max_length_parameter():
    """
    Returned fact is shorter or equal max length given.
    Length is less than or equal max_length.
    """
    response = requests.get(base_link + "?max_length=30")
    response_body = response.json()
    assert response_body["length"] <= 30
    assert len(response_body["fact"]) == response_body["length"]


def test_get_fact_length_is_correct():
    """
    Returned facts length is equal to length value.
    Try few facts.
    """
    for i in range(5):
        response = requests.get(base_link)
        response_body = response.json()
        assert len(response_body["fact"]) == response_body["length"]


def test_get_fact_max_length_equal_zero():
    """
    No fact is given back once max_length parameter is 0.
    """
    response = requests.get(base_link + "?max_length=0")
    response_body = response.json()
    assert response_body == {}
