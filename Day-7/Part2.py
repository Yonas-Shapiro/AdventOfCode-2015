with open("Inputs\Day7.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# [name, [providers] or value, command]
properties = []
letters = []
run2 = False
aRun1 = 0

def decode(input):
    # Initializing variables
    returnVal = []
    global properties
    global letters
    global run2
    global aRun1

    # Getting the input variables
    command, name = input.split(" -> ")
    parts = command.split(" ")

    # Setting "B" to first run "A" for the second run
    if run2 and name == "b":
        properties.append([name, [], "DONE", aRun1])
        letters.append(name)
        return
    
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

    # Two commands means "NOT"
    elif len(parts) == 2:
        properties.append([name, [parts[1]], parts[0], -1])
        letters.append(name)
        return

    # Three commands (Shift, and, or)
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


# Carrying out the command
def runCommand(input):
    # Initializing and getting variables
    global letters
    global properties
    commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT", "IS"]

    # Moving the variables to individual variables
    name, inputs, command, val = input

    # Getting the command and carrying it out
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

    # Changing the command to "DONE" and giving the proper value
    index = letters.index(name)
    properties[index][2] = "DONE"
    properties[index][3] = val
    return


# Running through the input to decode (Round 1)
for command in lines:
    decode(command)


# Finding the "a" value for the first run
notFoundA = True
while notFoundA:
    for command in properties:
        if command[0] == "a" and command[2] == "DONE":
            aRun1 = command[3]
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
            

# Running a second time for new Wire B value
for i in range(len(properties)):
    properties.pop()
    letters.pop()
run2 = True


# Decoding the input again
for command in lines:
    decode(command)


# Finding the new value for "A"
notFoundA = True
while notFoundA:
    for command in properties:
        if command[0] == "a" and command[2] == "DONE":
            print("The signal ultimately provided to wire a is", command[3])
            notFoundA = False
            break
        if command[2] != "DONE":
            #print(command[2])
            moveOn = True
            #print(command[1])
            for parent in command[1]:
                if isinstance(parent, str):
                    moveOn = False
                    index = letters.index(parent)
                    if properties[index][2] == "DONE":
                        #print(command[1])
                        command[1].pop(command[1].index(parent))
                        command[1].append(properties[index][3])
            if moveOn:
                runCommand(command)