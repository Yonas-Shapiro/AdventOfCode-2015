with open("Inputs\Day19.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Gathering the information
def readLine(input):
    print(input)
    start, ar, end = input.split(" ")
    return [start, end]


# Getting all possible values
def numPossibleValues(changes, molecule):
    possibilities = set()
    for i in range(len(molecule)):
        if i < len(molecule)-1 and molecule[i+1].islower():
            if molecule[i:i+2] in changes:
                for x in changes[molecule[i:i+2]]:
                    possibilities.add(molecule[:i] + x + molecule[i+2:])
        else:
            if molecule[i] in changes:
                for x in changes[molecule[i]]:
                    possibilities.add(molecule[:i] + x + molecule[i+1:])
    return len(possibilities)
    

# Compiling the information
molecule = lines[-1]
changes = {}
for line in lines:
    if line == "": break
    x = readLine(line)
    if x[0] not in changes:
        changes[x[0]] = [x[1]]
    else: changes[x[0]].append(x[1])


# Finding out how many distinct molecules can be made
num = numPossibleValues(changes, molecule)
print("There are", num, "distinct molecules that can be made.")