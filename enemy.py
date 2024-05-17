class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset


Boss_Gordon_Ramsay = enemy("Gordan Ramsay", 200, 999, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich", "YOU DONKEYYY!!"])
#Gordon final boss in restrauant(restrauant is biome/level) Hell's Kitchen

Boss_Uncle_Roger = enemy("Uncle Roger", 150, 999, "MSG", ["MSG", "FUI YOHH", "AI YA"])

Boss_Jamal = enemy("Jamal", 100, 50, ["Jerk Chicken", "Fried Chicken", "Watermelon", "Purple Kool-Aid"], 
['''Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa
This time for Africa'''])

Boss_Guy_Fieri = enemy("Guy Fieri", 200, 70, ["Celeb Scam Meal"])

Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"], ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

ProChef = enemy("Advanced Chef", 75, 20, "drops", ["moveset"])
class combatsystem():
    def using_item():
        print("olo")
    def combat(health, enemy_health, attack, enemy_attack):
        while health >= 0:
            while health>=1 and enemy_health>=1:
                player=input("")
                if player=="2":
                    combatsystem.using_item()
                health-=enemy_attack
                print(f"health: {health}")
                player=input("")
                enemy_health-=attack
                print(f"enemy: {enemy_health}")
combatsystem.combat(10, Boss_Gordon_Ramsey.health, 10, Boss_Gordon_Ramsey.attack)

