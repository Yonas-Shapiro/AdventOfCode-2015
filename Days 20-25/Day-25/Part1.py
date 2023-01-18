with open("Inputs\Day25.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()
    line = lines[0]


# Getting the next location
def getRow(prev):
  if prev > 0:
    return prev-1
  else:
    global grid
    grid.append([])
    return len(grid[0])

def findLocationVal(location):
  global grid
  next = 0
  val = 20151125
  while True:
    if len(grid) >= location[0] and len(grid[location[0]-1]) >= location[1]:
      return grid[location[0]-1][location[1]-1]
    next = getRow(next)
    val = (val*252533)%33554393
    grid[next].append(val)

    
# Getting the info
vals = line.replace(".", "").replace(",", "").split(" ")
location = [int(vals[-3]), int(vals[-1])]
grid = [[20151125]]


# Finding the value at the desired location
print("The value at row", str(location[0]) + ", column", location[1], "is", findLocationVal(location))