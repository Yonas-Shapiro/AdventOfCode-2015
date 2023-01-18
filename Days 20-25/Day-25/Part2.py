with open("Inputs\Day25.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()
    line = lines[0]

# Getting the info
vals = line.replace(".", "").replace(",", "").split(" ")
location = [int(vals[-3]), int(vals[-1])]
print(location)