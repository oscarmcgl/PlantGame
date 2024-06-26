import json

def experience(): #? this won't be needed anyway
    with open('database/users.json') as file:
        data = json.load(file)
        leaderboard = []
        for i in range(1, len(data)):
            leaderboard.append([data[i]['experience'], data[i]['id']])
            leaderboard.sort(reverse=True)
            print(leaderboard)
        print(f"Top Experience: {data[leaderboard[0][1]]['name']} with {leaderboard[0][0]} xp")

def level():
    with open('database/users.json') as db:
        data = json.load(db)
        leaderboard = []    
        for i in range(1, len(data)):
            leaderboard.append([data[i]['level'], data[i]['id']])
            leaderboard.sort(reverse=True)
            print(leaderboard)
        return f"Top Level: {data[leaderboard[0][1]]['name']} with level {leaderboard[0][0]}"