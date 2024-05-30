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
            if worldtype=="4":
                Boss_Gordon_Ramsey=enemy("Gordon Ramsey", 200, 999, 1000, ["ITS RAW!!","IDOT SANDWITCH", "YOU donkey"])
            elif worldtype=="3":
                Boss_Uncle_Roger=enemy("Uncle Roger", 150, 999, 1500, ["MSG", "FUI YOH!!", "AIYA", "You a Failure"])
            elif worldtype=="2":
                Boss_Jamal=enemy("Jamal", 100, 999, 1, ["Tsamina mina, eh, eh\n Waka waka, eh, eh\n Tsamina mina zangalewa,\n This time for Africa"])
            else:
                pan_cheng=enemy("Pan Cheng", 50, 999, 40000)
        if typenumber=="Weak":
            if worldtype=="1":
                Homecook = enemy("Homecook", 20, 5, 100, ["Struggle Meal Ramen", "Microwaved Cheese Sandwich", "Burnt Fire Alarm"])
            elif worldtype=="2":
                NormieChef = enemy("Chef", 50, 10, 200, ["I'm putting my blood, sweat, and tears into this 9-5 for minimum wage"])
            elif worldtype=="3":
                JamaicanChef = enemy("Jamaican Chef", 50, 10, 230, ["Wagwann bossman"])
            elif worldtype=="4":
                ProChef = enemy("Advanced Chef", 75, 20, 500, ["I am Pro Chef"])