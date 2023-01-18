with open("Inputs\Day11.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()
    line = lines[0]


# Password requirements:

# Must contain at least three consecutive letters.
# Must NOT contain "i", "o", or "l"
# Must contain at least two different non-overlapping pairs of letters

# Checking the requirement
def checkRequirements(input):
    # i, o, l requirement
    for i in input:
        if i in ["i", "o", "l"]:
            return False
    
    # Double letter requirement
    count = 0
    watch = -1
    for i in range(0, len(input)-1):
        if input[i] == input[i+1] and i != watch:
            watch = i+1
            count += 1
            if count == 2:
                break
    if count < 2:
        return False

    # Checking three in a row
    for i in range(0, len(input)-2):
        if ord(input[i]) == ord(input[i+1])-1 == ord(input[i+2])-2:
            return True

    return False


# Finding the next string in line
def nextString(last):
    # If the last letter isn't a 'Z', then no wrap-around is required
    if last[-1] != "z":
        return (last[:-1] + chr(ord(last[-1])+1))

    # Otherwise, check what the new string is after all of the wrap-arounding
    output = "a"
    x = 2
    while last[-x] == "z":
        output += "a"
        x += 1

    return (last[:-x] + chr(ord(last[-x])+1) + output)


# Finding the next available password
def findNextPassword(prev):
    found = False

    while not found:
        # Getting the next potential password
        prev = nextString(prev)
        # Checking its eligibility
        found = checkRequirements(prev)

    return prev


print("The next password should be", findNextPassword(line))