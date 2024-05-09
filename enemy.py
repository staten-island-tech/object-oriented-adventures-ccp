class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset
    enemy_template = enemy("name", 200, 200, ["drops"], ["moveset"])

    Gordon_Ramsey = enemy("Gordan Ramsey", 200, 10, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich"])
    ##boss
    Uncle_Roger = enemy("Uncle Roger", 150, 8, "MSG", ["MSG", "FUI YOHH", "AI YA"])
    ##boss

    Homecook = enemy("Homecook", 20, 5, ["Pepper", "Salt"] ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])

    NormieChef = enemy("Chef", 50, 10, ["Eggs", "Tomatoes", "Bell Pepper"], ["moveset"])

    ProChef = enemy("Advanced Chef", 200, 200, "drops", ["moveset"])
enemy()