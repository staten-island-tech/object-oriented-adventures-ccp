import json
import os

class typeenemy():
    def __init__(self, name, health, damage, moveset):
        self.name = name
        self.health = health
        self.damage = damage
        self.moveset = moveset

class chef(typeenemy):
    def __init__(self, name, health, damage, moveset, drops):
        super().__init__(name, health, damage, moveset)
        self.drops = drops
    def __str__(self):
        return f"{self.name}, {self.health}, {self.damage}, {self.moveset}, {self.drops}"
    
achievements = [{"The Special One"}, {"Good Ending"}, ["Rizz Ending"]]

with open("enemy.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    enemy = json.load(f)
    ##Call classes in here








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