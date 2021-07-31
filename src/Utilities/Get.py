import requests
from bs4 import BeautifulSoup

prettify_text = False
headers = None


def get_website_cli(address, variables):
    set_variables(variables)
    data = get_website_data(address)
    print_website_data(data)
    return data


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
