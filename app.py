import json
import os
import random
## Open the JSON file of movie data
## create variable "data" that represents the enitre movie list
playerstatpoint=60
menu_location="none"
player_choice="none"
#inventory system
inventory=[{'itemh1': 0, 
            'itemh2': 0,
            'itemh3': 0, 
            'itema1': 0, 
            'itema2': 0,
            'itema3': 0,
            'itemb1': 0, 
            'itemb2': 0,
            'itemb3': 0}, 
            {
            #sword, axe, spear, bow, helment, body armor, legging, boot
            'tier1eq': {'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'armorh': 1, 'armorba': 0, 'armorl': 0, 'armorb': 0}, 
            'tier2eq':{'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'armorh': 0, 'armorba': 0, 'armorl': 0, 'armorb': 0}, 
            'tier3eq':{'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'armorh': 0, 'armorba': 0, 'armorl': 0, 'armorb': 0}
            }, 
            #body armor equidment
            {
                'head': "none", 
                'body': "none", 
                'leg': "none", 
                'toe': "none", 
                'weapon': "sword1"
            }]
def inven():
    for i in inventory:
        for x in i:
            print(x, i[x])
def equidingstuff():
    for x in inventory[1]:
        for y in inventory[1][x]:
            if inventory[1][x][y]>=1:
                print(y, inventory[1][x][y])
    for x in inventory[2]:
        print(x, inventory[2][x])
    player_choice=input("What equidment do you want to equid?\n1.Helment\n2.Body armor\n3.Legging\n4.Boot\n5. Exit\n6. Weapon")
    os.system('cls')
    if player_choice=="1":
        print(f"1. leather helment: {inventory[1]['tier1eq']['armorh']}")
        print(f"2. copper helment: {inventory[1]['tier2eq']['armorh']}")
        print(f"3. iron helment: {inventory[1]['tier3eq']['armorh']}")
        print("4. Unequid")
        print("5. Exit")
        player_choice=input()
        os.system('cls')
        if player_choice == "1" or player_choice == "2" or player_choice == "3":
            if inventory[1][f'tier{player_choice}eq']['armorh']>=1 and inventory[2]['head']=="none":
                inventory[1][f'tier{player_choice}eq']['armorh']-=1
                inventory[2]['head']=player_choice
                print(inventory[1][f'tier{player_choice}eq']['armorh'])
                print(inventory[2]['head'])
            else:
               print("You can't do that") 
        elif player_choice == "4":
            if not inventory[2]['head']=="none":
                inventory[1][f'tier{inventory[2]["head"]}eq']['armorh']+=1
                print(inventory[1][f'tier{inventory[2]["head"]}eq']['armorh'])
                inventory[2]['head']="none"
                print(inventory[2]['head'])
            else:
               print("You can't do that") 
        else:
            pass
    elif player_choice=="2":
        print(f"1. body armor1: {inventory[1]['tier1eq']['armorba']}")
        print(f"2. body armor2: {inventory[1]['tier2eq']['armorba']}")
        print(f"3. body armor3: {inventory[1]['tier3eq']['armorba']}")
        print("4. Unequid")
        print("5. Exit")
        player_choice=input()
        os.system('cls')
        if player_choice == "1" or player_choice == "2" or player_choice == "3":
            if inventory[1][f'tier{player_choice}eq']['armorba']>=1 and inventory[2]['body']=="none":
                inventory[1][f'tier{player_choice}eq']['armorba']-=1
                inventory[2]['body']=player_choice
                print(inventory[1][f'tier{player_choice}eq']['armorba'])
                print(inventory[2]['body'])
            else:
               print("You can't do that") 
        elif player_choice == "4":
            if not inventory[2]['body']=="none":
                inventory[1][f'tier{inventory[2]["body"]}eq']['armorba']+=1
                print(inventory[1][f'tier{inventory[2]["body"]}eq']['armorba'])
                inventory[2]['body']="none"
                print(inventory[2]['body'])
            else:
               print("You can't do that") 
        else:
            pass
    elif player_choice=="3":
        print(f"1. legging1: {inventory[1]['tier1eq']['armorl']}")
        print(f"2. legging2: {inventory[1]['tier2eq']['armorl']}")
        print(f"3. legging3: {inventory[1]['tier3eq']['armorl']}")
        print("4. Unequid")
        print("5. Exit")
        player_choice=input()
        os.system('cls')
        if player_choice == "1" or player_choice == "2" or player_choice == "3":
            if inventory[1][f'tier{player_choice}eq']['armorl']>=1  and inventory[2]['leg']=="none":
                inventory[1][f'tier{player_choice}eq']['armorl']-=1
                inventory[2]['armorl']=player_choice
                print(inventory[1][f'tier{player_choice}eq']['armorl'])
                print(inventory[2]['leg'])
            else:
               print("You can't do that") 
        elif player_choice == "4":
            if not inventory[2]['leg']=="none":
                inventory[1][f'tier{inventory[2]["leg"]}eq']['armorl']+=1
                print(inventory[1][f'tier{inventory[2]["leg"]}eq']['armorl'])
                inventory[2]['leg']="none"
                print(inventory[2]['leg'])
            else:
               print("You can't do that") 
        else:
            pass
    elif player_choice=="4":
        print(f"1. boot1: {inventory[1]['tier1eq']['armorb']}")
        print(f"2. boot2: {inventory[1]['tier2eq']['armorb']}")
        print(f"3. boot3: {inventory[1]['tier3eq']['armorb']}")
        print("4. Unequid")
        print("5. Exit")
        player_choice=input()
        os.system('cls')
        if player_choice == "1" or player_choice == "2" or player_choice == "3" and inventory[2]['toe']=="none":
            if inventory[1][f'tier{player_choice}eq']['armorb']>=1 and inventory[2]['toe']=="none":
                inventory[1][f'tier{player_choice}eq']['armorb']-=1
                inventory[2]['toe']=player_choice
                print(inventory[1][f'tier{player_choice}eq']['armorb'])
                print(inventory[2]['toe'])
            else:
               print("You can't do that") 
        elif player_choice == "4":
            if not inventory[2]['toe']=="none":
                inventory[1][f'tier{inventory[2]["toe"]}eq']['armorb']+=1
                print(inventory[1][f'tier{inventory[2]["toe"]}eq']['armorb'])
                inventory[2]['toe']="none"
                print(inventory[2]['toe'])
            else:
               print("You can't do that") 
        else:
            pass
    elif player_choice=="5":
        global menu_location
        menu_location = "start"
    elif player_choice=="6":
        print("1. Sword")
        print("2. Axe")
        print("3. Spear")
        print("4. Bow")
        print("5. Exit")
        player_choice=input("")
        if player_choice=="1":
            for x in inventory[1]:
                print(inventory[1][x]['sword'])
            print(f"1. equid sword1\n2. equid sword2\n3. equid sword3\n4.unequid\n5.exit")
            player_choice=input("")
            if player_choice=="1" or player_choice=="2" or player_choice=="3":
                if inventory[1][int(player_choice)-1]['sword']>=0 and inventory[2]['weapon']=="none":
                    inventory[1][int(player_choice)-1]['sword']-=1
                    inventory[2]['weapon']="sword1"
            elif player_choice=="4" and not inventory[2]['weapon']=="none":
                def weaponcheck():
                    if "sword" in inventory[2]['weapon']:
                        
                    elif "axe" in inventory[2]['weapon']:
                    elif "spear" in inventory[2]['weapon']:
                    else:
                if "1" in inventory[2]['weapon']:
                        
    os.system('cls')
class character_data():
    def __init__(self, attack, defense, health, rizz, score_mutipler, intellgence):
        self.attack=attack
        self.defense=defense
        self.health=health
        self.rizz=rizz
        self.score_mutipler=score_mutipler
        self.intellgence=intellgence
    def __str__(self):
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}"
def compare(z):
    global playerstatpoint
    add_minus=int(input("How much point do you want to spend"))
    if add_minus <= playerstatpoint and add_minus >=1:
        z+=add_minus
        playerstatpoint-=add_minus
        return z
    elif abs(add_minus) <= z:
        z+=add_minus
        playerstatpoint-=add_minus
        return z
    else:
        print("Try again")
    player_choice="none"
while menu_location == "none":
    equidingstuff()
try:
    from enemy import enemy, ingredient
    level=1
    game_life=100
    menu_location="starting"
    while game_life>=1:
        print("TITLE!!!!!!")
        print("1. Start game")
        print("2. End game")
        print(player_choice)
        player_choice=input("input: ")
        os.system('cls')
        if player_choice=="1":
            name=input("What's your name: ")
        if player_choice=="2":
            print("Thank for playing this very azamzing game about the CCP")
            quit()
        print(f"Hello, {name}")
        print("Your goal is simple.")
        print("You have to defeat all of the cooking ingrients of a cookie and rescue the CCP.")
        print("But first, stat selection")
        menu_location="stat_creation"
        x=character_data(10, 10, 10, 10, 10, 10)
        while menu_location=="stat_creation":
            print(f"Point to spend: {playerstatpoint}")
            print(f"1. attack: {x.attack}")
            print(f"2. defense: {x.defense}")
            print(f"3. health: {x.health}")
            print(f"4. rizz: {x.rizz}")
            print(f"5. score mutipler: {x.score_mutipler}")
            print(f"6. intellgence: {x.intellgence}")
            player_choice=input("Select the stat you want to change.")
            os.system('cls')
            if player_choice=="1":
                x.attack=compare(x.attack)
            elif player_choice=="2":
                x.defense=compare(x.defense)
            elif player_choice=="3":
                x.health=compare(x.health)
            elif player_choice=="4":
                x.rizz=compare(x.rizz)
            elif player_choice=="5":
                x.score_mutipler=compare(x.score_mutipler)
            elif player_choice=="6":
                x.intellgence=compare(x.intellgence)
            elif playerstatpoint=="7":
                menu_location="Game_start"
            os.system('cls')
except:
    if not player_choice == "2":
        print("ERROR!!!!")
    if not player_choice=="2":
        print("<<|Achievement Unlocked: The Special One|>>")