#with open("Inputs\Day19.txt", 'r') as q:
with open("Sample.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Gathering the information
def readLine(input):
    print(input)
    start, ar, end = input.split(" ")
    return [start, end]


# Getting all possible values
def numPossibleValues(changes, molecule, current):
    if current == molecule:
        return 1
    
    

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
num = numPossibleValues(changes, molecule, 'e')
print("It will take", num, "steps to go from \"e\" to the medecine molecule")