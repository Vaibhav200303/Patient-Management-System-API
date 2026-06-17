import json

#this is the json file where patient records will be stored
DATA_FILE = "patients.json"


#i need functions such as load data and save data to handle the json file where we will store our patient records for now
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

