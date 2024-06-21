#logs in a user with their username based off users.json, else will create profile for username, add verification check on username


#todo add ability to check username with json file
#todo add ability to create profile for username
#todo add ability to verify username
#todo add ability co change username

import json

def login(username):
    with open('database/users.json') as db:
        data = json.load(db)
        print(data)
        for i in range(1, len(data)):
            if data[i]['username'] == username:

                data[0]['currentuser'] = username
                data[0]['currentid'] = i

                with open('database/users.json', 'w') as db:
                    json.dump(data, db, indent=4)
                print(f"Logged in as {username}")
                break
            
        else:
            print(f"User {username} not found, would you like to create a profile? (y/n)")

def createprofile():
    chosen = False
    while chosen is False:
        username = input("Enter a username: ")
        with open('database/users.json') as db:
            data = json.load(db)
            for i in range(1, len(data)):
                if data[i]['username'] == username:
                    print("Username already taken")
                    break
            else:
                check = input("Please enter your username again to confirm: ")
                if check == username:
                    name = input("Enter your name (This can be changed later): ")
                    id = len(data)
                    chosen = True
                    break
    
    new_profile = {

            "id": id,
            "username": username,
            "name": name,
            "owned_plants": [0],
            "coins": 100,
            "level": 0,
            "experience": 0,
            "inventory": {
                "fertilizer": 0,
                "water": 0,
                "pesticide": 0,
                "cuttings": 0
        }
        }

    with open('database/users.json', "r") as db:
        data = json.load(db)
        data.append(new_profile)

        with open('database/users.json', "w") as db:
            json.dump(data, db, indent=4)

def checklogin(): 
    with open ('database/users.json','r') as db:
        data = json.load(db)
    


def changename():
    #add code here
    pass

def retrieve(info):
    with open('database/users.json', 'r') as db:
        data = json.load(db)
        currentid = int(data[0][currentid])
        if currentid == 0:
            print('Not logged in.')
            return None
        else:                    
            return data[currentid][info] 
def logout():
    with open('database/users.json') as db:
        data = json.load(db)
        user = data[0]['currentuser']
        data[0]['currentuser'] = "none"

        with open('database/users.json', 'w') as db:
            json.dump(data, db, indent=4)
        print(f"Logged out {user}")


