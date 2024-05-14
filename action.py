import random
import os
class whatyouhave():
    inventory=[{'itemh1': 0, 
            'itemh2': 0,
            'itemh3': 0, 
            'itema1': 0, 
            'itema2': 0,
            'itema3': 0,
            'itemb1': 0, 
            'itemb2': 0,
            'itemb3': 0, 
            'arrow': 0}, 
            {
            #sword, axe, spear, bow, helment, body armor, legging, boot
            'tier1eq': {'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'pan': 0, 'armorh': 1, 'armorba': 0, 'armorl': 0, 'armorb': 0}, 
            'tier2eq':{'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'pan': 0, 'armorh': 0, 'armorba': 0, 'armorl': 0, 'armorb': 0}, 
            'tier3eq':{'sword': 0, 'axe': 0, 'spear': 0, 'bow': 0, 'pan': 0, 'armorh': 0, 'armorba': 0, 'armorl': 0, 'armorb': 0}
            }, 
            #body armor equidment
            {
                'head': "none", 
                'body': "none", 
                'leg': "none", 
                'toe': "none", 
                'weapon': "sword1"
            }]
class actionchoice():
    def walking(distance_cover_total, weighted, enemytype):
            distance_cover_total+=1
            if distance_cover_total==100:
                print("boss")
            else:
                encounter=random.choices(enemytype, weighted)
                print(encounter, distance_cover_total)
    def weaponcheck():
        if "sword" in whatyouhave.inventory[2]['weapon']:
            return "sword"
        if "bow" in whatyouhave.inventory[2]['weapon']:
            return "bow"
        if "axe" in whatyouhave.inventory[2]['weapon']:
            return "axe"
        if "spear" in whatyouhave.inventory[2]['weapon']:
            return "spear"
        if "pan" in whatyouhave.inventory[2]['weapon']:
            return "pan"
    #check the teir of the weapon
    def weaponbumbercheck():
        for i in whatyouhave.inventory[2]['weapon']:
            if i.isnumeric():
                return int(i)
    #print what you have
    def inven():
        for i in whatyouhave.inventory:
            for x in i:
                print(x, i[x])
    #equid and uneqid weapon and armor
    def equidingstuff():
        #only print what ypu have
        for x in whatyouhave.inventory[1]:
            for y in whatyouhave.inventory[1][x]:
                if whatyouhave.inventory[1][x][y]>=1:
                    print(y, whatyouhave.inventory[1][x][y])
        #show what you have equid
        for x in whatyouhave.inventory[2]:
            print(x, whatyouhave.inventory[2][x])
        player_choice=input("What equipment do you want to equip?\n1.Helmet\n2.Body armor\n3.Leggings\n4.Boots\n5. Exit\n6. Weapon")
        os.system('cls')
        #for helment
        if player_choice=="1":
            print(f"1. leather helment: {whatyouhave.inventory[1]['tier1eq']['armorh']}")
            print(f"2. copper helment: {whatyouhave.inventory[1]['tier2eq']['armorh']}")
            print(f"3. iron helment: {whatyouhave.inventory[1]['tier3eq']['armorh']}")
            print("4. Unequip")
            print("5. Exit")
            player_choice=input()
            os.system('cls')
            #equid helment
            if player_choice == "1" or player_choice == "2" or player_choice == "3":
                if whatyouhave.inventory[1][f'tier{player_choice}eq']['armorh']>=1 and whatyouhave.inventory[2]['head']=="none":
                    whatyouhave.inventory[1][f'tier{player_choice}eq']['armorh']-=1
                    whatyouhave.inventory[2]['head']=player_choice
                    print(whatyouhave.inventory[1][f'tier{player_choice}eq']['armorh'])
                    print(whatyouhave.inventory[2]['head'])
                else:
                    print("You can't do that") 
            #unequid helment
            elif player_choice == "4":
                if not whatyouhave.inventory[2]['head']=="none":
                    whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["head"]}eq']['armorh']+=1
                    print(whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["head"]}eq']['armorh'])
                    whatyouhave.inventory[2]['head']="none"
                    print(whatyouhave.inventory[2]['head'])
                else:
                    print("You can't do that") 
            else:
                pass
        #for body armor
        elif player_choice=="2":
            print(f"1. body armor1: {whatyouhave.inventory[1]['tier1eq']['armorba']}")
            print(f"2. body armor2: {whatyouhave.inventory[1]['tier2eq']['armorba']}")
            print(f"3. body armor3: {whatyouhave.inventory[1]['tier3eq']['armorba']}")
            print("4. Unequip")
            print("5. Exit")
            player_choice=input()
            os.system('cls')
            if player_choice == "1" or player_choice == "2" or player_choice == "3":
                if whatyouhave.inventory[1][f'tier{player_choice}eq']['armorba']>=1 and whatyouhave.inventory[2]['body']=="none":
                    whatyouhave.inventory[1][f'tier{player_choice}eq']['armorba']-=1
                    whatyouhave.inventory[2]['body']=player_choice
                    print(whatyouhave.inventory[1][f'tier{player_choice}eq']['armorba'])
                    print(whatyouhave.inventory[2]['body'])
                else:
                    print("You can't do that") 
            elif player_choice == "4":
                if not whatyouhave.inventory[2]['body']=="none":
                    whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["body"]}eq']['armorba']+=1
                    print(whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["body"]}eq']['armorba'])
                    whatyouhave.inventory[2]['body']="none"
                    print(whatyouhave.inventory[2]['body'])
                else:
                    print("You can't do that") 
            else:
                pass
        elif player_choice=="3":
            print(f"1. legging1: {whatyouhave.inventory[1]['tier1eq']['armorl']}")
            print(f"2. legging2: {whatyouhave.inventory[1]['tier2eq']['armorl']}")
            print(f"3. legging3: {whatyouhave.inventory[1]['tier3eq']['armorl']}")
            print("4. Unequip")
            print("5. Exit")
            player_choice=input()
            os.system('cls')
            if player_choice == "1" or player_choice == "2" or player_choice == "3":
                if whatyouhave.inventory[1][f'tier{player_choice}eq']['armorl']>=1  and whatyouhave.inventory[2]['leg']=="none":
                    whatyouhave.inventory[1][f'tier{player_choice}eq']['armorl']-=1
                    whatyouhave.inventory[2]['armorl']=player_choice
                    print(whatyouhave.inventory[1][f'tier{player_choice}eq']['armorl'])
                    print(whatyouhave.inventory[2]['leg'])
                else:
                    print("You can't do that") 
            elif player_choice == "4":
                if not whatyouhave.inventory[2]['leg']=="none":
                    whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["leg"]}eq']['armorl']+=1
                    print(whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["leg"]}eq']['armorl'])
                    whatyouhave.inventory[2]['leg']="none"
                    print(whatyouhave.inventory[2]['leg'])
                else:
                    print("You can't do that") 
            else:
                pass
        elif player_choice=="4":
            print(f"1. boot1: {whatyouhave.inventory[1]['tier1eq']['armorb']}")
            print(f"2. boot2: {whatyouhave.inventory[1]['tier2eq']['armorb']}")
            print(f"3. boot3: {whatyouhave.inventory[1]['tier3eq']['armorb']}")
            print("4. Unequip")
            print("5. Exit")
            player_choice=input()
            os.system('cls')
            if player_choice == "1" or player_choice == "2" or player_choice == "3" and whatyouhave.inventory[2]['toe']=="none":
                if whatyouhave.inventory[1][f'tier{player_choice}eq']['armorb']>=1 and whatyouhave.inventory[2]['toe']=="none":
                    whatyouhave.inventory[1][f'tier{player_choice}eq']['armorb']-=1
                    whatyouhave.inventory[2]['toe']=player_choice
                    print(whatyouhave.inventory[1][f'tier{player_choice}eq']['armorb'])
                    print(whatyouhave.inventory[2]['toe'])
                else:
                    print("You can't do that") 
            elif player_choice == "4":
                if not whatyouhave.inventory[2]['toe']=="none":
                    whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["toe"]}eq']['armorb']+=1
                    print(whatyouhave.inventory[1][f'tier{whatyouhave.inventory[2]["toe"]}eq']['armorb'])
                    whatyouhave.inventory[2]['toe']="none"
                    print(whatyouhave.inventory[2]['toe'])
                else:
                    print("You can't do that") 
            else:
                pass
        elif player_choice=="5":
            global menu_location
            menu_location = "start"
        elif player_choice=="6":
            print("1. Sword")
            print("2. Axe")
            print("3. Spear")
            print("4. Bow")
            print("5. Pan")
            print("6.unequid")
            print("7. Exit")
            player_choice=input("")
            if player_choice=="1":
                for x in whatyouhave.inventory[1]:
                    print(whatyouhave.inventory[1][x]['sword'])
                print(f"1. equid sword1\n2. equid sword2\n3. equid sword3\n4.exit")
                player_choice=input("")
                if player_choice=="1" or player_choice=="2" or player_choice=="3":
                    if whatyouhave.inventory[1][f'tier{player_choice}eq']['sword']>=1 and whatyouhave.inventory[2]['weapon']=="none":
                        whatyouhave.inventory[1][f'tier{player_choice}eq']['sword']-=1
                        whatyouhave.inventory[2]['weapon']=f"sword{player_choice}"
            elif player_choice=="2":
                for x in whatyouhave.inventory[1]:
                    print(whatyouhave.inventory[1][x]['axe'])
                print(f"1. equid axe1\n2. equid axe2\n3. equid axe3\n4.exit")
                player_choice=input("")
                if player_choice=="1" or player_choice=="2" or player_choice=="3":
                    if whatyouhave.inventory[1][f'tier{player_choice}eq']['axe']>=1 and whatyouhave.inventory[2]['weapon']=="none":
                        whatyouhave.inventory[1][f'tier{player_choice}eq']['axe']-=1
                        whatyouhave.inventory[2]['weapon']=f"axe{player_choice}"
            elif player_choice =="3":
                for x in whatyouhave.inventory[1]:
                    print(whatyouhave.inventory[1][x]['spear'])
                print(f"1. equid spear1\n2. equid spear2\n3. equid spear3\n4.exit")
                player_choice=input("")
                if player_choice=="1" or player_choice=="2" or player_choice=="3":
                    if whatyouhave.inventory[1][f'tier{player_choice}eq']['spear']>=1 and whatyouhave.inventory[2]['weapon']=="none":
                        whatyouhave.inventory[1][f'tier{player_choice}eq']['spear']-=1
                        whatyouhave.inventory[2]['weapon']=f"spear{player_choice}"
            elif player_choice =="4":
                for x in whatyouhave.inventory[1]:
                    print(whatyouhave.inventory[1][x]['bow'])
                print(f"1. equid bow1\n2. equid bow2\n3. equid bow3\n4.exit")
                player_choice=input("")
                if player_choice=="1" or player_choice=="2" or player_choice=="3":
                    if whatyouhave.inventory[1][f'tier{player_choice}eq']['bow']>=1 and whatyouhave.inventory[2]['weapon']=="none":
                        whatyouhave.inventory[1][f'tier{player_choice}eq']['bow']-=1
                        whatyouhave.inventory[2]['weapon']=f"bow{player_choice}"
            elif player_choice =="5":
                for x in whatyouhave.inventory[1]:
                    print(whatyouhave.inventory[1][x]['pan'])
                print(f"1. equid pan1\n2. equid pan2\n3. equid pan3\n4.exit")
                player_choice=input("")
                if player_choice=="1" or player_choice=="2" or player_choice=="3":
                    if whatyouhave.inventory[1][f'tier{player_choice}eq']['pan']>=1 and whatyouhave.inventory[2]['weapon']=="none":
                        whatyouhave.inventory[1][f'tier{player_choice}eq']['pan']-=1
                        whatyouhave.inventory[2]['weapon']=f"pan{player_choice}"
            elif player_choice=="6" and not whatyouhave.inventory[2]['weapon']=="none":
                    whatyouhave.inventory[1][f'tier{actionchoice.weaponbumbercheck()}eq'][actionchoice.weaponcheck()]+=1
                    whatyouhave.inventory[2]['weapon']="none"
    def choice(distance_cover_total, weighted, enemytype):
        player_choice=input("1. Walk\n2. Open inventory")
        if player_choice=="1":
            actionchoice.walking(distance_cover_total, weighted, enemytype)
        if player_choice=="2":
            actionchoice.equidingstuff()