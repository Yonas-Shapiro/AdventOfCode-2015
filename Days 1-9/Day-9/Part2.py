import itertools

with open("Inputs\Day9.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Processing the information
def readLines(input):
    vals = input.split(" ")
    return [vals[0], vals[2], vals[4]]


# Finding the shortest route
def findShortestRoute(info):
    lengths = []
    for subset in itertools.permutations(list(info.keys()), len(info)):
        sum = 0
        for i in range(len(info)-1):
            sum += info[subset[i]][subset[i+1]]
        lengths.append(sum)
    lengths.sort()
    return lengths[0]


# Running throught the information
info = {}
for line in lines:
    vals = readLines(line)
    if vals[0] not in info:
        info[vals[0]] = {}
    if vals[1] not in info:
        info[vals[1]] = {}
    info[vals[0]][vals[1]] = int(vals[2])
    info[vals[1]][vals[0]] = int(vals[2])


# Calling the function to find the longest possible length
length = findShortestRoute(info)
print("The shortest total distance to visit all locations is", length, "kilometres.")