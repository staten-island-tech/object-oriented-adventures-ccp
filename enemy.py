enemies = []

class enemy():
    def __init__(self, name, health, attack, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.moveset = moveset

class ingredient(enemy):
    def __init__(self, health, attack, moveset, drops):
        super().__init__(health, attack, moveset)
        self.drops = drops
    def __str__(self):
        return f"{self.name}, {self.health}, {self.attack}"

