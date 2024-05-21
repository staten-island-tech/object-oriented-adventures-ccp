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
def enemytype(e):
    Boss_Gordon_Ramsey = enemy("Gordan Ramsey", 200, 999, 1000000, ["ITS RAWWWWWWW!!!!!", "IDIOT SANDWICH!!!!!", "YOU DONKEYYY!!!!"])
    
    Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, 1000000000, ["MSG", "FUIII YOHHHH", "AI YAAA", "YOU STUPID BOYY"])

    Boss_Jamal = enemy("Jamal", 100, 50, 100, 
    ['''Tsamina mina, eh, eh\n Waka waka, eh, eh\n Tsamina mina zangalewa,\n This time for Africa'''])

    Homecook = enemy("Homecook", 20, 5, 5, ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

    NormieChef = enemy("Chef", 50, 10, 30, ["I'm putting my blood, sweat, and tears into this 9-5 for minimum wage."])

    JamaicanChef = enemy("Jamaican Chef", 50, 10, 20, ["Wagwann bossman"])

    ProChef = enemy("Advanced Chef", 75, 20, 100, ["moveset"])

    if e == "1":
        return Boss_Gordon_Ramsey
    elif e == "2":
        return Boss_Uncle_Roger
    elif e =="3":
        return Boss_Jamal
    elif e == "4":
        return Homecook
    elif e == "5":
        return NormieChef
    elif e == "6":
        return JamaicanChef
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
                print(x.name,x.health)
                break
            elif player == "3":
                x.health += 10 - e.attack
            elif player == "4":
                z = random.randint(1,20)
                if z >= 15:
                    print("You have successfully rizzed up",e.name)
                    break
                else:
                    print("Rizz failed due to too little rizz you ugly")
                    x.health -= e.attack * 2
        else:
            if x.health > e.health:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you won!!")
            else:
                print(x.name,x.health)
                print(e.name,e.health)
                print("you lose!!")

class walking():
    def walk():
        player = input("Press 1 to walk: ")
        if player == "1":
            combat.combating(x, enemytype(random.choices(['1', '2','3','4','5','6'], (0.1,0.1,0.1,0.3,0.2,0.2))))
        else:
            print("<<|Achievement Unlocked: The Special One|>>")
while True:
    walking.walk()

