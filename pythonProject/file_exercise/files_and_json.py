import json

book = {
    "bree": {
        "name": "brenda"
    },
    "steve": {
        "name": "stephen muiru",
        "course": "computer science",
        "high school": "muhoho high"
    },
    "bob": {
        "name": "Bob",
        "course": "computer science",
        "high school": "mang'u"
    }
}

data = {}


# create the file enter the json
def create_file():
    with open("./json_data.txt", "w") as json_file:
        # this will convert the dictionary to string in json format and store it into the file.
        json_file.write(json.dumps(book))


def read_json():
    with open("./json_data.txt", "r") as json_file:
        json_data = json.loads(json_file.read())
        for person in json_data:
            print(json_data[person]["name"])
