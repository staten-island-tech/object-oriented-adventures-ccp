class enemy():
    def __init__(self, name, health, attack, defense, coin, exp):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense 
        self.coin=coin
        self.exp=exp
class characterdata(enemy):
    def __init__(self, attack, defense, health, rizz, score_mutipler, intellgence, total_step, weight_chance, enemyencounter, name, worldtype, exp, coin, level):
        super().__init__(name, health, attack, defense, coin, exp)
        self.rizz=rizz
        self.score_mutipler=score_mutipler
        self.intellgence=intellgence
        self.total_step=total_step
        self.weight_chance=weight_chance
        self.enemyencounter=enemyencounter
        self.name=name
        self.worldtype=worldtype
        self.level=level
    def __str__(self):
        return f"{self.attack}, {self.defense}, {self.health}, {self.rizz}, {self.score_mutipler}, {self.intellgence}, {self.total_step}, {self.weight_chance}, {self.enemyencounter}, {self.name}"
    def enemytypestat(worldtype, typenumber):
        if typenumber=="Boss":
            if worldtype==3:
                Boss_Gordon_Ramsey=enemy("Gordon Ramsey", 100000, 50000, 1750, 480, 3000)
                return Boss_Gordon_Ramsey
            elif worldtype==4:
                Boss_Pan_Cheng = enemy("Pan Cheng", 200000, 75000, 2000, 600, 4500)
                return Boss_Pan_Cheng
            elif worldtype==1:
                Boss_Uncle_Roger=enemy("Uncle Roger", 20000, 10000, 1500, 240, 1000)
                return Boss_Uncle_Roger
            else:
                Boss_Jamal=enemy("Jamal", 75000, 25000, 1, 360, 2000)
                return Boss_Jamal
        elif typenumber=="a":
            if worldtype==1:
                Homecook = enemy("Homecook", 20, 5, 100, 1, 10)
                return Homecook
            elif worldtype==2:
                NormieChef = enemy("Chef", 50, 10, 200, 4, 40)
                return NormieChef
            elif worldtype==3:
                JamaicanChef = enemy("Jamaican Chef", 70, 15, 230, 7, 70)
                return JamaicanChef
            else:
                ProChef = enemy("Advanced Chef", 75, 20, 500, 10, 100)
                return ProChef
        elif typenumber=="b":
            if worldtype == 1:
                NoobChef = enemy("Noob Chef", 50, 20, 125, 2, 20)
                print("Hello Gordon")
                return NoobChef
            elif worldtype == 2:
                ThreeStarChef = enemy("3 Star Chef", 70, 25, 250, 5, 50)
                return ThreeStarChef
            elif worldtype == 3:
                JamalJr = enemy("Jamal Jr.", 100, 30, 300, 8, 80)
                return JamalJr
            else:
                FiveStarChef = enemy("5 Star Chef", 100, 30, 400, 11, 110)
                return FiveStarChef
        elif typenumber =="c":
            if worldtype == 1:
                ChinaChef = enemy("Chinese Chef", 70, 30, 150, 3, 30)
                return ChinaChef
            elif worldtype ==2:
                FourStarChef = enemy("4.99999 Star Chef", 100, 40, 300, 6, 60)
                return FourStarChef
            elif worldtype ==3:
                LebronJames = enemy("Lebron James", 150, 50, 350, 9, 90)
                return LebronJames
            else:
                MasterChef = enemy("Master Chef", 200, 100, 600, 12, 120)
                return MasterChef
    def joe(worldtype):
        if worldtype==3:
            print("Hell's Kitchen")
        elif worldtype==4:
            print("The Metaverse")
        elif worldtype==1:
            print("MSG Mountain")
        else:
            print("Jamacia")
