with open("Inputs\Day3.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    commands = lines[0]
    q.close()


santa = [0, 0]
robo = [0, 0]
roboTurn = False
locations ={(0, 0)}

def newLocation(command):
    global santa
    global robo
    global roboTurn
    ud = 0
    lr = 0


    if command == "^":
        ud = -1
    elif command == ">":
        lr = 1
    elif command == "v":
        ud = 1
    else:
        lr = -1

    if roboTurn:
        robo[0] += lr
        robo[1] += ud
        roboTurn = False
        return tuple(robo)
    
    santa[0] += lr
    santa[1] += ud
    roboTurn = True

    return tuple(santa)


for command in commands:
    locations.add(newLocation(command))


print("Santa and Robo-Santa have visited", len(locations), "houses.")