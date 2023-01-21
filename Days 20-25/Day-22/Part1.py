import itertools

with open("Inputs\Day22.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Getting the boss' information
def getInfo(input):
    temp = input[0].split(" ")
    health = int(temp[-1])
    temp = input[1].split(" ")
    damage = int(temp[-1])
    return [health, damage]


# Taking a turn
def runTurn(playerTurn, spells, info, spellCast = "N/A"):
    global blacklist
    armour = 0
    if spells["s"][6] > 0: 
        armour = 7
        spells["s"][6] -= 1
    if spells["p"][6] > 0:
        info["bossHP"] -= 3
        spells["p"][6] -= 1
    if spells["r"][6] > 0:
        info["mana"] += 101
        spells["r"][6] -= 1
    # If passive damage wins, return the win
    if info["bossHP"] < 1: return True


    # Player turn
    if playerTurn:
        # Doing the stuff
        info["mana"] -= spells[spellCast][0]
        if info["mana"] < 0:
            return False
        if spellCast == "m": info["bossHP"] -= 3
        elif spellCast == "d": info["health"] += 2; info["bossHP"] -= 2
        else:
            # Can't call a spell while it is still running
            if spells[spellCast][6] > 0:
                return False
            spells[spellCast][6] = spells[spellCast][5]

        # No errors, return True
        return True
    else:
        # Boss attacks
        damage = info["bossD"] - armour
        if damage < 1: damage = 1
        info["health"] -= damage
        return True
  
  
# Simulating a battle
def battle(spells, boss, order):
    global blacklist
    info = {"health":50, "mana":500, "bossHP":boss[0], "bossD":boss[1], "manaUsed":0}
    pTurn = True
    cont = True
    num = 0
    
    # Taking turns while both combatants are still alive
    while info["health"] > 0 and info["bossHP"] > 0 and cont:
        if pTurn:
            if num >= len(order): return False
            cont = runTurn(pTurn, spells, info, order[num])
            num += 1
        else: 
            cont = runTurn(pTurn, spells, info)
        pTurn = not pTurn


    # Printing whether the battle was a success
    if cont == False: blacklist.add(order); return False
    if info["health"] > 0: return True
    else: return False


# Running through the possibilities: (Terribly inefficient, but it works)
def runPossibilities(spells, boss, spellNames):
    cheapest = 10000
    num = 1
    global blacklist
    while num < 12:
        for combo in itertools.product(spellNames, repeat=num):
            if combo.count("m")*4 + combo.count("p")*18 + combo.count("d")*2 < boss[0]: continue
            cont = False
            for i in blacklist:
                if combo[:len(i)] == i:
                    cont = True
                    break
            if cont: continue
            manas = [spells[x][0] for x in combo]
            if sum(manas) > cheapest: continue
            if battle(spells.copy(), boss, combo): return(sum(manas))
            if cheapest <= len(combo)*53: return cheapest
        num += 1
    return 0

        
# Turning the infomation into variables
boss = getInfo(lines)
# Cost, damage, armour, heal, added mana, turns active, turns left
spells = {"m":[53, 4, 0, 0, 0, 0, 0], "d":[73, 2, 0, 2, 0, 0, 0], "s":[113, 0, 7, 0, 0, 7, 0], "p":[173, 3, 0, 0, 0, 6, 0], "r":[229, 0, 0, 0, 101, 6, 0]}
spellNames = ("m", "d", "s", "p", "r")
blacklist = set()


print("The least amount of mana that can be used to defeat the boss is", runPossibilities(spells, boss, spellNames))
