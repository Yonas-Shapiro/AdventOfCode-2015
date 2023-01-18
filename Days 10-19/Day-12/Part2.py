import json

with open("Inputs\Day12.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()
    line = lines[0]


# Recursing through the dicts and lists
def getVal(piece):
    num = 0
    try:
        if "red" in list(piece.values()): return 0
    except:
        pass
    for i in piece:
        try:
            x = int(i)
            num += x
        except:
            try:
                x = int(piece[i])
                num += x
            except:
                try:
                    if type(piece[i]) is dict:
                        num += getVal(piece[i])
                    elif type(piece[i]) is list:
                        num += getVal(piece[i])
                except:
                    if type(i) is dict:
                        num += getVal(i)
                    elif type(i) is list:
                        num += getVal(i)
    return num
                


# Turning the input into a dict
info = json.loads(line)


print("The total sum of valid numbers is", getVal(info))