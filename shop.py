import os
import json
with open("json/ingredients.json", "r") as f:
    helpme=json.load(f)
with open("json/buyingweaponandarmor.json", "r") as f:
    helpme2thebetterone=json.load(f)
class shop():
    def shop(iven):
        numberselection=0
        player=input("1.Buy item\n2.Buy armor")
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
            if int(player)<=len(itemselected):
                for i in helpme:
                    if i['name']==itemselected[int(player)-1]:
                        if iven[4]['coin']>=int(i['price']):
                            iven[4]['coin']-=int(i['price'])
                            iven[0][i['name']]+=1
        