import json
import os
from characterandenemy import characterdata
from actionyoucantake import actionchoice
## Open the JSON file of movie data
## create variable "data" that represents the enitre movie list
playerstatpoint=60
player_choice="none"
with open("json/inventory.json", "r") as f:
    data=json.load(f)
def compare(z):
    global playerstatpoint
    add_minus=int(input("How much point do you want to spend?: "))
    os.system('cls')
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
def leveldetermine(characterstat):
    while characterstat.exp>=characterstat.level*characterstat.level*characterstat.level:
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
        elif player_choice=="7" and playerstatpoint==0:
            break
        else:
            print("You can't do that")
            e=input("")
        os.system('cls')
def testing():
    menu_location="starting"
    while True:
        print("The story of the MSG King")
        print("1. Start game")
        print("2. End game")
        player_choice=input("input: ")
        os.system('cls')
        if player_choice=="1":
            name=input("What's your name: ")
            os.system('cls')
        elif player_choice=="2":
            print("Thank for playing this very amazing game about the CCP")
            quit()
        else:
            print("Achievement Unlocked <<|The Special One|>>")
        print(f"Hello, {name}")
        print("Your goal is simple.")
        print("You have to defeat all of the enemies and rescue the CCP.")
        print("But first, stat selection")
        x=characterdata(10, 10, 10, 10, 10, 10, 0, (0.15, 0.35, 0.5), ('a', 'b', 'c'), name, 1, 0, 1, 1)
        menu_location="stat_creation"
        while menu_location=="stat_creation":
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
            elif player_choice=="7" and playerstatpoint==0:
                menu_location="Game_start"
            else:
                print("You can't do that")
                e=input("")
            os.system('cls')
        while True:
            leveldetermine(x)
            playerstatpoint_selection(x)
            actionchoice.choice(x, x.weight_chance, x.enemyencounter, data)
testing()
""" except:
    if not player_choice == "2":
        print("ERROR!!!!")
    if not player_choice=="2":
        print("<<|Achievement Unlocked: Stop breaking intendly|>>") """