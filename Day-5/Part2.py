with open("Inputs\Day5.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def checkIfNice(val):
    cont = False
    
    for i in range(len(val)-3):
        start = val[i] + val[i+1]
        for j in range(i+2, len(val)-1):
            end = val[j] + val[j+1]
            if start == end:
                i = len(val)
                cont = True
                break
    if not cont:
        return 0
    
    for i in range(len(val)-2):
        if val[i] == val[i+2]:
            return 1
    
    return 0




count = 0


for val in lines:
    count += checkIfNice(val)


print(count, "strings are nice.")