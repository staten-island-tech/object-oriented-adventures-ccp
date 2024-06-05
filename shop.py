import os
import json
import math
with open("json/ingredients.json", "r") as f:
    helpme=json.load(f)
with open("json/buyingweaponandarmor.json", "r") as f:
    helpme2thebetterone=json.load(f)
with open("json/itemstatuseffect.json", "r") as f:
    data2=json.load(f)
with open("json/armorstat.json", "r") as f:
    data3=json.load(f)
with open("json/weapon.json", "r") as f:
    data4=json.load(f)
class shop():
    def weaponamedisplay(tier_of_the_weapon, what_kind_of_weapon):
    #The second one work by entering a key and check where that key is not just have the item name in therre and it should work. sdhibdfvbibfwibif
        return helpme2thebetterone[1][tier_of_the_weapon][list(helpme2thebetterone[0][tier_of_the_weapon].keys()).index(what_kind_of_weapon)]
    def joebiden(tieroftheweapon, nameofweapon, iven, discount):
        if iven[4]['coin']>=math.ceil(helpme2thebetterone[0][tieroftheweapon][nameofweapon]/discount):
            iven[4]['coin']-=math.ceil(helpme2thebetterone[0][tieroftheweapon][nameofweapon]/discount)
            iven[1][tieroftheweapon][nameofweapon]+=1
            print("coin:", iven[4]['coin'])
            print(f"{shop.weaponamedisplay(tieroftheweapon, nameofweapon)}:", iven[1][tieroftheweapon][nameofweapon])
            print(f"You bought one {shop.weaponamedisplay(tieroftheweapon, nameofweapon)}")
        else:
            print("You can't do that")
    def shop(iven, characterstat):
        numberselection=0
        player=input("1.Buy item\n2.Buy armor\n3.Exit")
        os.system('cls')
        if player=="1":
            itemselected=[i for i in helpme[0]]
            for i in helpme[0]:
                numberselection+=1
                if i =="Marshmallow":
                    print("Healing")
                    print("-"*40)
                elif i =="Salt":
                    print("Attack")
                    print("-"*40)
                elif i=="Vitamins":
                    print("Buff")
                    print("-"*40)
                print(f"{numberselection}, "+i)
                print("price: " + str(math.ceil(helpme[0][i]/characterstat.intellgence)))
                for j in data2[0]:
                    for x in data2[0][j]:
                        if x == i:
                            if j=="healing":
                                print(f"Heal {data2[0][j][x]} hp")
                            elif j=="attack":
                                print(f"Deal {data2[0][j][x]} damages")
                            else:    
                                print(f"Increase your attack {data2[0][j][x]} times")
                print("")
            print(f"{numberselection+1}, "+"Exit")
            print("Coin: "+f"{iven[4]['coin']}")
            player=input("What do you wanted to buy?:")
            os.system('cls')
            if int(player)<=len(itemselected):
                for i in helpme[0]:
                    if i==itemselected[int(player)-1]:
                        player_choice=int(input("How much do you wanted to buy?: "))
                        if iven[4]['coin']>=int(helpme[0][i]/characterstat.intellgence*player_choice):
                            print(f"You bought {player_choice} {i}")
                            print(f"{i}: {iven[0][i]}+{player_choice}")
                            print(f"Coin: {iven[4]['coin']}-{int(helpme[0][i]/characterstat.intellgence*player_choice)}")
                            iven[4]['coin']-=int(helpme[0][i]/characterstat.intellgence*player_choice)
                            iven[0][i]+=player_choice
                        else:
                            print("You can't do that")
        elif player=="2":
            numberselection=0
            for i in helpme2thebetterone[0]:
                for j in helpme2thebetterone[0][i]:
                    numberselection+=1
                    print(f"{numberselection},", shop.weaponamedisplay(i, j), math.ceil(helpme2thebetterone[0][i][j]/characterstat.intellgence))
                    for x in data3[0]:
                        if x == f"{j}{i[4]}":
                            print(f"defense: {math.ceil(data3[0][x]*characterstat.defense)}")
                    for x in data4[0]:
                        if x == f"{j}{i[4]}":
                            print(f"attack damage: {math.ceil(data4[0][x]*characterstat.attack)}")
                    itemselected=[j for i in helpme2thebetterone[0] for j in helpme2thebetterone[0][i]]
                    print("")
                print("-"*40)
            print(f"{numberselection+1}, Exit" )
            print("Coin: "+f"{iven[4]['coin']}")
            player=input("What do you wanted to buy")
            os.system('cls')
            if int(player)<=len(itemselected):
                if int(player)<=9:
                    shop.joebiden('tier1eq', itemselected[int(player)-1], iven, characterstat.intellgence)
                elif int(player)<=18:
                    shop.joebiden('tier2eq', itemselected[int(player)-1], iven, characterstat.intellgence)
                else:
                    shop.joebiden('tier3eq', itemselected[int(player)-1], iven, characterstat.intellgence)
            else:
                pass