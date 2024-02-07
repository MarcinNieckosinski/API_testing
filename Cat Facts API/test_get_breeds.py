"""
Test cases for GET /breeds
"""

from datetime import timedelta
import requests
from requests import Response

base_link = "https://catfact.ninja/breeds"


def check_if_each_entry_has_key(response: Response, key: str) -> int:
    """
    Function checks if each entry in response has key given by user.
    :param response:
    Response that user got from url.
    :param key:
    Key that should be found in each entry.
    :return:
    Count of all entries that got key inside of it.
    """
    response_body = response.json()
    entries = response_body["data"]
    key_counter = 0
    for entry in entries:
        if key in entry:
            key_counter = key_counter + 1
    return key_counter


def test_get_breeds_positive_response():
    """
    Positive response.
    """
    response = requests.get(base_link)
    assert response.status_code == 200


def test_get_breeds_good_response_time():
    """
    Response under 3 seconds.
    """
    response = requests.get(base_link)
    assert response.elapsed < timedelta(seconds=3)


def test_get_breeds_check_content_type_equals_json():
    """
    Content type is application/json.
    """
    response = requests.get(base_link)
    assert response.headers["Content-Type"] == "application/json"


def test_get_breeds_is_valid_json():
    """
    Is response a valid JSON.
    """
    response = requests.get(base_link)
    assert response.json()


def test_get_breeds_with_limit_parameter_positive_response():
    """
    Positive response with limit parameter.
    """
    response = requests.get(base_link + "?limit=5")
    assert response.status_code == 200


def test_get_breeds_with_limit_parameter_breed_quantity():
    """
    Correct amount of breeds returned as stated in limit parameter.
    """
    response = requests.get(base_link + "?limit=5")
    response_body = response.json()
    assert len(response_body["data"]) == 5


def test_get_breeds_with_limit_over_breed_quantity():
    """
    Correct amount of breeds when limit is set over total breed quantity (98).
    """
    response = requests.get(base_link + "?limit=100")
    response_body = response.json()
    assert len(response_body["data"]) == 98


def test_get_breeds_each_breed_key():
    """
    Has every breed returned a "breed" key.
    """
    response = requests.get(base_link + "?limit=98")
    counter = check_if_each_entry_has_key(response, "breed")
    assert counter == 98


def test_get_breeds_each_country_key():
    """
    Has every breed returned a "country" key.
    """
    response = requests.get(base_link + "?limit=98")
    counter = check_if_each_entry_has_key(response, "country")
    assert counter == 98


def test_get_breeds_each_origin_key():
    """
    Has every breed returned a "origin" key.
    """
    response = requests.get(base_link + "?limit=98")
    counter = check_if_each_entry_has_key(response, "origin")
    assert counter == 98


def test_get_breeds_each_coat_key():
    """
    Has every breed returned a "coat" key.
    """
    response = requests.get(base_link + "?limit=98")
    counter = check_if_each_entry_has_key(response, "coat")
    assert counter == 98


def test_get_breeds_each_pattern_key():
    """
    Has every breed returned a "pattern" key.
    """
    response = requests.get(base_link + "?limit=98")
    counter = check_if_each_entry_has_key(response, "pattern")
    assert counter == 98


def test_get_breeds_check_connection_equal_keep_alive():
    """
    Connection is keep-alive.
    """
    response = requests.get(base_link + "?limit=98")
    assert response.headers["connection"] == "keep-alive"


def test_get_breeds_check_cache_control_equal_no_cache_private():
    """
    Cache-control is no-cache, private
    """
    response = requests.get(base_link + "?limit=98")
    assert response.headers["cache-control"] == "no-cache, private"


def test_get_breeds_check_x_content_type_options_equals_nosniff():
    """
    X-content-type-options is nosniff.
    """
    response = requests.get(base_link + "?limit=98")
    assert response.headers["x-content-type-options"] == "nosniff"


def test_get_breeds_check_access_control_allow_origin():
    """
    Access-control-allow-origin is *.
    """
    response = requests.get(base_link + "?limit=98")
    assert response.headers["access-control-allow-origin"] == "*"


def test_get_breeds_check_response_is_default_with_string_limit():
    """
    Response is default when limit parameter set with string instead integer.
    """
    string_response = requests.get(base_link + "?limit=text")
    default_response = requests.get(base_link)
    assert string_response.json() == default_response.json()
