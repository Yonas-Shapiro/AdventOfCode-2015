import hashlib

with open("Inputs\Day4.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    code = lines[0]
    q.close()


# Checking if the number meets the requirements
def checkVal(num):
    # Creating a new string with the potential number
    val = code + str(num)

    # Getting the hash value and setting it to a hex-value
    hashval = hashlib.md5(val.encode())
    encoded = hashval.hexdigest()

    # Seeing if it meets the requirements and returning the appropriate value
    if encoded[:5] == "00000":
        print(encoded)
        return False
    return True


counter = 0
searching = True


# Running through numbers to find the lowest that meets the requirements
while searching:
    counter += 1
    searching = checkVal(counter)
    


print("The lowest number to output 5 zeroes at the start is", counter)