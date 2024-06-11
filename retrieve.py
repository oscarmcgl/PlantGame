import json 


def retrieve_data(num, info):
    with open('database/info.json', 'r') as db:
        data = json.load(db)

        return data[num][info]




