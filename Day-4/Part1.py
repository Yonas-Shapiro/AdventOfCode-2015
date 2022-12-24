import hashlib

with open("Inputs\Day4.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    code = lines[0]
    q.close()



def checkVal(num):
    val = code + str(num)
    hashval = hashlib.md5(val.encode())
    encoded = hashval.hexdigest()
    if encoded[:5] == "00000":
        print(encoded)
        return False
    return True


counter = 0
searching = True

while searching:
    counter += 1
    searching = checkVal(counter)
    


print("The lowest number to output 5 zeroes at the start is", counter)