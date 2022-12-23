with open("Day 1\input.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    command = lines[0]
    q.close()

floor = 0
character = 0

for i in command:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
    else:
        print("Error")
    character += 1
    if floor < 0:
        break
        


print("Santa first enters the basement at character", character)