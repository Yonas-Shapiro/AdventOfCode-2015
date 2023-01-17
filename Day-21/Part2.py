import itertools

with open("Inputs\Day21.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


def readLines(input):
    vals = input.split(" ")
    vals = [x for x in vals if x not in  [" ", ""]]
    if vals[0] in ["Weapons:", "Armor:", "Rings:"]:
        type = vals[0][:-1]
        return type
    if len(vals) ==  4:
      return [vals[1], vals[2], vals[3]]
    return [vals[2], vals[3], vals[4]]


# Finding the most expensive way to lose
def findExpensive(items, player, boss):
  # Initializing the "cheapest" variable
  expensive = 0
  
  # Running through the possible combinations
  for a in items["Weapons"]:
    # If the price is cheaper than the most expensive, add more
    if a > expensive:
      player["Armor"] = 0
      player["Damage"] = items["Weapons"][a]["Damage"]

      # Simulating the fight
      if not simFight(boss.copy(), player.copy()): expensive = a; print(a)

    # Getting armour
    for b in items["Armor"]:
      # If the price is already more than the cheapest, continue
      if a+b > expensive:

        # Adding to the player's stats
        player["Damage"] = items["Weapons"][a]["Damage"]
        player["Armor"] = items["Armor"][b]["Armor"]
        
        # Simulating the fight
        if not simFight(boss.copy(), player.copy()): expensive = a+b; print(a, b)

      # Checking with 1 ring
      for c in items["Rings"]:
        if a+b+c > expensive:
          player["Damage"] = items["Weapons"][a]["Damage"] + items["Rings"][c]["Damage"]
          player["Armor"] = items["Armor"][b]["Armor"] + items["Rings"][c]["Armor"]
          if not simFight(boss.copy(), player.copy()): expensive = a+b+c; print(a, b, c)

        # Checking a potential second ring
        for d in items["Rings"]:
          if c == d: continue
          if a+b+c+d < expensive: continue
          player["Damage"] = items["Weapons"][a]["Damage"] + items["Rings"][c]["Damage"] + items["Rings"][d]["Damage"]
          player["Armor"] = items["Armor"][b]["Armor"] + items["Rings"][c]["Armor"] + items["Rings"][d]["Armor"]
          if not simFight(boss.copy(), player.copy()): expensive = a+b+c+d; print(a, b, c, d)
        
        
      
  
  return expensive


# Simulating a battle
def simFight(boss, player):
  myTurn = True
  if player["Damage"] <= boss["Armor"]: return False
  while player["Health"] > 0 and boss["Health"] > 0:
    if myTurn:
      boss["Health"] -= player["Damage"] - boss["Armor"]
      myTurn = False
    else:
      player["Health"] -= boss["Damage"] - player["Armor"]
      myTurn = True
  # Returning whether the player won or not
  if player["Health"] <= 0: return False
  else: return True

  
# Compiling the information
items = {}
boss = {}
me = {"Health":100, "Damage":0, "Armor":0}
equipment = ""
for line in lines:
    if line == "INFO:":
        break
    if line == "":
        continue
    output = readLines(line)
    if type(output) is str:
        equipment = output
        items[output] = {}
    else:
        items[equipment][int(output[0])] = {"Damage":int(output[1]), "Armor":int(output[2])}
for i in range(-3, 0):
    temp = lines[i].replace(":", "").split(" ")
    if "Health" not in boss:
        boss["Health"] = int(temp[-1])
    else:
        boss[temp[0]] = int((temp[-1]))

# Adding a "no armour" option
items["Armor"][0] = {"Damage":0, "Armor":0}


# Printing out the answer
print("The greatest amount of gold a player can spend and still lose to the boss is", findExpensive(items, me, boss), "gold coins.")