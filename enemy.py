class enemy():
    def __init__(self, name, health, attack, drops, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.drops = drops
        self.moveset = moveset

class boss(enemy):
    def __init__(self, name, health, attack, drops, moveset):
        super().__init__(name, health, attack, drops, moveset)
    def __str__(self):
        return f"{self.name}, {self.health}, {self.attack}, {self.drops}, {self.moveset}"