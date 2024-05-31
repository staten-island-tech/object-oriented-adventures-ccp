class enemy():
    def __init__(self, name, health, attack, coins):
        self.name = name
        self.health = health
        self.attack = attack
        self.coins = coins
class characterdata(enemy):
    def __init__(self, attack, defense, health, rizz, score_mutipler, intellgence, total_step, weight_chance, enemyencounter, name):
        super().__init__(name, health, attack)
        self.defense=defense
        self.rizz=rizz
        self.score_mutipler=score_mutipler
        self.intellgence=intellgence
        self.total_step=total_step
        self.weight_chance=weight_chance
        self.enemyencounter=enemyencounter
        self.name=name
    def __str__(self):
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}, {self.total_step}, {self.weight_chance}, {self.enemyencounter}, {self.name}"
    def enemytypestat(worldtype, typenumber):
        if typenumber=="Boss":
            if worldtype==3:
                Boss_Gordon_Ramsey=enemy("Gordon Ramsey", 100000, 999, 1750, ["ITS RAW!!","IDOT SANDWITCH", "YOU donkey"])
            elif worldtype==4:
                Boss_Pan_Cheng = enemy("Pan Cheng", 200000, 1000, 2000, ["Ohh be quiet", "sign out shut down", "close your chromebook"])
            elif worldtype==1:
                Boss_Uncle_Roger=enemy("Uncle Roger", 20000, 999, 1500, ["MSG", "FUI YOH!!", "AIYA", "You a Failure"])
            elif worldtype==2:
                Boss_Jamal=enemy("Jamal", 75000, 999, 1, ["Tsamina mina, eh, eh\n Waka waka, eh, eh\n Tsamina mina zangalewa,\n This time for Africa"])
        elif typenumber=="a":
            if worldtype==1:
                Homecook = enemy("Homecook", 20, 5, 100, ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])
            elif worldtype==2:
                NormieChef = enemy("Chef", 50, 10, 200, ["I'm putting my blood, sweat, and tears into this 9-5 for minimum wage"])
            elif worldtype==3:
                JamaicanChef = enemy("Jamaican Chef", 70, 15, 230, ["Wagwann bossman"])
            elif worldtype==4:
                ProChef = enemy("Advanced Chef", 75, 20, 500, ["I am Pro Chef"])
        elif typenumber=="b":
            if worldtype == 1:
                NoobChef = enemy("Noob Chef", 50, 20, 125)
            elif worldtype == 2:
                ThreeStarChef = enemy("3 Star Chef", 70, 25, 250)
            elif worldtype == 3:
                JamalJr = enemy("Jamal Jr.", 100, 30, 300)
            elif worldtype == 4:
                FiveStarChef = enemy("5 Star Chef", 100, 30, 400)
        elif typenumber =="c":
            if worldtype == 1:
                ChinaChef = enemy("Chinese Chef", 70, 30, 150)
            elif worldtype ==2:
                FourStarChef = enemy("4.99999 Star Chef", 100, 40, 300)
            elif worldtype ==3:
                LebronJames = enemy("Lebron James", 150, 50, 350)
            elif worldtype ==4:
                MasterChef = enemy("Master Chef", 200, 100, 600)