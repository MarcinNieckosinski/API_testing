"""
Test cases for GET /facts
"""
from datetime import timedelta
import requests

base_link = "https://catfact.ninja/facts"


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


def test_get_facts_default_response_ten_facts():
    """
    Default response gives 10 fatcs.
    """
    response = requests.get(base_link)
    response_body = response.json()
    assert len(response_body["data"]) == 10


def test_get_facts_default_response_limit_equals_zero():
    """
    Default response is given once limit is set to 0.
    """
    response = requests.get(base_link + "?limit=0")
    response_body = response.json()
    assert len(response_body["data"]) == 10


def test_get_facts_lengths_less_or_equal_max_length():
    """
    Given facts have maximum max_length signs.
    !!!If you want to find a bug - change max_length to value bigger than 27.!!!
    """
    response = requests.get(base_link + "?max_length=27")
    response_body = response.json()
    for entry in response_body["data"]:
        assert entry["length"] <= 27
        assert len(entry["fact"]) == entry["length"]


def test_get_facts_max_length_and_limit_specified():
    """
    Response contains quantity of facts equal to limit parameter.
    Response contains facts that have maximum max_length signs.
    """
    response = requests.get(base_link + "?max_length=27&limit=4")
    response_body = response.json()
    assert len(response_body["data"]) == 4
    for entry in response_body["data"]:
        assert entry["length"] <= 27
        assert len(entry["fact"]) == entry["length"]
