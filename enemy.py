import random
class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset

class character():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
x = character("Sigma Rizzler", 200, 20, 20)
def enemytype(y):
    Boss_Gordon_Ramsey = enemy("Gordan Ramsey", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
    
    Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

    Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
    ['''Tsamina mina, eh, eh\n Waka waka, eh, eh\n Tsamina mina zangalewa,\n This time for Africa'''])

    Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

    NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

    ProChef = enemy("Advanced Chef", 75, 20, "drops", ["moveset"])

    if y == "1":
        return Boss_Gordon_Ramsey
    elif y == "2":
        return Boss_Uncle_Roger
    elif y =="3":
        return Boss_Jamal
    elif y == "4":
        return Homecook
    elif y == "5":
        return NormieChef
    else:
        return ProChef

class combat():
    def combating(x, e):
        while x.health > 0 and e.health > 0:
            print(x.name, x.health)
            print(e.name, e.health)
            player = input("1. Attack\n2. Retreat\n3. Eat\n4. Rizz: ")
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
            combat.combating(x, enemytype(random.choices(['1', '2','3','4','5','6'], (0.05,0.05,0.5,0.1,0.1,0.2))))
        else:
            print("<<|Achievement Unlocked: The Special One|>>")
while True:
    walking.walk()

