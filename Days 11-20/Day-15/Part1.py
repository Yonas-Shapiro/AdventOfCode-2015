with open("Inputs\Day15.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Reading the lines
def readLine(input):
    vals = input.replace(",", "").split(" ")
    cap = int(vals[2])
    dur = int(vals[4])
    flav = int(vals[6])
    text = int(vals[8])
    cals = int(vals[10])

    # Returning as a dict
    return {"capacity":cap, "durability":dur, "flavour":flav, "texture":text, "calories":cals}


# Calculating the best score
def getBestScore(info):
    scores = []

    # Running through each possibility
    for i in range(100):
        for j in range(100):
            if j + i > 100:
                break
            for k in range(100):
                if j + k + i > 100: 
                    break
                for l in range(100):
                    if j + k + l + i > 100:
                        break
                    elif j + k + l + i != 100:
                        continue

                    # Getting the scores
                    cap = info[0]["capacity"]*i + info[1]["capacity"]*j + info[2]["capacity"]*k + info[3]["capacity"]*l
                    dur = info[0]["durability"]*i + info[1]["durability"]*j + info[2]["durability"]*k + info[3]["durability"]*l
                    flav = info[0]["flavour"]*i + info[1]["flavour"]*j + info[2]["flavour"]*k + info[3]["flavour"]*l
                    text = info[0]["texture"]*i + info[1]["texture"]*j + info[2]["texture"]*k + info[3]["texture"]*l
                    if cap < 1 or dur < 1 or flav < 1 or text < 1: break
                    scores.append(cap*dur*flav*text)

    # Finding the highest score and returning it
    scores.sort()
    return scores[-1]


# Processing the input
info = []
for line in lines:
    info.append(readLine(line))


# Getting the best score and printing it out
score = getBestScore(info)
print("The highest possible score is", score)