import os
import json
with open("json/ingredients.json", "r") as f:
    helpme=json.load(f)
with open("json/buyingweaponandarmor.json", "r") as f:
    helpme2thebetterone=json.load(f)
with open("json/inventory.json", "r") as f:
    data=json.load(f)
class shop():
    def weaponamedisplay(tier_of_the_weapon, what_kind_of_weapon):
    #The second one work by entering a key and check where that key is not just have the item name in therre and it should work. sdhibdfvbibfwibif
        return helpme2thebetterone[1][tier_of_the_weapon][list(helpme2thebetterone[0][tier_of_the_weapon].keys()).index(what_kind_of_weapon)]
    def joebiden(tieroftheweapon, nameofweapon, iven):
        if iven[4]['coin']>=helpme2thebetterone[0][tieroftheweapon][nameofweapon]:
            iven[4]['coin']-=helpme2thebetterone[0][tieroftheweapon][nameofweapon]
            iven[1][tieroftheweapon][nameofweapon]+=1
            print("coin:", iven[4]['coin'])
            print(f"{shop.weaponamedisplay(tieroftheweapon, nameofweapon)}:", iven[1][tieroftheweapon][nameofweapon])
            print(f"You bought one {shop.weaponamedisplay(tieroftheweapon, nameofweapon)}")
    def shop(iven):
        numberselection=0
        player=input("1.Buy item\n2.Buy armor")
        os.system('cls')
        if player=="1":
            itemselected=[i[x] for i in helpme for x in i if x == "name"]
            print(helpme[0]['price'])
            for i in helpme:
                numberselection+=1
                print(f"{numberselection}, "+i['name'])
                print("price: "+i['price'])
                print("description"+i['description'])
            print(f"{numberselection+1}, "+"Exit")
            print("Coin: "+f"{iven[4]['coin']}")
            player=input("What do you wanted to buy?:")
            os.system('cls')
            if int(player)<=len(itemselected):
                for i in helpme:
                    if i['name']==itemselected[int(player)-1]:
                        if iven[4]['coin']>=int(i['price']):
                            iven[4]['coin']-=int(i['price'])
                            iven[0][i['name']]+=1
                            print(f"You bought 1 {i['name']}")
        elif player=="2":
            numberselection=0
            for i in helpme2thebetterone[0]:
                for j in helpme2thebetterone[0][i]:
                    numberselection+=1
                    print(f"{numberselection},", shop.weaponamedisplay(i, j), helpme2thebetterone[0][i][j])
                    itemselected=[j for i in helpme2thebetterone[0] for j in helpme2thebetterone[0][i]]
            print(f"{numberselection+1}, Exit" )
            player=input("What do you wanted to buy")
            os.system('cls')
            if int(player)<=len(itemselected):
                if int(player)<=9:
                    shop.joebiden('tier1eq', itemselected[int(player)-1], iven)
                elif int(player)<=18:
                    shop.joebiden('tier2eq', itemselected[int(player)-1], iven)
                else:
                    shop.joebiden('tier3eq', itemselected[int(player)-1], iven)
            else:
                pass