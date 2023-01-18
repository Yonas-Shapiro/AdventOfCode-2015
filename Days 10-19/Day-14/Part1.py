with open("Inputs\Day14.txt", 'r') as q:
  lines = q.read().strip().split("\n")
  q.close()


# Reading the lines
def readLines(input):
  commands = input.split(" ")
  name = commands[0]
  dist = int(commands[3])
  t1 = int(commands[6])
  t2 = int(commands[13])
  return [dist, t1, t2, name]


# Returning the distance each reindeer goes
def getDist(vals):
  time = 0
  val = 0
  while time < 2503:
    if time+vals[1] < 2503:
      val += vals[0]*vals[1]
      time += vals[1]
      time += vals[2]
    else:
      val += (2503-time) * vals[0]
      time = 2503
  print(val, vals[3])
  return val


# Gathering the info
info = []
for line in lines:
  info.append(readLines(line))


# Finding the longest distance travelled
nums = []
for deer in info:
  nums.append(getDist(deer))
nums.sort()
print("The fastest reindeer has gone", nums[-1], "kilometres.")