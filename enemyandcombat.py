import random
import json
import math
#This section loaded json stat
with open("json/weapon.json", "r") as f:
    weaponstat=json.load(f)
with open("json/armorstat.json", "r") as f:
    armorstat=json.load(f)
with open("json/itemstatuseffect.json", "r") as f:
    itemstatuseffect=json.load(f)
#This is the enemy templete
class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset
#This is the combat system
class combat():
#This determine what enemy you encounter and set the enemy stat
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
#This calculate the amount of damage your enemy take    
    def damagedealcal(attack, inventory, buff_amount):
        return attack*weaponstat[0][inventory[2]["Weapon"]]*buff_amount
#This calculate the amount of damage you take    
    def damagetakencalcaltor(enemy_attack, inventory):
        x=[armorstat[0][inventory[2][i]] for i in inventory[2] if not i =="Weapon" if not inventory[2][i]=="none"]
        y=sum(x)
        return math.ceil(enemy_attack/y)
#This combine everything to make a working combat system
    def combating(x, e, inventory):
        buff_amount=1
        while x.health > 0 and e.health > 0:
            print(x.name, x.health)
            print(e.name, e.health)
            player = input("1. Attack\n2. Retreat\n3. Use item\n4. Rizz")
            if player == "1":
                e.health -= combat.damagedealcal(x.attack, buff_amount)
                x.health -= combat.damagetakencalcaltor(e.attack)
            elif player == "2":
                x.health -= combat.damagetakencalcaltor(e.attack)*5
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
                for i in itemstatuseffect:
                    for x in i:
                        for y in itemstatuseffect[0][x]:
                            if y == listofitemuseable[int(player_choice)-1]:
                                if x == 'healing':
                                    x.health+=itemstatuseffect[0][x][y]
                                    pass
                                elif x == 'attack':
                                    e.health-=itemstatuseffect[0][x][y]
                                    pass
                                else:
                                    buff_amount+=itemstatuseffect[0][x][y]
                if int(player_choice)<=number_selection:
                    for i in itemstatuseffect:
                        print(i)
                else:
                    pass
            elif player == "4":
                z = random.randint(1,1000)
                if x.rizz >= random.randint:
                    print("You have successfully rizzed up",e.name)
                    break
                else:
                    print("Rizz failed due to too little rizz you ugly")
                    x.health -= combat.damagetakencalcaltor(e.attack)*3
        else:
            if x.health > e.health:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you won!!")
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")