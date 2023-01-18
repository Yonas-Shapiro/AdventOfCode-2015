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


def splitAndCheck(input, depth):
    for i in range(len(input)):
        if input[i] == 






# Getting all of the numbers from the input
def getNums(input):
    # Initializing the output array
    output = []

    # Going through the input
    upto = -1
    watch = 0
    red = 0
    temp = []
    for i in range(len(input)):
        # Making sure not to duplicate any numbers
        if i <= upto:
            continue
        # Seeing if in an object
        if input[i] == "{":
            watch += 1
        elif input[i] == "}":
            print(watch, red)
            print(temp)
            if not red:
                
                for i in temp:
                    output.append(temp.pop())
            else:
                for i in temp:
                    temp.pop()
            watch -= 1
            red -= 1
        
        if watch and input[i:i+3] == "red" and i < len(input)-2:
            red = True
        # Ensuring all digits are accounted for
        if checkIfInt(input[i]):
            upto = i
            while checkIfInt(input[upto]):
                upto += 1
            out = int(input[i:upto])

            # Checking if the number is negative
            if i > 0 and input[i-1] == "-":
                out *= -1
            temp.append(out)
        if watch == False:
            for i in temp:
                output.append(temp.pop())
    return output








print("The total sum is", sum(getNums(line)))