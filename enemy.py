import json
import os

class typeenemy():
    def __init__(self, name, health, attack, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.moveset = moveset

class ingredient(typeenemy):
    def __init__(self, name, health, attack, moveset, drops):
        super().__init__(name, health, attack, moveset)
        self.drops = drops
    def __str__(self):
        return f"{self.name}, {self.health}, {self.attack}, {self.moveset}, {self.drops}"
    

with open("enemy.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    enemy = json.load(f)
    ##Call classes in here

while True:
    name = input("Name of enemy: ")
    health = input(int("health of enemy: "))
    attack = input(int("Attack power: "))
    moveset = input("moveset: ")
    drops = input("drops: ")
    newenemy = ingredient(name, health, attack, moveset, drops)
    enemy.append(newenemy.__dict__)
    addanotherenemy = input("Do you want to add another character? Y/N: ")
    if addanotherenemy.upper() != "Y":
        break

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(enemy)

    #"Write the JSON string to the new JSON file"

    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("enemy.json")
os.rename(new_file, "enemy.json")