from datetime import timedelta
import requests
import utils


def test_get_categories_positive_response():
    response = requests.get(utils.categories_url)
    assert response.status_code == 200


def test_get_categories_good_response_time():
    response = requests.get(utils.categories_url)
    assert response.elapsed < timedelta(seconds=3)


def test_get_categories_check_content_type_equals_json():
    response = requests.get(utils.categories_url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_categories_count_equals_categories_count():
    response = requests.get(utils.categories_url)
    response_body = response.json()
    assert response_body["count"] == len(response_body["categories"])
