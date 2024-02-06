"""
File contains functions used in test cases for Public APIs services.
"""

from requests import Response

entries_url = "https://api.publicapis.org/entries"
random_url = "https://api.publicapis.org/random"
categories_url = "https://api.publicapis.org/categories"
health_url = "https://api.publicapis.org/health"


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
    entries = response_body["entries"]
    key_counter = 0
    for entry in entries:
        if key in entry:
            key_counter = key_counter + 1
    return key_counter


def check_if_each_entry_has_correct_data(response: Response, data: tuple) -> bool:
    """
    Function checks if each entry in response has correct data.
    :param response:
    Response that user got from url.
    :param data:
    A tuple that consists from key(string) and data(string) that we are looking for in value.
    :return:
    Returns boolean information if each entry has correct data.
    """
    response_body = response.json()
    entries = response_body["entries"]
    data_counter = 0
    for entry in entries:
        if str(data[1]).upper() in str(entry[data[0]]).upper():
            data_counter = data_counter + 1
    return len(entries) == data_counter
