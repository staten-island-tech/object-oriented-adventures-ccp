import json
import os
## Open the JSON file of movie data
movies = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
playerstatpoint=60
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
try:
    data = json.load(movies)
    game_life=100
    menu_location="starting"
    while game_life>=1:
        print("TITLE!!!!!!")
        print("1. Start game")
        print("2. End game")
        player_choice=input("input: ")
        os.system('cls')
        if player_choice=="1":
            name=input("What's your name: ")
        if player_choice=="2":
            print("Thank for playing this very azamzing game about the CCP")
            quit()
        print(f"Uncle |'King of MSG'| Roger: Hello, {name}")
        print("Your goal is simple.")
        print("You have to defeat all of the top chefs in each restaurant.")
        ##Restaurant is a Stage/Level
        print("How? Defeat other cooks, gather recipes and ingredients, until you can duel the masterchef with your newfound knowledge.")
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
    if not player_choice=="2":
        print("Achievement Unlocked: The Special One")