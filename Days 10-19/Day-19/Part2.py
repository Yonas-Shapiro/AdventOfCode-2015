import random

with open("Inputs\Day19.txt", 'r') as q:
#with open("Sample.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Gathering the information
def readLine(input):
    start, ar, end = input.split(" ")
    return [start, end]


# Finding out how many turns it will take to reduce to "e"
def numPossibleValues(changes, values, molecule):
    check = {}
    mol = molecule
    num = 0
    for j in values: check[j] = ""
    while mol != "e":
        for j in values:
            # If no other changes can be made, reset.
            if check[j] == mol: mol = "ee"
            val = mol.count(j)
            num += val
            mol = mol.replace(j, changes[j])
            if mol == "e": return num
        if mol.count("e") > 1:
            # If multiple "e"s are in the string, there has been a failure. Run again with a different order
            random.shuffle(values)
            num = 0
            mol = molecule
    return num
    

# Compiling the information
molecule = lines[-1]
changes = {}
for line in lines:
    if line == "": break
    x = readLine(line)
    changes[x[1]] = x[0]
values = changes.keys()
values = sorted(values, key=len, reverse=True)
print(values)


# Finding out how many distinct molecules can be made
num = numPossibleValues(changes, values, molecule)
print("It will take", num, "steps to go from \"e\" to the medecine molecule")