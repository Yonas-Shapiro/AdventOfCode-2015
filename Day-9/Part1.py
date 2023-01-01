with open("Inputs\Day9.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def readLines(input, places):
    addVal = 0
    start, x, end, eq, length = input.split(" ")
    if start in places:
        index = places.index(start)
        #print(index)
    else:
        #print("Test")
        index = len(places)
        addVal = 1
    if end in places:
        endI = places.index(end)
    else:
        endI = len(places) + addVal
    return [index, endI, int(length), start, end]


def getRoutes(lst, depth, input, checked = []):
    
    if depth == len(lst):
        return input
    
    next = []
    result = []
    checked.append(-1)

    if depth == 0:
        depth += 1
        for i in range(len(lst)):
            next.append(0)
            result += [getRoutes(lst, depth, 0, [i])]
        print(result, "TEST")
        result.sort()
        #print(result)
        return result[0]


    for i in range(len(lst)):
        depth += 1
        if i in checked:
            continue
        checked[-1] = i
        next.append(int(input + lst[checked[-2]][checked[-1]]))
        print(next[-1], "NEXT\n")
        result += [getRoutes(lst, depth, next[-1], checked)]
    
    print("UMMMMMMMM")
    #depth += 1
    print(depth, checked, "CHECKED\n\n")
    #result += (getRoutes(lst, depth, j, checked) for j in next)
    print(result)
    return result
    
    


# Gathering the necessary information
info = []
places = []        
for line in lines:
    # Get back the necessary inputs
    vals = readLines(line, places)

    # Add the place names to the places array if it isn't already there
    if vals[0]+1 > len(places):
        places.append(vals[3])
        info.append([])
    if vals[1]+1 > len(places):
        places.append(vals[4])
        info.append([])
    
    # Helps make the grid (Can't go from one spot to the same spot)
    if len(info[vals[0]]) == vals[0]:
        info[vals[0]].append("N/A")
    elif len(info[vals[1]]) == vals[1]:
        info[vals[1]].append("N/A")
    
    # Add the distances
    info[vals[0]].append(vals[2])
    info[vals[1]].append(vals[2])



#print(info)
#print(len(info))        

#getRoutes(info, 0, 0)    
    


distance = getRoutes(info, 0, 0)
print("The shortest route is", distance)