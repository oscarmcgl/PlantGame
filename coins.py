
#*For the purpose to deduct/add/transfer or view coins

import userface as uf
import json

def add(value):
    current = uf.retrieve('coins')
    with open ('database/users.json','r') as db:
        data = json.load(db)
        currentid = int(data[0]['currentid'])
        data[currentid]['coins']  =current + value

        with open('database/users.json', 'w') as db:
            json.dump(data, db, indent=4)

            print(f"Added {value} coins to account")

def deduct(value):
    current = uf.retrieve('coins')
    with open('database/users.json', 'r') as db:
        data = json.load(db)
        currentid = int(data[0]['currentid'])
        if current < value:
            print("Insufficient coins")
            return
        else:
            data[currentid]['coins'] = current - value

            with open('database/users.json', 'w') as db:
                json.dump(data, db, indent=4)

                print(f"Deducted {value} coins from account")

def view():
    return uf.retrieve('coins') #? what is the actual point of this 


def transfer(): 
    if uf.checklogin() is False:
        return None
    else:
        currentuser = uf.currentuser()
        currentid = uf.currentid()

        pass 

        #todo add transaction here + verification check