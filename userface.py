#logs in a user with their username based off users.json, else will create profile for username, add verification check on username

#todo add a password system

database: str | None = "database/users.json"
assert database, "Cannot run without user database"

import json

def login(username):
    with open('database/users.json') as db:
        data = json.load(db)
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

            ans = input().lower()
            if ans == 'y':
                createprofile()
            else:
                print("Returning to main menu")
                #! add code to return to main menu 
                #? needs a main menu??

def createprofile():
    if checklogin() is True:
        print("Already logged in, cannot create profile")
        return

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

def checklogin(): #returns true or false based on login
    with open ('database/users.json','r') as db:
        data = json.load(db)

        if data[0]['currentuser'] == "none":
            return False
        else:
            return True
    


def changename(nname):
    if checklogin() is False:
        print("Not logged in, cannot change name")
    
    else:
        with open('database/users.json') as db:
            data = json.load(db)
            currentid = int(data[0]['currentid'])
            data[currentid]['name'] = nname

            with open('database/users.json', 'w') as db:
                json.dump(data, db, indent=4)
            print(f"Name changed to {nname}")

def changeusername(nusername):
    if checklogin() is False:
        print("Not logged in, cannot change username")
    else:
        with open('database/users.json') as db:
            data = json.load(db)
            for i in range(1, len(data)):
                if data[i]['username'] == nusername:
                    print("Username already taken")
                    break
            else:
                    currentid = int(data[0]['currentid'])
                    data[currentid]['username'] = nusername
                    with open('database/users.json', 'w') as db:
                        json.dump(data, db, indent=4)
                        print(f"Username changed to {nusername}")   


def retrieve(info):
    with open('database/users.json', 'r') as db:
        data = json.load(db)
        if checklogin() is False:
            print('Not logged in.')
            return None
        else:
            currentid = data[0]['currentid']                    
            return data[currentid][info] 
        
def store(info, data):
    with open('databaser/users.json', 'r') as db:
        data = json.load(db)
        if checklogin() is False:
            print('Not logged in.')
            return None
        else:
            try:
                currentid = data[0]['currentid']
                data[currentid][info] = data
                with open('database/users.json', 'w') as db:
                    json.dump(data, db, indent=4)
                    print("Data stored")
            except KeyError:
                print("Does not exist")
                return None
            except: 
                print("Error")
                return None




def logout():
    with open('database/users.json') as db:
        data = json.load(db)
        user = data[0]['currentuser']
        data[0]['currentuser'] = "none"
        data[0]['currentid'] = 0

        with open('database/users.json', 'w') as db:
            json.dump(data, db, indent=4)

        print(f"Logged out {user}")


def currentid():
    if not checklogin():
        with open('databaser/users.json', 'r') as db:
            data = json.load(db)
            return data[0]['currentid']
    else:
        return None

def currentuser():
    if not checklogin():
        with open('databaser/users.json', 'r') as db:
            data = json.load(db)
            return data[0]['currentuser']
    else:
        return None
    