import json
import os
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
try:
    data = json.load(movies)
    game_life=100
    menu_location="starting"
    while game_life>=1:
        if menu_location=="starting":
            print("TITLE!!!!!!")
            print("1. Start game")
            print("2. End game")
            player_choice=input("input: ")
        os.system('cls')
        if player_choice>=1:
            print("sad")
except:
    print("ERROR!!!!")