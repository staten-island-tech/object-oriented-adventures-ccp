import json
import os
from characterandenemy import characterdata
from actionyoucantake import actionchoice
import time
## Open the JSON file of movie data
## create variable "data" that represents the enitre movie list
playerstatpoint=100
player_choice="none"
with open("json/inventory.json", "r") as f:
    data=json.load(f)
class itsclassingtime():
    def compare(z):
        global playerstatpoint
        add_minus=input("How much point do you want to spend?: ")
        if not add_minus[0]=="-":
            for i in add_minus:
                if i.isnumeric():
                    allnumber=True
                else:
                    allnumber=False
                    break
        else:
            print(add_minus[0:1])
            for i in add_minus[1:]:
                if i.isnumeric():
                    allnumber=True
                else:
                    allnumber=False
                    break
        os.system('cls')
        if allnumber==True:
            add_minus=int(add_minus)
            if add_minus <= playerstatpoint and add_minus >=1:
                z+=add_minus
                playerstatpoint-=add_minus
                return z
            elif abs(add_minus) <= z-1 and add_minus<=0:
                z+=add_minus
                playerstatpoint-=add_minus
                return z
            else:
                print("Try again")
                return z 
        else:
            print("You can't do that")
            return z
    def leveldetermine(characterstat):
        while characterstat.exp>=characterstat.level*characterstat.level:
            characterstat.level+=1
            global playerstatpoint
            playerstatpoint+=1
    def playerstatpoint_selection(x):
        global playerstatpoint
        while playerstatpoint >=1:
            print(f"Point to spend: {playerstatpoint}")
            print(f"1. attack: {x.attack}")
            print(f"2. defense: {x.defense}")
            print(f"3. health: {x.health}")
            print(f"4. rizz: {x.rizz}")
            print(f"5. Coin mutipler: {x.score_mutipler}")
            print(f"6. Barter: {x.intellgence}")
            print("7. Countine the game")
            player_choice=input("Select the stat you want to change: ")
            os.system('cls')
            if player_choice=="1":
                x.attack=itsclassingtime.compare(x.attack)
            elif player_choice=="2":
                x.defense=itsclassingtime.compare(x.defense)
            elif player_choice=="3":
                x.health=itsclassingtime.compare(x.health)
            elif player_choice=="4":
                x.rizz=itsclassingtime.compare(x.rizz)
            elif player_choice=="5":
                x.score_mutipler=itsclassingtime.compare(x.score_mutipler)
            elif player_choice=="6":
                x.intellgence=itsclassingtime.compare(x.intellgence)
            elif player_choice=="7" and playerstatpoint==0:
                break
            else:
                print("You can't do that")
listformenulocation=["start"]
def testing():
    while listformenulocation[0]=="start":  
        print("The story of the MSG King")
        print("1. Start game")
        print("2. End game")
        player_choice=input("input: ")
        os.system('cls')
        while player_choice=="1":
            name=input("What's your name: ")
            os.system('cls')
            if not name.strip():
                print("Try again")
            else:
                print("This will be a turn-based game")
                time.sleep(1)
                print("You will venture through various restaurants, challenging each chef to a 'cookoff'")
                time.sleep(1)
                print("You have 4 actions that you can do when you're in battle")
                time.sleep(1)
                print("1 - Attack - Certain items can be used for dealing damage")
                time.sleep(1)
                print("2 - Rizz - You relive your life as a past gambler, but instead of hitting the jackpot, you're just trying to charm anyone you meet. Your base rizz is 1%, every point you put into rizz will incease it by 0.1%. When you successfully 'rizzed' your person of choice, you will avoid the battle.")
                time.sleep(2)
                print("3 - Run Away - You run away obviously")
                time.sleep(1)
                print("4 - Use Item - Use any item you currently have")
                time.sleep(1)
                print("There are 3 types of items you can acquire.")
                time.sleep(1)
                print("You can gain healing, buffs, or attack items")
                time.sleep(1)
                print("You can go to the shop to buy all of these items")
                time.sleep(3)
                listformenulocation[0]="stat_creation"
                break
        if player_choice=="2":
            print("Thank for playing this very amazing game about the CCP")
            quit()
        elif not player_choice=="1":
            print("You can't do that")
    print(f"Hello, {name}")
    print("Your goal is simple.")
    print("You have to defeat all of the enemies and rescue the CCP.")
    print("But first, stat selection")
    x=characterdata(10, 10, 10, 10, 10, 10, 0, (0.15, 0.35, 0.5), ('a', 'b', 'c'), name, 1, 0, 1, 1)
    while listformenulocation[0]=="stat_creation":
        print(f"Point to spend: {playerstatpoint}")
        print(f"1. attack: {x.attack}")
        print(f"2. defense: {x.defense}")
        print(f"3. health: {x.health}")
        print(f"4. rizz: {x.rizz}")
        print(f"5. Coin mutipler: {x.score_mutipler}")
        print(f"6. Barter: {x.intellgence}")
        print("7. Start the game")
        player_choice=input("Select the stat you want to change: ")
        os.system('cls')
        if player_choice=="1":
            x.attack=itsclassingtime.compare(x.attack)
        elif player_choice=="2":
            x.defense=itsclassingtime.compare(x.defense)
        elif player_choice=="3":
            x.health=itsclassingtime.compare(x.health)
        elif player_choice=="4":
            x.rizz=itsclassingtime.compare(x.rizz)
        elif player_choice=="5":
            x.score_mutipler=itsclassingtime.compare(x.score_mutipler)
        elif player_choice=="6":
            x.intellgence=itsclassingtime.compare(x.intellgence)
        elif player_choice=="7" and playerstatpoint==0:
            listformenulocation[0]="Game_start"
        else:
            print("You can't do that")
            print("<<|Achievement Unlocked: Thoughout Heaven and Earth, I Alone am the Special One |>>")
    while True:
        if x.worldtype==5:
            print("YOU WIN and became a good cook")
            quit()
        itsclassingtime.leveldetermine(x)
        itsclassingtime.playerstatpoint_selection(x)
        actionchoice.choice(x, x.weight_chance, x.enemyencounter, data)
testing()
""" except:
    if not player_choice == "2":
        print("ERROR!!!!")
        print("<<|Achievement Unlocked: Stop breaking intendly|>>")
    else:
        print("good idea") """