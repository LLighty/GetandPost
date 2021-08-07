import requests
from bs4 import BeautifulSoup

prettify_text = False
headers = None
payload = None


def get_website(address, variables):
    set_variables(variables)
    data = get_website_data(address)
    print_website_data(data)
    reset_variables()
    return data


def get_website(address, provided_headers):
    print(provided_headers)
    response = requests.get(address, headers=provided_headers)
    return response


def get_website_data(address):
    response = requests.get(address, headers=headers)
    return response


def print_website_data(data):
    if prettify_text:
        soup = BeautifulSoup(data.text)
        print(soup.prettify())
    else:
        print(data.text)


def set_variables(variables):
    set_prettify(variables.prettify)


def set_prettify(prettify_bool):
    global prettify_text
    print(prettify_bool)
    prettify_text = prettify_bool


def reset_variables():
    global prettify_text
    prettify_text = False
    global headers
    headers = None
    global payload
    payload = None
