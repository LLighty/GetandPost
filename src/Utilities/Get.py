import requests


def get_website_cli(address):
    data = get_website_data(address)
    print_website_data(data)


def get_website_data(address):
    response = requests.get(address)
    return response


def print_website_data(data):
    print(data.text)
