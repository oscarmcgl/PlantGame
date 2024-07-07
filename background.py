# things happening in the background
#todo probably experience leveling, plant growth, etc.

import json
import userface as uf

def backgroundruns():
    checkexperience()


def checkexperience():
    if uf.checklogin() is False:
        print("Not logged in")
        return None
    else:
        experience: int = uf.retrieve('experience')
        current_level = uf.retrieve('level')
        if experience >= 100:
            experience -= 100
            current_level += 1
            uf.store('experience', experience)
            uf.store('level', current_level)
            print("Congratulations! You have leveled up to level " + str(current_level) + "!")
        else:
            print("You have " + str(experience) + " experience points until the next level.")
