from enemy import enemytype
class restaurants():
    def __init__(self, name, boss, enemies):
        self.name = name
        self.boss = boss
        self.enemies = enemies

enemytype()

restaurants_template = restaurants('name', 'boss', ['enemys'])

Hells_Kitchen = restaurants('Hells Kitchen', Boss_Gordon_Ramsay , [ProChef])

MSG_Munch = restaurants("MSG Munch", Boss_Uncle_Roger, [Homecook])

Flavor_Town = restaurants("Flavor Town", Boss_Guy_Fieri, [NormieChef, ProChef])

Jamaica_Fried_Chicken = restaurants("Jamaica Fried Chicken", Boss_Jamal, [NormieChef, JamaicanChef])

