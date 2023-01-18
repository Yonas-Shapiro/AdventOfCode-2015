with open("Inputs\Day3.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    commands = lines[0]
    q.close()


# Initializing location variables (Santa's current location and list of past locations Santa has been)
santa = [0, 0]
locations = set((0, 0))


# Getting Santa's new location
def newLocation(command):
    # Getting / initializing variables
    global santa
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

    # Moving Santa appropriately
    santa[0] += lr
    santa[1] += ud

    # Returning Santa's new location
    return tuple(santa)



for command in commands:
    locations.add(newLocation(command))


print("Santa has visited", len(locations), "houses.")