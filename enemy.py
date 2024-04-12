enemies = []

class enemy():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class ingredient(enemy):
    def __init__(self, health, attack, drops):
        super().__init__(health, attack)
        self.drops = drops
    def __str__(self):
        return f"{self.name}, {self.health}, {self.attack}"