with open("Inputs\Day21.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def readLines(input):
    vals = input.split(" ")
    vals = [x for x in vals if x not in  [" ", ""]]
    if vals[0] in ["Weapons:", "Armor:", "Rings:"]:
        type = vals[0][:-1]
        return type
    return [vals[1], vals[2], vals[3]]


items = {}
stats = {}
equipment = ""
for line in lines:
    if line == "INFO:":
        break
    if line == "":
        continue
    output = readLines(line)
    if type(output) is str:
        equipment = output
        items[output] = {}
    else:
        items[equipment][int(output[0])] = {"Damage":int(output[1]), "Armour":int(output[2])}
for i in range(-3, 0):
    temp = lines[i].replace(":", "").split(" ")
    if "HP" not in stats:
        stats["HP"] = int(temp[-1])
    else:
        stats[temp[0]] = (temp[-1])

print(stats)
print(items)