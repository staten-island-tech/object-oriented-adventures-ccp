import random
class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset

Boss_Gordon_Ramsey = enemy("Gordan Ramsey", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
#Gordon final boss in restrauant(restrauant is biome/level) Hell's Kitchen

Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
['''Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa
This time for Africa'''])

Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

ProChef = enemy("Advanced Chef", 75, 20, "drops", ["moveset"])

class character():
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
x = character(200, 20, 20)
def enemytype(y):
    Boss_Gordon_Ramsey = enemy("Gordan Ramsey", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
    
    Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

    Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
    ['''Tsamina mina, eh, eh, Waka waka, eh, eh, Tsamina mina zangalewa, This time for Africa'''])

    Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

    NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

    ProChef = enemy("Advanced Chef", 75, 20, "drops", ["moveset"])

    if y == "1":
        return Boss_Gordon_Ramsey
    elif y == "2":
        return Boss_Uncle_Roger
    elif y =="3":
class combat():
    def combating(x, e):
        while x.health > 0 and e.health > 0:
            print(x.health)
            print(e.health)
            player = input("1. Attack\n2. defense\n3.heal")
            if player == "1":
                e.health -= x.attack
                x.health -= e.attack
            elif player == "2":
                x.health -= e.attack / 2
            else:
                x.health += 10 - e.attack
        else:
            print(x.health)
            print(e.health)
            print("You won!!!!")
class walking():
    def walk():
        player = input("Press 1 to walk: ")
        if player == "1":
            combat.combating(x, enemytype(random.choices(['1', '2'], (0.1, 0.9))))
        else:
            print("<<|Achievement Unlocked: The Special One|>>")
while True:
    walking.walk()

