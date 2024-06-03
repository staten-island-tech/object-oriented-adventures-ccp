import random
import os
import json
from characterandenemy import characterdata
from enemyandcombat import combat
with open("json/weapon.json", "r") as f:
    weaponstat=json.load(f)
with open("json/armorstat.json", "r") as f:
    armorstat=json.load(f)
class actionchoice():
#This determine walking and walking encounter
    def walking(characterstat, enemyencounter, weight_chance, inven):
            characterstat.total_step+=100
            os.system('cls')
            if characterstat.total_step==100:
                combat.combating(characterstat, characterstat.enemytypestat(characterstat.worldtype, "Boss"), inven)
                characterstat.total_step=0
                characterstat.worldtype+=1
                characterdata.enemytypestat(characterstat.worldtype, encounter, inven)
            else:
                encounter=random.choices(enemyencounter, weight_chance)
                combat.combating(characterstat, characterdata.enemytypestat(characterdata.worldtype, encounter), inven)
            if characterstat.worldtype==1:
                print("MSG mountains")
            elif characterstat.worldtype==2:
                print("Jaciamica")
            elif characterstat.worldtype==3:
                print("Hell Kitchen")
            else:
                print("The Metaverse")
#THIS HURT MY BRAINHHSAKLHFDSKHFUKHAS
    def weaponamedisplay(tier_of_the_weapon, what_kind_of_weapon, data):
    #The second one work by entering a key and check where that key is not just have the item name in therre and it should work. sdhibdfvbibfwibif
        return data[3][tier_of_the_weapon][list(data[1][tier_of_the_weapon].keys()).index(what_kind_of_weapon)]
#This display item
    def inventorydisplay(data):
    #This is the inventory display
        print("Items")
        for items in data[0]:
            print(f"{items}: {data[0][items]}")
    #This display armor and weapons
        print("Weapon and armor you have")
        for tier_of_weapon in data[1]:
      #This show us the index number so you can check the list of name
      #the first is the name of the weapon, just enter tier of weapon and the type of weapon
            for weapon in data[1][tier_of_weapon]:  
                print(f"{actionchoice.weaponamedisplay(tier_of_weapon, weapon, data)}: {data[1][tier_of_weapon][weapon]}")
        print("Armor and Weapon Equid")
        for armor_and_weapon_equiped in data[2]:
      #This check the tier of the armor and the type of armor
            x=[i for i in data[2][armor_and_weapon_equiped] if i.isdigit()]
            weapon=''.join([i for i in data[2][armor_and_weapon_equiped] if not i.isdigit()])
            if not len(x)==0 and not weapon=="none":
                print(armor_and_weapon_equiped, actionchoice.weaponamedisplay(f"tier{x[0]}eq", weapon, data) + "defense:" + armorstat[0][data[2][data[2][armor_and_weapon_equiped]]])
            else:
                print(armor_and_weapon_equiped, data[2][armor_and_weapon_equiped]+"attack:"+armorstat[0][data[2][data[2][armor_and_weapon_equiped]]])
    def weaponchecktypedisplay(x):
        if x=="1":
            return "sword"
        elif x=="2":
            return "axe"
        elif x=="3":
            return "spear"
        elif x=="4":
            return "bow"
        elif x=="5":
            return "pan"
#This equid and unequid weapon and armor    
    def unequipandequipingweapon(player_choice, whereonbody, armortype, data):
        os.system('cls')
        if player_choice=="4":
            if not data[2][whereonbody]=="none":
                x=[i for i in data[2][whereonbody] if i.isdigit()]
                data[1][f"tier{x[0]}eq"][armortype]+=1
                data[2][whereonbody]="none"
                print(actionchoice.weaponamedisplay(f"tier{x[0]}eq", armortype, data),":",data[1][f"tier{x[0]}eq"][armortype])
                print(f"{whereonbody}: none")
            else:
                print("You can't do that")
        elif int(player_choice)>=1 and int(player_choice)<=3 and data[2][whereonbody]=="none":
            if data[1][f"tier{player_choice}eq"][armortype]>=1:
                data[2][whereonbody]=f"{armortype}{player_choice}"
                data[1][f"tier{player_choice}eq"][armortype]-=1
                print(actionchoice.weaponamedisplay(f"tier{player_choice}eq", armortype, data),":",data[1][f"tier{player_choice}eq"][armortype])
                print(f"{whereonbody}: ",actionchoice.weaponamedisplay(f"tier{player_choice}eq", armortype, data))
            else:
                print("You can't do that")
        else:
            print("You can't do that")
