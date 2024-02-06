from datetime import timedelta
import requests
import utils


def test_get_health_positive_response():
    """
    Positive response.
    """
    response = requests.get(utils.health_url)
    assert response.status_code == 200


def test_get_health_good_response_time():
    """
    Response under 3 seconds.
    """
    response = requests.get(utils.health_url)
    assert response.elapsed < timedelta(seconds=3)


def test_get_health_check_content_type_equals_text():
    """
    Content type is text/plain; charset=utf-8.
    """
    response = requests.get(utils.health_url)
    assert response.headers["Content-Type"] == "text/plain; charset=utf-8"


def test_get_health_correct_response():
    """
    Response is correct ("alive": "True").
    """
    response = requests.get(utils.health_url)
    response_body = response.json()
    assert response_body["alive"] == True
