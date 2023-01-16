with open("Inputs\Day16.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# The culprit's information
ticker = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}


# Processing the information
def readLines(input):
    vals = input.replace(":", "").replace(",", "").split(" ")
    return {"number":vals[1], vals[2]:int(vals[3]), vals[4]:int(vals[5]), vals[6]:int(vals[7])}



# Finding the correct Sue
def checkSue(sue):
    global ticker
    checks = list(sue.keys())
    checks.pop(0)
    for i in checks:
        if sue[i] != ticker[i]: return False
    return True



# Getting the information
sues = []
for line in lines:
    sues.append(readLines(line))


# Finding the right Sue, then printing out the result
for sue in sues:
    if checkSue(sue):
        print("The gift is from Sue", sue["number"])
        break
