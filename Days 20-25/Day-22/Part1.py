with open("Inputs\Day22.txt", 'r') as q:
    lines = q.read().strip().split("\n")
    q.close()


# Getting the boss' information
def getInfo(input):
    temp = input[0].split(" ")
    health = int(temp[-1])
    temp = input[1].split(" ")
    damage = int(temp[-1])
    return {"Health":health, "Damage":damage}


# Finding out the shortest 




# Turning the infomation into variables
boss = getInfo(lines)
player = {"Health":50, "Mana":500, "Damage":{"val":0, "count":0}, "Armor":{"val":0, "count":0}, "Heal":{"val":0, "count":0}, "Recharge":{"val":0, "count":0}}
spells = {53:{"Damage":4}, 73:{"Damage":2, "Heal":2}, 113:{"Armor":7}, 173:{"Damage":3}, 229:{"Recharge":101}}
