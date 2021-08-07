def save_data(data, file_name):
    file_name += ".txt"
    print("Saving data to %s" % file_name)
    try:
        with open(file_name, 'w') as f:
            f.write("Url queried: " + data.url)
            f.write('\n')
    except IOError as error:
        print(error)
    save_raw_data(data, file_name)
    save_header_data(data, file_name)
    save_cookie_data(data, file_name)


def save_raw_data(data, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write("Raw: ")
            f.write("\n")
            for line in data.text:
                f.write(str(line))
                f.write('\n')
    except IOError as error:
        print(error)


def save_header_data(data, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write("Headers: ")
            f.write("\n")
            for line in data.headers:
                f.write(str(line))
                f.write('\n')
    except IOError as error:
        print(error)


def save_cookie_data(data, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write("Cookies: ")
            f.write("\n")
            for line in data.cookies:
                f.write(str(line))
                f.write('\n')
    except IOError as error:
        print(error)
