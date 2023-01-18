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
                # If the sum of the group is equal to 1/4 of the total, find a combination for the other boxes
                available = [x for x in boxes if x not in group]
                for j in range(1, len(boxes)-len(group)):
                    temp1 = len(least)
                    for g2 in itertools.combinations(available, j):
                        sum = 0
                        for y in g2: sum += y
                        if sum == val:
                            temp2 = len(least)
                            available2 = [x for x in boxes if x not in g2]
                            for l in range(len(boxes)-len(g2)-1):
                                temp3 = len(least)
                                for g3 in itertools.combinations(available2, l):
                                    sum = 0
                                    for z in g3: sum += z
                                    if sum == val: least.add(group); break
                                if len(least) > temp3: break
                            if len(least) > temp2: break
                    if len(least) > temp1: break
        if len(least) > 0: break

    # Finding the lowest quantum number
    quantumNumbers = []
    for x in least:
        mult = 1
        for i in x:
            mult *= i
        quantumNumbers.append(mult)
    print(least)
    quantumNumbers.sort()
    return quantumNumbers[0]


# Known variables
boxes = [int(x) for x in lines]
boxes.sort(reverse=True)
sum = int(sum(boxes)/4)
print(sum)


# Printing out the smallest number of gifts with the smallest quantum entanglement number
print("The ideal configuration has a quantum entanglement of", balancing(boxes, sum))