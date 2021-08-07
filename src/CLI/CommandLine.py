from Utilities.Get import get_website
from Utilities.Post import post_website
from Utilities.Save import save_data
import errno


def entry_point(args):
    print("cli entry")
    if args.post is not None:
        post_request(args)
    else:
        get_request(args)


def get_request(args):
    print("get request")
    website_address = get_address(args)
    response = get_website(website_address, args)
    if args.save is not None:
        save_data(response, args.save)


def post_request(args):
    print("post request")
    website_address = get_address
    response = post_website(website_address, args)


def check_http(address):
    if "http" not in address[0:4]:
        address = "https://" + address
    return address


def get_address(args):
    website_address = args.url
    if website_address is None:
        print("Unexpected Error has occurred - URL parameter was not passed")
        exit(errno.EINVAL)
    website_address = check_http(website_address)
    return website_address
