import random
import json
from action import actionchoice
with open("json/weapon.json", "r") as f:
    weaponstat=json.load(f)
with open("json/armorstat.json", "r") as f:
    armorstat=json.load(f)
with open("json/inventory.json", "r") as f:
    inventory=json.load(f)
class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset

class character():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
x = character("Sigma Rizzler", 200, 20, 20)
def enemytype(e):
    Boss_Gordon_Ramsey = enemy("Gordan Ramsey", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
    
    Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

    Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
    ['''Tsamina mina, eh, eh\n Waka waka, eh, eh\n Tsamina mina zangalewa,\n This time for Africa'''])

    Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

    NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

    ProChef = enemy("Advanced Chef", 75, 20, "drops", ["moveset"])

    if e == "1":
        return Boss_Gordon_Ramsey
    elif e == "2":
        return Boss_Uncle_Roger
    elif e =="3":
        return Boss_Jamal
    elif e == "4":
        return Homecook
    elif e == "5":
        return NormieChef
    else:
        return ProChef

class combat():
    def defensedisplay(armordefstat, inventory):
        defense=0
        for i in inventory[2]:
            if not i =="Weapon":
                defense+=armordefstat[0][inventory[2][i]]
        return defense
    def damageatakingcalculation(enemyattack, armordefstat, inventory):
        return enemyattack/combat.defensedisplay(armordefstat, inventory)
    def combating(x, e, data):
        while x.health > 0 and e.health > 0:
            print(x.name, x.health)
            print(e.name, e.health)
            player = input("1. Attack\n2. Retreat\n3. Eat\n4. Use item\n5. Rizz\n")
            if player == "1":
                e.health -= x.attack*weaponstat[0][data[2]['Weapon']]
                x.health -= e.attack
            elif player == "2":
                x.health -= e.attack / 2
                print(x.name,x.health)
                break
            elif player == "3":
                x.health += 10 - e.attack
            elif player == "4":
                z = random.randint(1,20)
                if z >= 15:
                    print("You have successfully rizzed up",e.name)
                    break
                else:
                    print("Rizz failed due to too little rizz you ugly")
                    x.health -= e.attack * 2
        else:
            if x.health > e.health:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you won!!")
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")

""" class walking():
    def walk():
        player = input("Press 1 to walk: ")
        if player == "1":
            combat.combating(x, enemytype(random.choices(['1', '2','3','4','5','6'], (0.1,0.1,0.1,0.3,0.2,0.2))))
        else:
            print("<<|Achievement Unlocked: The Special One|>>") """
print(combat.damageatakingcalculation(20, armorstat, inventory))