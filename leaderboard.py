import json

def experience():
    with open('database/users.json') as file:
        data = json.load(file)
        leaderboard = []
        for i in range(1, len(data)):
            leaderboard.append([data[i]['experience'], data[i]['id']])
            leaderboard.sort(reverse=True)
            print(leaderboard)
        print(f"Top Experience: {data[leaderboard[0][1]]['name']} with {leaderboard[0][0]} xp")

