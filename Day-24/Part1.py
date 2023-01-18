import itertools

with open("Inputs\Day24.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Balancing
def balancing(boxes, val):
    least = set()
    # Running through all of the possibilities, from fewest number of boxes to the greatest
    for i in range(1, len(boxes)-1):
        for group in itertools.combinations(boxes, i):
            sum = 0
            for x in group: sum += x
            if sum == val:
                # If the sum of the group is 503, try to find a combination for the others
                available = [x for x in boxes if x not in group]
                for j in range(1, len(boxes)):
                    see = len(least)
                    for g2 in itertools.combinations(available, j):
                        sum = 0
                        for y in g2: sum += y
                        if sum == val: least.add(group); break
                    if len(least) > see: break
        if len(least) > 0: break

    # Finding the lowest quantum number
    quantumNumbers = []
    for x in least:
        mult = 1
        for i in x:
            mult *= i
        quantumNumbers.append(mult)
    quantumNumbers.sort()
    return quantumNumbers[0]


# Known variables
boxes = [int(x) for x in lines]
boxes.sort(reverse=True)
sum = int(sum(boxes)/3)


# Printing out the smallest number of gifts with the smallest quantum entanglement number
print("The ideal configuration has a quantum entanglement of", balancing(boxes, sum))