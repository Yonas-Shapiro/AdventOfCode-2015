with open("Inputs\Day3.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    commands = lines[0]
    q.close()


# Initializing Santa's location, Robo-Santa's location, visited locations, and who's turn it is to move
santa = [0, 0]
robo = [0, 0]
roboTurn = False
locations ={(0, 0)}


# Getting Santa's (or Robo-Santa's) new location
def newLocation(command):
    # Getting / initializing variables
    global santa
    global robo
    global roboTurn
    ud = 0
    lr = 0

    # Getting the appropriate command
    if command == "^":
        ud = -1
    elif command == ">":
        lr = 1
    elif command == "v":
        ud = 1
    else:
        lr = -1

    # If it is time to move Robo-Santa, move him, set it to Santa's turn, and return the newly visited location
    if roboTurn:
        robo[0] += lr
        robo[1] += ud
        roboTurn = False
        return tuple(robo)
    
    # If it isn't Robo-Santa's turn it must be Santa's
    # So, move Santa, set it to Robo-Santa's turn, and return the newly visited location
    santa[0] += lr
    santa[1] += ud
    roboTurn = True
    return tuple(santa)


for command in commands:
    locations.add(newLocation(command))


print("Santa and Robo-Santa have visited", len(locations), "houses.")