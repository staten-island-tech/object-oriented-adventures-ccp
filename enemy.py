class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset


Boss_Gordon_Ramsay = enemy("Gordan Ramsay", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
#Gordon final boss in restrauant(restrauant is level) Hell's Kitchen

Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
['''Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa
This time for Africa'''])

Boss_Guy_Fieri = enemy("Guy Fieri", 200, 70, ["Celeb Scam Meal"])

Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

JamaicanNormieChef = enemy("Jamaican Chef", 50, 10, ["Oil", "Chicken", "Watermelon"], ["moveset"])

ProChef = enemy("Advanced Chef", 75, 20, "", ["moveset"])


