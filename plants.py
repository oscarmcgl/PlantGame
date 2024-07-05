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

            if len(data)-1 < type:
                print('Plant not found in database.')
                return None
            
            else:
                plantname = data[type]['name']

        with open('database/users.json', 'r') as db:
            data = json.load(db)
            currentid = data[0]['currentid'] 
            owned_plants = data[currentid]['owned_plants']
            owned_plants.append(type)
            data[currentid]['owned_plants'] = owned_plants
            with open('database/users.json', 'w') as db:
                json.dump(data, db, indent=4)
                print(plantname + ' added to your collection.')

def remove_plant(type):

    if uf.checklogin() is False:
        print('Not logged in.')
        return None
    else:
        with open('database/info.json', 'r') as db:
            data = json.load(db)

            if len(data)-1 < type:
                print('Plant not found in database.')
                return None
            
            else:
                plantname = data[type]['name']

        try:
            with open('database/users.json', 'r') as db:
                data = json.load(db)
                currentid = data[0]['currentid']
                owned_plants = data[currentid]['owned_plants']
                owned_plants.remove(type)
                data[currentid]['owned_plants'] = owned_plants
                with open('database/users.json', 'w') as db:
                    json.dump(data, db, indent=4)
                    print(plantname + ' removed from your collection.')
        except:
            print('Plant not found in database.')



    



