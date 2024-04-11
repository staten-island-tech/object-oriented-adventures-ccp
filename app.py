import json
import os
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
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
        print(f"Hello, {name}")
        print("Your goal is simple.")
        print("You have to defeat all of the cooking ingrients of a cookie and rescue the CCP.")
        print("But first, stat selection")
        menu_location="stat_creation"
        x=character_data(10, 10, 10, 10, 10, 10)
        while menu_location=="stat_creation":
            print(f"attack: {x.attack}")
            print(f"defense: {x.defense}")
            print(f"health: {x.health}")
            print(f"rizz: {x.rizz}")
            print(f"attack: {x.attack}")
            print(f"attack: {x.attack}")
except:
    print("ERROR!!!!")