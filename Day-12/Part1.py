with open("Inputs\Day12.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()
    line = lines[0]


# Seeing if a character is an integer
def checkIfInt(char):
    try:
        x = int(char)
        return True
    except:
        return False


# Getting all of the numbers from the input
def getNums(input):
    # Initializing the output array
    output = []

    # Going through the input
    upto = -1
    for i in range(len(input)):
        # Making sure not to duplicate any numbers
        if i <= upto:
            continue
        
        # Ensuring all digits are accounted for
        if checkIfInt(input[i]):
            upto = i
            while checkIfInt(input[upto]):
                upto += 1
            out = int(input[i:upto])

            # Checking if the number is negative
            if i > 0 and input[i-1] == "-":
                out *= -1
            output.append(out)
    return output


print("The total sum is", sum(getNums(line)))