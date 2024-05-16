from enemy import NormieChef, ProChef, Boss_Gordon_Ramsay, Boss_Jamal, Boss_Uncle_Roger, Boss_Guy_Fieri

class restaurants():
    def __init__(self, name, boss, enemies):
        self.name = name
        self.boss = boss
        self.enemies = enemies

restaurants_template = restaurants('name', 'boss', ['enemys'])

Hells_Kitchen = restaurants('Hells Kitchen', Boss_Gordon_Ramsay , [ProChef])

MSG_Munch = restaurants("MSG Munch", Boss_Uncle_Roger)

Flavor_Town = restaurants("Flavor Town", Boss_Guy_Fieri, [NormieChef, ProChef])

Jamaican_Fried_Chicken = restaurants("Jamaican Fried Chicken", Boss_Jamal, [NormieChef])