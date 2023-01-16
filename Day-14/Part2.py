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
  return [dist, t1, t2, name, 0, 0, True]


# Finding the leader at the end of each second
def findLeader(deer):
  global info
  
  leaders = []
  score = 0

  for i in range(len(deer)):
    if deer[i][6]:
      info[i][4] += deer[i][0]
      info[i][5] += 1
      if deer[i][5] == deer[i][1]:
        info[i][6] = False
        info[i][5] = 0
    else:
      info[i][5] += 1
      if info[i][5] == deer[i][2]:
        info[i][6] = True
        info[i][5] = 0
    if info[i][4] > score:
        leaders = [deer[i][3]]
        score = info[i][4]
    elif info[i][4] == score:
      leaders.append(deer[i][3])
  return leaders


# Gathering the info
info = []
for line in lines:
  info.append(readLines(line))


# Initializing the scores dict
scores = {}
for i in info:
  scores[i[3]] = 0


# Tallying the points
for j in range(2503):
  leaders = findLeader(info)
  for i in leaders:
    scores[i] += 1


# Printing out the winner
points = list(scores.values())
points.sort()
print("The highest scoring reindeer got a score of", points[-1])