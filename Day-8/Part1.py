with open("Inputs\Day8.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def readLine(input):
    # The string literal length
    literal = len(input)

    # Finding the memory chars
    input = input[:-1]
    input = input[1:]
    
    # Running through each character
    i = 0
    while i < len(input):
        # If it is a "\", check what the following character is
        if input[i] == "\\":
            # If it is an "x", then it is a four letter code
            if input[i+1] == "x":
                for j in range(3):
                    input = input[:i] + input[i+1:]
            # Otherwise, it is 2 characters
            else:
                input = input[:i] + input[i+1:]
            input = input[:i] + "?" + input[i+1:]
        else:
            i += 1

    # Returning the values
    return [literal, len(input)]


# Solving the problem by running through each line
total = 0
for line in lines:
    plus, minus = readLine(line)
    total += plus-minus


print("The answer is", total)