class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset

Gordon_Ramsey = enemy("Gordan Ramsey", 200, 10, "Supreme Beef Wellington", ["ITS RAW!!", "Idiot Sandwich"])

Uncle_Roger = enemy("Uncle Roger", 150, 8, "MSG", ["MSG", "FUI YOHH", "AI YA"])

def attack():
    