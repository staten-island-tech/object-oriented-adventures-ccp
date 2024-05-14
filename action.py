import random
import os
from Thestuffthattrackyourstuff import whatyouhave 
class actionchoice():
    def walking(distance_cover_total, weighted, enemytype):
            distance_cover_total+=1
            if distance_cover_total==100:
                print("boss")
            else:
                encounter=random.choices(enemytype, weighted)
                print(encounter, distance_cover_total)
    def choice(distance_cover_total, weighted, enemytype):
        player_choice=input("1. Walk\n2. Open inventory")
        if player_choice=="1":
            actionchoice.walking(distance_cover_total, weighted, enemytype)
        if player_choice=="2":
            whatyouhave.equidingstuff()