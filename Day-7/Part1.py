with open("Inputs\Day7.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# [name, [providers] or value, command]
properties = []
letters = []


def decode(input):
    # Initializing variables
    returnVal = []
    global properties
    global letters

    command, name = input.split(" -> ")
    parts = command.split(" ")

    # If there is only one command (exact number or direct translation)
    if len(parts) == 1:
        try:
            properties.append([name, [], "DONE", int(parts[0])])
            letters.append(name)
            return
        except:
            properties.append([name, [parts[0]], "IS", -1])
            letters.append(name)
            return

    elif len(parts) == 2:
        properties.append([name, [parts[1]], parts[0], -1])
        letters.append(name)
        return

    else:
        if parts[0] == '1':
            parts[0] = parts[2]
            parts[2] = '1'
        try:
            properties.append([name, [parts[0], int(parts[2])], parts[1], -1])
            letters.append(name)
            return
        except:
            properties.append([name, [parts[0], parts[2]], parts[1], -1])
            letters.append(name)
            return
    return


def runCommand(input):
    global letters
    global properties
    commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT", "IS"]

    # Moving the variables to individual variables
    name, inputs, command, val = input
    #print(input)
    num = commands.index(command)
    #print(inputs)
    if num == 0:
        val = int(inputs[0] & inputs[1])
    elif num == 1:
        val = int(inputs[0] | inputs[1])
    elif num == 4:
        val = int(~inputs[0])
    elif num == 5:
        val = int(inputs[0])
    elif num == 2:
        val = int(inputs[1] << inputs[0])
    elif num == 3:
        val = int(inputs[1] >> inputs[0])

    index = letters.index(name)
    properties[index][2] = "DONE"
    properties[index][3] = val
    return


for command in lines:
    decode(command)


notFoundA = True
while notFoundA:
    for command in properties:
        if command[0] == "a" and command[2] == "DONE":
            print("The signal ultimately provided to wire a is", command[3])
            notFoundA = False
            break
        if command[2] != "DONE":
            moveOn = True
            #print(command[1])
            for parent in command[1]:
            #for i in range(len(command)):
                #print(moveOn, parent)
                #print(type(parent), parent)
                if isinstance(parent, str):
                    moveOn = False
                    index = letters.index(parent)
                    if properties[index][2] == "DONE":
                        #print(command[1])
                        command[1].pop(command[1].index(parent))
                        command[1].append(properties[index][3])
            if moveOn:
                #print("running moveOn")
                runCommand(command)