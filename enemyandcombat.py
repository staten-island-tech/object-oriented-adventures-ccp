import random
import json
import math
import os
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
    def damagedealcal(attack, inventory, buff_amount):
        if not inventory[2]["Weapon"]=="none":
            return math.ceil(attack*weaponstat[0][inventory[2]["Weapon"]]*buff_amount)
        else:
            return math.ceil(attack)
#This calculate the amount of damage you take    
    def damagetakencalcaltor(enemy_attack, inventory, x):
        z=[armorstat[0][inventory[2][i]] for i in inventory[2] if not i =="Weapon" if not inventory[2][i]=="none"]
        y=sum(z)
        if y>0:
            return math.ceil(enemy_attack/(y*x))
        else:
            return enemy_attack/x
#This combine everything to make a working combat system
    def combating(x, e, inventory):
        buff_amount=1
        maxhealth=x.health
        while x.health > 0 and e.health > 0:
            print(x.name, x.health)
            print(e.name, e.health)
            player = input("1. Attack\n2. Retreat\n3. Use item\n4. Rizz")
            os.system('cls')
            if player == "1":
                e.health -= combat.damagedealcal(x.attack, inventory, buff_amount)
                x.health -= combat.damagetakencalcaltor(e.attack, inventory, x.defense)
            elif player == "2":
                x.health -= combat.damagetakencalcaltor(e.attack, inventory, x.defense)*5
                if random.choice((1, 2))==1:
                    print("Haha, YOU FAIL")
                else:
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
                os.system('cls')
                if int(player_choice)<=number_selection:    
                    for i in itemstatuseffect:
                        for j in i:
                            for y in itemstatuseffect[0][j]:
                                if y == listofitemuseable[int(player_choice)-1]:
                                    if j == 'healing':
                                        if x.health+itemstatuseffect[0][j][y]<=maxhealth:
                                            x.health+=itemstatuseffect[0][j][y]
                                            inventory[0][listofitemuseable[int(player_choice)-1]]-=1
                                        else:
                                            x.health=maxhealth
                                    elif j == 'attack':
                                        e.health-=itemstatuseffect[0][j][y]
                                        inventory[0][listofitemuseable[int(player_choice)-1]]-=1
                                    else:
                                        buff_amount+=itemstatuseffect[0][j][y]
                                        inventory[0][listofitemuseable[int(player_choice)-1]]-=1
                else:
                    pass
            elif player == "4":
                if x.rizz >= random.randint(1,1000):
                    print("You have successfully rizzed up",e.name)
                    break
                else:
                    print("Rizz failed due to too little rizz you ugly")
                    x.health -= combat.damagetakencalcaltor(e.attack, inventory, x.defense)*3
        else:
            if x.health > 0 and e.health <=0:
                print(x.name,x.health)
                print(e.name,e.health)
                print(f"{x.exp}+{e.exp}/{x.level*x.level*x.level} exp")
                x.exp+=e.exp
                print(f"Coin: {inventory[4]['coin']}+{e.coin*x.score_mutipler}")
                inventory[4]['coin']+=(e.coin*x.score_mutipler)
                print("you won!!")
                x.health=maxhealth
                player=input("")    
                os.system('cls')
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")
                quit()