import hashlib

with open("Inputs\Day4.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    code = lines[0]



def checkVal(num):
    val = code + str(num)
    hashval = hashlib.md5(val.encode())
    encoded = hashval.hexdigest()
    if encoded[:6] == "000000":
        print(encoded)
        return False
    return True


counter = 0
searching = True

while searching:
    counter += 1
    searching = checkVal(counter)
    


print("The lowest number to output 6 zeroes at the start is", counter)