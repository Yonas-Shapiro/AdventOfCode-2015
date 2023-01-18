import itertools

with open("Inputs\Day13.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Decoding the input
def readLines(input):
    vals = input.replace(".", "").split(" ")
    num = int(vals[3])
    if vals[2] == "lose": num *= -1
    return [vals[0], vals[-1], num]


# Finding the highest combination of happiness
def getHappiest(info):
    happinesses = []

    # Running through each possible combination
    for x in itertools.permutations(list(info.keys()), len(info)):
        smile = 0
        for i in range(len(info)-1):
            smile += info[x[i]][x[i+1]]
            smile += info[x[i+1]][x[i]]
        smile += info[x[0]][x[-1]]
        smile += info[x[-1]][x[0]]
        happinesses.append(smile)
    happinesses.sort()
    return happinesses[-1]



# Compiling the input
info = {}
for line in lines:
    inf = readLines(line)
    if inf[0] not in info:
        info[inf[0]] = {}
    info[inf[0]][inf[1]] = inf[2]


# Getting and printing the happiest possible combination's value
print("The greatest total change in happiness is", getHappiest(info))
