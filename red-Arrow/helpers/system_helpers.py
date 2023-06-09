import json


def get_file_data():
    file = open("database/employees.json", "r")
    data_list = json.loads(file.read())
    file.close()
    return data_list


def save_to_file(data: dict):
    data_list = get_file_data()
    if len(data_list) < 1:
        data["id"] = 1
    else:
        data["id"] = len(data_list) + 1
    data_list.append(data)
    file = open("database/employees.json", "w")
    data_in_json = json.dumps(data_list)
    file.write(data_in_json)
    file.close()