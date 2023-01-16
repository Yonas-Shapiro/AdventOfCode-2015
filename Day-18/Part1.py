# GAME OF LIFE!!!!!!!!!!!!!
with open("Inputs\Day18.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Running one round
def round(grid):
    next = []
    for i in range(len(grid)):
        temp  = ""
        for j in range(len(grid[i])):
            count = 0
            up = i > 0
            down = i < len(grid)-1
            left = j > 0
            right = j < len(grid[i])-1
            if up:
                if left:
                    if grid[i-1][j-1] == "#": count += 1
                if grid[i-1][j] == "#": count += 1 
                if right:
                    if grid[i-1][j+1] == "#": count += 1
            if right:
                if grid[i][j+1] == "#": count += 1
            if left:
                if grid[i][j-1] == "#": count += 1
            if down:
                if left:
                    if grid[i+1][j-1] == "#": count += 1
                if grid[i+1][j] == "#": count += 1
                if right:
                    if grid[i+1][j+1] == "#": count += 1
            if grid[i][j] == "." and count == 3: temp += "#"
            elif grid[i][j] == "#" and (count == 2 or count == 3): temp += "#"
            else: temp += "."
        next.append(temp)
    return next


# Running for 100 rounds
for i in range(100):
    lines = round(lines)


# Getting the final count
num = 0
for i in lines:
    for j in i:
        if j == "#": num += 1


# Printing out the final result
print("After 100 rounds,", num, "lights are on.")