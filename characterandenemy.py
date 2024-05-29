class enemy():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense 
class characterdata(enemy):
    def __init__(self, attack, defense, health, rizz, score_mutipler, intellgence, total_step, weight_chance, enemyencounter, name, worldtype):
        super().__init__(name, health, attack, defense)
        self.rizz=rizz
        self.score_mutipler=score_mutipler
        self.intellgence=intellgence
        self.total_step=total_step
        self.weight_chance=weight_chance
        self.enemyencounter=enemyencounter
        self.name=name
        self.worldtype=worldtype
    def __str__(self):
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}, {self.total_step}, {self.weight_chance}, {self.enemyencounter}, {self.name}"
    def enemytypestat(worldtype, typenumber):
        if typenumber=="Boss":
            if worldtype=="4":
                Boss_Gordon_Ramsey=enemy("Gordon Ramsey", 200, 999, 30)
            elif worldtype=="3":
                Boss_Uncle_Roger=enemy("Uncle Roger", 150, 999, 25)
            elif worldtype=="2":
                Boss_Jamal=enemy("Jamal")