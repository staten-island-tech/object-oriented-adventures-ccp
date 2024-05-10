import random
step_counter=0
total_step=0
weight_chance=(0.5, 0.3, 0.15, 0.05)
enemyencounter=("none", 0, 1, 2)
class actionwalking():
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
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}, {self}"
    def walking():
        total_step+=1
        encounter=random.choices(enemyencounter, weight_chance)
        if not isinstance(encounter, int):
            if step_counter==10:
                while not isinstance(encounter, int):
                    encounter=random.choices(enemyencounter, weight_chance)
            else:
                step_counter+=1
        else:
            print(encounter)
            print(step_counter)
            print(total_step)