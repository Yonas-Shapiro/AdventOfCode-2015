with open("Inputs\Day23.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Processing the lines:
def readLine(input):
    vals = input.replace(",", '').split(" ")
    return vals


# Running a command
def runCommand(command, num, vals):
    if command[0] == "hlf":
        vals[command[1]] /= 2
        return num+1
    elif command[0] == "tpl":
        vals[command[1]] *= 3
        return num+1
    elif command[0] == "inc":
        vals[command[1]] += 1
        return num+1
    elif command[0] == "jmp":
        return num + int(command[1])
    elif command[0] == "jie":
        if vals[command[1]] % 2 == 0: return num + int(command[2])
        else: return num + 1
    elif command[0] == "jio":
        if vals[command[1]] == 1: return num + int(command[2])
        else: return num + 1
    print(command)
    return -1



# Initializing the variables:
vals = {"a":0, "b":0}
commands = []
for line in lines:
    commands.append(readLine(line))


# Running the commands until it exits
run = 1
while run > 0 and run <= len(commands):
    run = runCommand(commands[run-1], run, vals)


# Printing out the result
print("The final value in register b is", str(vals["b"]) + ".")