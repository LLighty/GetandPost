import argparse
import sys
from CLI.CommandLine import entry_point
from GUI.GUI import init

def get_parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', "--url", type=str, help="Specifies the website for the post or get request.")
    parse.add_argument('-pr', "--prettify", help="Prints (and saves) the get request in a more human readable format.",
                       action="store_true")
    parse.add_argument('-s', "--save", type=str, help="Saves the output to the specified out file")
    parse.add_argument('-H', "--headers", type=str, help="Sets the headers for the request")
    parse.add_argument('-p', "--post", type=str, help="Specifies to conduct a Post Request with the data appended after"
                                                      ". Data should be in the format 'var1:1,var2:2'")
    return parse


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    if len(sys.argv) > 1:
        entry_point(args)
    else:
        init(args)
