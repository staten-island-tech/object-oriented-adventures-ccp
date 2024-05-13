import random
class actionchoice():
    def walking(distance_cover_total, total_distance_without_enemy, weighted, enemytype):
        while True:
            player_choice=input()
            if distance_cover_total==100:
                return "boss"
            distance_cover_total+=1
            total_distance_without_enemy+=1
            encounter=random.choices(enemytype, weighted)
            while total_distance_without_enemy==10 and encounter=="none":
                encounter=encounter=random.choices(enemytype, weighted)
            else:
                total_distance_without_enemy=0
            if total_distance_without_enemy==10:
                total_distance_without_enemy=0
            print(encounter)
            print(distance_cover_total)
            print(total_distance_without_enemy)
actionchoice.walking(0, 0, (0.5, 0.3, 0.15, 0.05), ('none', 'a', 'b', 'c'))