#This combine the previous function together to create a unequid and equid armor and weapon
    def equip_and_unequip(data):
        player_choice=input("What equipment do you want to equip?\n1.Helmet\n2.Body armor\n3.Leggings\n4.Boots\n5. Weapon\n6. Exit")
        os.system('cls')
        if player_choice=="1":
            for tier in data[1]:
                print(f"{tier[4]},", actionchoice.weaponamedisplay(tier, 'armorh', data), data[1][tier]['armorh'])
            player_choice=input("4. Uneqip\n5. Exit")
            actionchoice.unequipandequipingweapon(player_choice, 'Head', 'armorh', data)
        elif player_choice=="2":
            for tier in data[1]:
                print(f"{tier[4]},",actionchoice.weaponamedisplay(tier, 'armorba', data), data[1][tier]['armorba'])
            player_choice=input("4. Uneqip\n5. Exit")
            actionchoice.unequipandequipingweapon(player_choice, 'Body', 'armorba', data)
        elif player_choice=="3":
            for tier in data[1]:
                print(f"{tier[4]},",actionchoice.weaponamedisplay(tier, 'armorl', data), data[1][tier]['armorl'])
            player_choice=input("4. Uneqip\n5. Exit")
            actionchoice.unequipandequipingweapon(player_choice, 'Leg', 'armorl', data)
        elif player_choice=="4":
            for tier in data[1]:
                print(f"{tier[4]},",actionchoice.weaponamedisplay(tier, 'armorb', data), data[1][tier]['armorb'])
            player_choice=input("4. Uneqip\n5. Exit")
            actionchoice.unequipandequipingweapon(player_choice, 'Toe', 'armorb', data)
        elif player_choice=="5":
            print("1. Sword")
            print("2. Axe")
            print("3. Spear")
            print("4. Bow")
            print("5. Pan")
            print("6. Unequip")
            print("7. Exit")
            player_choice=input("")
            os.system('cls')
            if player_choice=="7":
                pass
            elif player_choice=="6":
                if data[2]['Weapon']=="none":
                    print("You don't have a weapon equipped")
                else:
                    x=[i for i in data[2]["Weapon"] if i.isdigit()]
                    weapon=''.join([i for i in data[2]["Weapon"] if not i.isdigit()])
                    data[1][f"tier{x[0]}eq"][weapon]+=1
                    print(actionchoice.weaponamedisplay(f"tier{x[0]}eq", weapon, data),": ",data[1][f"tier{x[0]}eq"][weapon])
                    data[2]['Weapon']="none"
                    print(data[2]['Weapon'])
            else:
                for touhou in data[1]:
                    numberselection=[i for i in touhou if i.isdigit()]
                    print(f"{numberselection[0]}, {actionchoice.weaponamedisplay(touhou, actionchoice.weaponchecktypedisplay(player_choice), data)}: {data[1][touhou][actionchoice.weaponchecktypedisplay(player_choice)]}")
                print("4. Exit")
                this_remember_what_weapon_we_are_on=actionchoice.weaponchecktypedisplay(player_choice)
                player_choice=input("")
                os.system('cls')
                if player_choice=="4":
                    pass
                elif int(player_choice)>=1 and int(player_choice)<=3:
                    if data[2]['Weapon'] == "none" and data[1][f"tier{player_choice}eq"][this_remember_what_weapon_we_are_on]>=1:
                        data[1][f"tier{player_choice}eq"][this_remember_what_weapon_we_are_on]-=1
                        data[2]['Weapon']=f"{this_remember_what_weapon_we_are_on}{player_choice}"
                        print(actionchoice.weaponamedisplay(f"tier{player_choice}eq" ,this_remember_what_weapon_we_are_on, data),":", data[1][f"tier{player_choice}eq"][this_remember_what_weapon_we_are_on])
                        print("Weapon:", actionchoice.weaponamedisplay(f"tier{player_choice}eq" ,this_remember_what_weapon_we_are_on, data))
                    else:
                        print("You can't do that")
#This combine everything to create the ult walking sim
    def choice(characterstat, weight_chance, enemyencounter, data):
        player_choice=input("1. Walk\n2. Open inventory")
        os.system('cls')
        if player_choice=="1":
            actionchoice.walking(characterstat, enemyencounter, weight_chance, data)
        else:
            actionchoice.inventorydisplay(data)
            actionchoice.equip_and_unequip(data)