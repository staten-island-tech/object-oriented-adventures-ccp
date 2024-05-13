class characterdata():
    def __init__(self, attack, defense, health, rizz, score_mutipler, intellgence, step_counter, total_step, weight_chance, enemyencounter):
        self.attack=attack
        self.defense=defense
        self.health=health
        self.rizz=rizz
        self.score_mutipler=score_mutipler
        self.intellgence=intellgence
        self.step_counter=step_counter
        self.total_step=total_step
        self.weight_chance=weight_chance
        self.enemyencounter=enemyencounter
    def __str__(self):
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}, {self.step_counter}, {self.total_step}, {self.weight_chance}, {self.enemyencounter}"