with open("Inputs\Day6.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Global variables
grid = []
for i in range(1000):
    grid.append([])
    for j in range(1000):
        grid[i].append(False)


def runCommand(input):
    # Global variable
    global grid

    # Seeing what kind of command it is
    if input[:4] == "turn":
        turn, onOff, inf, na, out = input.split(" ")
    else:
        toggle, inf, na, out = input.split(" ")
        turn = False

    # Getting the specific numbers to change
    in1, in2 = inf.split(",")
    out1, out2 = out.split(",")
    in1 = int(in1)
    in2 = int(in2)
    out1 = int(out1)
    out2 = int(out2)

    # Running the Turn on/off commands
    if (turn):
        if onOff == "on":
            for i in range(in1, out1+1):
                for j in range(in2, out2+1):
                    grid[i][j] = True
        else:
            for i in range(in1, out1+1):
                for j in range(in2, out2+1):
                    grid[i][j] = False
    
    # Running the toggle commands
    else:
        for i in range(in1, out1+1):
            for j in range(in2, out2+1):
                grid[i][j] = not grid[i][j]

    return


# Running through the input
for command in lines:
    runCommand(command)


on = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j]:
            on += 1


print(on, "lights are lit.")

