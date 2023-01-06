with open("Sample.txt", 'r') as q:
#with open("Inputs\Day13.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def makeGrid(input, people):
    addVal = 0
    p1, a, pm, val, hap, u, b, s, n, t, p2 = input.split(" ")
    p2 = p2[:-1]
    if p1 in people:
        index = people.index(p1)
    else:
        index = len(people)
        addVal = 1
    if p2 in people:
        p2Index = people.index(p2)
    else:
        p2Index = len(people) + addVal
    val = int(val)
    if pm == "lose":
        val *= -1
    return [index, p2Index, val, p1, p2]    


info = []
people = []
for line in lines:
    vals = makeGrid(line, people)

    if vals[0]+1 > len(people):
        people.append(vals[3])
        info.append([])
    if vals[1]+1 > len(people):
        people.append(vals[4])
        info.append([])
    
    if len(info[vals[0]]) == vals[0]:
        info[vals[0]].append(0)
    elif len(info[vals[1]]) == vals[1]:
        info[vals[1]].append(0)
    

    try:
        info[vals[0]][vals[1]] += vals[2]
        info[vals[1]][vals[0]] += vals[2]
    except:
        info[vals[0]].append(vals[2])
        info[vals[1]].append(vals[2])

for i in info:
    print(i)


def getDistances(lst, checked = []):
    print(checked)
    if len(checked) == len(lst):
        return [lst[checked[-1]][checked[-2]]]
    
    result = []
    myChecked = checked + [-1]
    for i in range(len(lst)):
        if i in myChecked:
            continue
        myChecked[-1] = i
        temp = getDistances(lst, myChecked)
        for j in temp:
            if len(myChecked) > 1:
                result += [j + lst[myChecked[-2]][myChecked[-1]]]
                print(myChecked)
            else:
                result += [j]

    print(result)
    return result


result = getDistances(info)
#print(result)
print(max(result))