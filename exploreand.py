import random
step_counter=0
total_step=0
weight_chance=(0.5, 0.3, 0.15, 0.05)
enemyencounter=("none", 0, 1, 2)
def walking():
    global step_counter, total_step
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
while True:
    walking()