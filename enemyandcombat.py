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
#This is the combat system
class combat():
#This calculate the amount of damage your enemy take    
    def damagedealcal(attack, inventory, buff_amount, defenseofenemy):
        return (attack*weaponstat[0][inventory[2]["Weapon"]]*buff_amount)/defenseofenemy
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
                e.health -= combat.damagedealcal(x.attack, inventory, buff_amount, e.defense)
                x.health -= combat.damagetakencalcaltor(e.attack, inventory)
            elif player == "2":
                x.health -= combat.damagetakencalcaltor(e.attack, inventory)*5
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
                    x.health -= combat.damagetakencalcaltor(e.attack, inventory)*3
        else:
            if x.health > 0 and e.health <=0:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you won!!")
                
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")