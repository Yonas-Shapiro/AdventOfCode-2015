with open("Inputs\Day8.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def readLine(input):
    # Getting the original length
    original = len(input)
    new = len(input)
    
    # Running through each character to see if a "\" needs to proceed it in the result.
    for i in input:
        if i == "\\":
            new += 1
        elif i == "\"":
            new += 1

    # Adding the quotation marks at the start and end
    new += 2

    return [new, original]


# Solving the problem by running through each line
total = 0
for line in lines:
    plus, minus = readLine(line)
    total += plus-minus


print("The answer is", total)