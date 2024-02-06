from datetime import timedelta
import requests
import utils


def test_get_entries_positive_response():
    response = requests.get(utils.entries_url)
    assert response.status_code == 200


def test_get_entries_good_response_time():
    response = requests.get(utils.entries_url)
    assert response.elapsed < timedelta(seconds=3)


def test_get_entries_check_content_type_equals_json():
    response = requests.get(utils.entries_url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_entries_count_equals_entries_count():
    response = requests.get(utils.entries_url)
    response_body = response.json()
    count_value = response_body["count"]
    entries_count = len(response_body["entries"])
    assert count_value == entries_count


def test_get_entries_each_entry_has_api_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "API")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_description_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "Description")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_auth_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "Auth")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_https_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "HTTPS")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_cors_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "Cors")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_link_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "Link")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_each_entry_has_category_key():
    response = requests.get(utils.entries_url)
    key_counter = utils.check_if_each_entry_has_key(response, "Category")
    entries_count = response.json()["count"]
    assert key_counter == entries_count


def test_get_entries_title_positive_response():
    response = requests.get(utils.entries_url + "?title=at")
    assert response.status_code == 200


def test_get_entries_title_correct_data_in_response():
    response = requests.get(utils.entries_url + "?title=at")
    data = ("API", "at")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_description_positive_response():
    response = requests.get(utils.entries_url + "?description=an")
    assert response.status_code == 200


def test_get_entries_description_correct_data_in_response():
    response = requests.get(utils.entries_url + "?description=an")
    data = ("Description", "an")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_auth_positive_response():
    response = requests.get(utils.entries_url + "?auth=apikey")
    assert response.status_code == 200


def test_get_entries_auth_correct_data_in_response():
    response = requests.get(utils.entries_url + "?auth=apikey")
    data = ("Auth", "apikey")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_https_positive_response():
    response = requests.get(utils.entries_url + "?https=false")
    assert response.status_code == 200


def test_get_entries_https_correct_data_in_response():
    response = requests.get(utils.entries_url + "?https=false")
    data = ("HTTPS", "false")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_cors_positive_response():
    response = requests.get(utils.entries_url + "?cors=yes")
    assert response.status_code == 200


def test_get_entries_cors_correct_data_in_response():
    response = requests.get(utils.entries_url + "?cors=yes")
    data = ("Cors", "yes")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_category_positive_response():
    response = requests.get(utils.entries_url + "?category=nima")
    assert response.status_code == 200


def test_get_entries_category_correct_data_in_response():
    response = requests.get(utils.entries_url + "?category=nima")
    data = ("Category", "nima")
    assert utils.check_if_each_entry_has_correct_data(response, data)


def test_get_entries_title_and_category_positive_response():
    response = requests.get(utils.entries_url + "?title=at&category=ni")
    data = ("API", "at")
    assert utils.check_if_each_entry_has_correct_data(response, data)
    data = ("Category", "ni")
    assert utils.check_if_each_entry_has_correct_data(response, data)
