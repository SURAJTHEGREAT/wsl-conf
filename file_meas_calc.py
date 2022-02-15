import json


def FILE_TO_LIST(filename, encode=None):
    file_list = list()
    try:
        if encode is not None:
            with open(filename, encoding=encode) as f:
                txt_obj = f.read()
        else:
            with open(filename) as f:
                txt_obj = f.read()

        file_list = txt_obj.split()

    except Exception as e:
        print("unable to read file and convert to JSON " + str(e))
    finally:
        return file_list


def FILE_TO_JSON(filename, encode=None):
    json_object = {}
    try:
        if encode is not None:
            with open(filename, encoding=encode) as f:
                json_object = json.loads(f.read())
        else:
            with open(filename) as f:
                json_object = json.loads(f.read())

    except Exception as e:
        print("unable to read file and convert to JSON " + str(e))
    finally:
        return json_object


def GET_VALUES(file_list, module_path):
    meas_count = 0
    file_count = 0
    for file in file_list:
        file = module_path + "/" + file
        meas_count += len(FILE_TO_JSON(file).get("measurements", list()))
        file_count += 1
    print("The number of files is {0} and measurements count : {1}".format(file_count,meas_count))


if __name__ == '__main__':
    print("Remember to execute me as root user")
    master_file = input("Enter the file location where master file is available:")
    module_path = input("Enter the module path:")
    GET_VALUES(FILE_TO_LIST(filename=master_file), module_path=module_path)
