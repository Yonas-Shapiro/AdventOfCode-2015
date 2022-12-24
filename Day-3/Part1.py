with open("Inputs\Day3.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    commands = lines[0]
    q.close()


santa = [0, 0]
locations = set((0, 0))

def newLocation(command):
    global santa
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

    santa[0] += lr
    santa[1] += ud

    return tuple(santa)



for command in commands:
    locations.add(newLocation(command))


print("Santa has visited", len(locations), "houses.")