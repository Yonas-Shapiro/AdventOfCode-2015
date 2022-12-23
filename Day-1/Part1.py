with open("Day 1\input.txt", "r") as q:
    lines = q.read().strip().split("\n")
    command = lines[0]
    q.close()

floor = 0

for i in command:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
    else:
        print("Error")
        


print("Final location is floor", floor)