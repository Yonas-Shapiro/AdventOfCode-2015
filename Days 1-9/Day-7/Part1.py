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

    # Two commands (Not)
    elif len(parts) == 2:
        properties.append([name, [parts[1]], parts[0], -1])
        letters.append(name)
        return

    # Three commands (Shift, and , or)
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
    # Initializing + getting variables
    global letters
    global properties
    commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT", "IS"]

    # Moving the variables to individual variables
    name, inputs, command, val = input

    # Finding out what the command is, then carrying it out
    num = commands.index(command)
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

    # Changing the command to "DONE", and adding the proper value
    index = letters.index(name)
    properties[index][2] = "DONE"
    properties[index][3] = val
    return


# Running through each line to decode it
for command in lines:
    decode(command)


# Running through the decoded results to get "A" to "DONE"
notFoundA = True
while notFoundA:
    for command in properties:
        if command[0] == "a" and command[2] == "DONE":
            print("The signal ultimately provided to wire a is", command[3])
            notFoundA = False
            break
        if command[2] != "DONE":
            moveOn = True
            for parent in command[1]:
                if isinstance(parent, str):
                    moveOn = False
                    index = letters.index(parent)
                    if properties[index][2] == "DONE":
                        command[1].pop(command[1].index(parent))
                        command[1].append(properties[index][3])
            if moveOn:
                runCommand(command)