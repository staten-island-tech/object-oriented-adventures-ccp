import random
import json
import math
with open("json/weapon.json", "r") as f:
    weaponstat=json.load(f)
with open("json/armorstat.json", "r") as f:
    armorstat=json.load(f)
with open("json/itemstatuseffect.json", "r") as f:
    itemstatuseffect=json.load(f)
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
class combat():
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
        elif e== "6":
            return ProChef
    def damagedealcal(attack, inventory):
        return attack*weaponstat[0][inventory[2]["Weapon"]]
    def damagetakencalcaltor(enemy_attack, inventory):
        x=[armorstat[0][inventory[2][i]] for i in inventory[2] if not i =="Weapon" if not inventory[2][i]=="none"]
        y=sum(x)
        return math.ceil(enemy_attack/y)
    def combating(x, e, inventory):
        while x.health > 0 and e.health > 0:
            print(x.name, x.health)
            print(e.name, e.health)
            player = input("1. Attack\n2. Retreat\n3. Use item\n5. Rizz\n")
            if player == "1":
                e.health -= combat.damagedealcal(x.attack)
                x.health -= combat.damagetakencalcaltor(e.attack)
            elif player == "2":
                x.health -= combat.damagetakencalcaltor(e.attack)*5
                print(x.name,x.health)
                break
            elif player == "3":
                number_selection=0
                for items in inventory[0]:
                    if inventory[0][items]>0:
                        number_selection+=1
                        print(f"{number_selection}, {items}: {inventory[0][items]}")
                if number_selection==0:
                    print("You have nothing")
                print(f"{number_selection+1}, Exit")
                listofitemuseable=[i for i in inventory[0] if inventory[0][i]>0]
                player_choice=input("What do you want to do?")
                if int(player_choice)<=number_selection:
                    pass
                else:
                    pass
            elif player == "4":
                z = random.randint(1,20)
                if z >= 15:
                    print("You have successfully rizzed up",e.name)
                    break
                else:
                    print("Rizz failed due to too little rizz you ugly")
                    x.health -= combat.damagetakencalcaltor(e.attack)*10
        else:
            if x.health > e.health:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you won!!")
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")