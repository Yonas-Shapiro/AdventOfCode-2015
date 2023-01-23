# Preface: copied then rewritten to learn from u/SebastianLague on Reddit
from copy import deepcopy
from sys import maxsize


# Getting the info from the input
with open("Inputs\Day22.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()

def getInfo(input):
    temp = input[0].split(" ")
    health = int(temp[-1])
    temp = input[1].split(" ")
    damage = int(temp[-1])
    return [health, damage]

boss = getInfo(lines)


# Spells info
# Cost, Damage, Heal, Armour, Refill, Turns, Index
missile = (53, 4, 0, 0, 0, 0 ,0)
drain = (73, 2, 2, 0, 0, 0, 1)
shield = (113, 0, 0, 7, 0, 6, 2)
poison = (173, 3, 0, 0, 0, 6, 3)
recharge = (229, 0, 0, 0, 101, 5, 4)
spells = [missile, drain, shield, poison, recharge]
leastMana = maxsize


# Running the fight (simulating until fastest found)
def main():
    sim(boss[0], 50, 500, [], True, 0)
    print("The least amount of mana that can be used to defeat the boss is", leastMana)


# The simulation of the fight
def sim(bossHP, myHP, myMana, activeSpells, playerTurn, manaUsed):
    global boss
    bossDmg = boss[1]
    myArmour = 0
    
    newActiveSpells = []
    # Running through the active spells and applying the effects
    for activeSpell in activeSpells:
        if activeSpell[5] >= 0:
            bossHP -= activeSpell[1]
            myHP += activeSpell[2]
            myArmour += activeSpell[3]
            myMana += activeSpell[4]

        # If the spell continues on the next turn, add it into newActiveSpells
        newActiveSpell = (activeSpell[0], activeSpell[1], activeSpell[2], activeSpell[3], activeSpell[4], activeSpell[5]-1, activeSpell[6])
        if newActiveSpell[5] > 0:
            newActiveSpells.append(newActiveSpell)

        
    # If the boss is dead, return True (win) and see if less mana has been used
    if bossHP <= 0:
        global leastMana
        if manaUsed < leastMana: leastMana = manaUsed
        return True

    # If the mana used is already over the least amount used, return False
    if manaUsed >= leastMana: return False

    # Running through the possibilities if it is a player's turn
    if playerTurn:
        for spell in spells:
            spellActive = False
            for activeSpell in newActiveSpells:
                if activeSpell[6] == spell[6]:
                    spellActive = True
                    break
            
            spellManaCost = spell[0]
            if spellManaCost <= myMana and not spellActive:
                a = deepcopy(newActiveSpells)
                a.append(spell)
                sim(bossHP, myHP, myMana - spellManaCost, a, False, manaUsed+spellManaCost)

    # If it is the boss's turn
    else:
        myHP += myArmour-bossDmg if myArmour-bossDmg < 0 else -1
        if myHP > 0:
            sim(bossHP,myHP,myMana,newActiveSpells, True,manaUsed)

main()