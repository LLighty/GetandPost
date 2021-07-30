from Utilities.Get import get_website_cli
from Utilities.Save import save_data
import errno


def entry_point(args):
    print("cli entry")
    website_address = args.url
    if website_address is None:
        print("Unexpected Error has occurred - URL parameter was not passed")
        exit(errno.EINVAL)
    website_address = check_http(website_address)
    data = get_website_cli(website_address, args)
    if args.save is not None:
        save_data(data, args.save)


def check_http(address):
    if "http" not in address[0:4]:
        address = "https://" + address
    return address
