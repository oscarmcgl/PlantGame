import json 
import userface as uf


def retrieve_data(num, info):
    with open('database/info.json', 'r') as db:
        data = json.load(db)

        return data[num][info]


def name(num):
    retrieve_data(num, 'name')

def pname(num):
    retrieve_data(num, 'proper_name')


def add_plant(type):

    if uf.checklogin() is False:
        print('Not logged in.')
        return None
    else:
        with open('database/info.json', 'r') as db:
            data = json.load(db)
            currentid = data[0]['currentid'] #! This doesn't work??
            print(currentid)




    



