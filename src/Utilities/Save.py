

def save_data(data, file_name):
    print("Saving data to %s" % file_name)
    try:
        with open(file_name, 'w') as f:
            for line in data:
                f.write(line)
                f.write('\n')
    except IOError as error:
        print(error)