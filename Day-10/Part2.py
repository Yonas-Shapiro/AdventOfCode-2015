with open("Inputs\Day10.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    line = lines[0]
    q.close()


# Perfrom the "Look-and-Say" sequence
def las(line):
    # Initializing variables
    output = ""
    i = 0
    count = 1
    val = ""

    # Running through each character
    for i in range(len(line)):
        char = line[i]
        if i == 0:
            val = line[0]
        else:
            # If the character is the same as the previous character, continue the count
            if line[i] == val:
                count += 1
            # If not, then stop the count, record the count and the character
            else:
                output += str(count) + val
                count = 1
                val = line[i]
    # To ensure the final value is logged
    output += str(count) + val
    return output
        

for i in range(50):
    line = las(line)

print("The length of the final look-and-say is", len(line))