import itertools

with open("Inputs\Day17.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Finding the number of combinations
def findCombinations(lst):
    num = 0
    lst = [int(x) for x in lst]
    for i in range(len(lst)):
        for subset in itertools.combinations(lst, i):
            if sum(subset) == 150: num += 1
    return num


# Getting the answer and printing it out
combinations = findCombinations(lines)
print("There are", combinations, "different combinations to fit exactly 150 litres of eggnog.")