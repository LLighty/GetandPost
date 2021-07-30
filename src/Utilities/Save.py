

def save_data(data, file_name):
    if file_name is None:
        print("There was no file name specified so saving did not occur.")
        return
    print("Saving data to %s" % file_name)
    with open(file_name, 'w') as f:
        for line in data:
            f.write(line)
            f.write('\n')