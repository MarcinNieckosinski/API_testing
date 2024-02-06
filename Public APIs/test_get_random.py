import requests
import utils
from datetime import timedelta


def test_get_random_positive_response():
    response = requests.get(utils.random_url)
    assert response.status_code == 200


def test_get_random_good_response_time():
    response = requests.get(utils.random_url)
    assert response.elapsed < timedelta(seconds=3)


def test_get_random_check_content_type_equals_json():
    response = requests.get(utils.entries_url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_random_only_one_entry_each_time():
    for i in range(5):
        response = requests.get(utils.random_url)
        response_body = response.json()
        assert response_body["count"] == 1


def test_get_random_title_positive_response():
    response = requests.get(utils.random_url + "?title=at")
    assert response.status_code == 200


def test_get_random_title_correct_data_in_response():
    response = requests.get(utils.random_url + "?title=at")
    data = ("API", "at")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_description_positive_response():
    response = requests.get(utils.random_url + "?description=an")
    assert response.status_code == 200


def test_get_random_description_correct_data_in_response():
    response = requests.get(utils.random_url + "?description=an")
    data = ("Description", "an")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_auth_positive_response():
    response = requests.get(utils.random_url + "?auth=apikey")
    assert response.status_code == 200


def test_get_random_auth_correct_data_in_response():
    response = requests.get(utils.random_url + "?auth=apikey")
    data = ("Auth", "apikey")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_https_positive_response():
    response = requests.get(utils.random_url + "?https=false")
    assert response.status_code == 200


def test_get_random_https_correct_data_in_response():
    response = requests.get(utils.random_url + "?https=false")
    data = ("HTTPS", "false")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_cors_positive_response():
    response = requests.get(utils.random_url + "?cors=yes")
    assert response.status_code == 200


def test_get_random_cors_correct_data_in_response():
    response = requests.get(utils.random_url + "?cors=yes")
    data = ("Cors", "yes")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_category_positive_response():
    response = requests.get(utils.random_url + "?category=nima")
    assert response.status_code == 200


def test_get_random_category_correct_data_in_response():
    response = requests.get(utils.random_url + "?category=nima")
    data = ("Category", "nima")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_random_title_and_category_positive_response():
    response = requests.get(utils.random_url + "?title=at&category=ni")
    data = ("API", "at")
    assert utils.check_if_each_entry_has_correct_data(response, data)
    data = ("Category", "ni")
    assert utils.check_if_each_entry_has_correct_data(response, data)
