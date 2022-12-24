with open("Inputs\Day5.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def checkIfNice(val):
    nos = ["ab", "cd", "pq", "xy"]
    vowels = ['a', 'e', 'i', 'o', 'u']
    vNum = 0
    
    for pair in nos:
        if pair in val:
            return 0
    
    for vowel in vowels:
        for char in val:
            if vowel == char:
                vNum += 1
    if vNum < 3:
        return 0

    for i in range(len(val)-1):
        if val[i] == val[i+1]:
            return 1

    return 0


count = 0


for val in lines:
    count += checkIfNice(val)


print(count, "strings are nice.")