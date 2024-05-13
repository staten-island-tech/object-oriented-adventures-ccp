import random
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
class action():
    def walking(x):
        x.total_step+=1
        encounter=random.choices(x.enemyencounter, x.weight_chance)
        if not isinstance(encounter, int):
            if x.step_counter==10:
                while not isinstance(encounter, int):
                    encounter=random.choices(x.enemyencounter, x.weight_chance)
            else:
                x.step_counter+=1
        else:
            print(encounter)
            print(x.step_counter)
            print(x.total_step)
x=characterdata(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
action.walking(x)