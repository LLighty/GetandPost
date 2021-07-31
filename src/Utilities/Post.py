import requests
from bs4 import BeautifulSoup

data_to_post = None


def post_website_cli(address, variables):
    set_variables(variables)
    response = get_post_response(address)
    return response


def set_variables(variables):
    global data_to_post
    data_to_post = variables.post


def get_post_response(address):
    response = requests.post(address, convert_data_to_object(data_to_post))
    return response


def convert_data_to_object(data):
    return_data = {}
    variables = data.split(",")
    for var in variables:
        values = var.split(":")
        key = values[0]
        value = values[1]
        return_data[key] = value
    return return_data
