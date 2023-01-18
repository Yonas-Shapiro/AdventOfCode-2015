import math

with open("Inputs\Day20.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    line = int(lines[0])
    q.close()


# Finding all of the factors of a number
def factorsSum(num):
    factors = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0: 
            factors.append(i)
            factors.append(int(num/i))
    num = sum(factors)
    return num


# Finding the lowest number that meets the requirements
def calculateLowestNum(num):
    house = 1
    while True:
        if factorsSum(house) >= num/10:
            return house
        house += 1
        

# Printing out the lowest number
print("The lowest house number to recieve", line, "gifts is house number", calculateLowestNum(line))