import argparse
import sys
from CLI.CommandLine import entry_point


def get_parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("--url", type=str, help="Specifies the website for the post or get request.")
    parse.add_argument("--prettify", help="Prints (and saves) the get request in a more human readable format.",
                       action="store_true")
    parse.add_argument("--save", type=str, help="Saves the output to the specified out file")
    return parse


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    if len(sys.argv) > 1:
        entry_point(args)
