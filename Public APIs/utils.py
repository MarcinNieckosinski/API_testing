entries_url = "https://api.publicapis.org/entries"
random_url = "https://api.publicapis.org/random"
categories_url = "https://api.publicapis.org/categories"
health_url = "https://api.publicapis.org/health"


def check_if_each_entry_has_key(response, key):
    response_body = response.json()
    entries = response_body["entries"]
    key_counter = 0
    for entry in entries:
        if key in entry:
            key_counter = key_counter + 1
    return key_counter


def check_if_each_entry_has_correct_data(response, data):
    response_body = response.json()
    entries = response_body["entries"]
    data_counter = 0
    for entry in entries:
        if str(data[1]).upper() in str(entry[data[0]]).upper():
            data_counter = data_counter + 1
    return len(entries) == data_counter
