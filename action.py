import random
import os
import json
with open("inventory.json", "r") as f:
  data=json.load(f)
class actionchoice():
    def walking(distance_cover_total, weighted, enemytype):
            distance_cover_total+=1
            if distance_cover_total==100:
                print("boss")
            else:
                encounter=random.choices(enemytype, weighted)
                print(encounter, distance_cover_total)
  #THIS HURT MY BRAINHHSAKLHFDSKHFUKHAS
    def weaponamedisplay(tier_of_the_weapon, what_kind_of_weapon):
    #The second one work by entering a key and check where that key is not just have the item name in therre and it should work. sdhibdfvbibfwibif
        return data[3][tier_of_the_weapon][list(data[1][tier_of_the_weapon].keys()).index(what_kind_of_weapon)]
  #This display item
    def inventorydisplay():
    #This is the inventory display
        for items in data[0]:
            print(f"{items}: {data[0][items]}")
    #This display armor and weapons
        for tier_of_weapon in data[1]:
      #This show us the index number so you can check the list of name
      #the first is the name of the weapon, just enter tier of weapon and the type of weapon
            for weapon in data[1][tier_of_weapon]:  
                print(f"{actionchoice.weaponamedisplay(tier_of_weapon, weapon)}: {data[1][tier_of_weapon][weapon]}")
        for armor_and_weapon_equiped in data[2]:
      #This check the tier of the armor and the type of armor
            x=[i for i in data[2][armor_and_weapon_equiped] if i.isdigit()]
            weapon=''.join([i for i in data[2][armor_and_weapon_equiped] if not i.isdigit()])
            if not len(x)==0 and not weapon=="none":
                print(armor_and_weapon_equiped, actionchoice.weaponamedisplay(f"tier{x[0]}eq", weapon))
            else:
                print(armor_and_weapon_equiped, data[2][armor_and_weapon_equiped])
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
    def equip_and_unequip():
        player_choice=input("What equipment do you want to equip?\n1.Helmet\n2.Body armor\n3.Leggings\n4.Boots\n5. Weapon\n6. Exit")
        if player_choice=="1":
            for tier in data[1]:
                print(actionchoice.weaponamedisplay(tier, 'armorh'), data[1][tier]['armorh'])
        if player_choice=="2":
            for tier in data[1]:
                print(actionchoice.weaponamedisplay(tier, 'armorba'), data[1][tier]['armorba'])
        if player_choice=="3":
            for tier in data[1]:
                print(actionchoice.weaponamedisplay(tier, 'armorl'), data[1][tier]['armorl'])
        if player_choice=="4":
            for tier in data[1]:
                print(actionchoice.weaponamedisplay(tier, 'armorb'), data[1][tier]['armorb'])
        if player_choice=="5":
            print("1. Sword")
            print("2. Axe")
            print("3. Spear")
            print("4. Bow")
            print("5. Pan")
            print("6. Unequip")
            print("7. Exit")
            player_choice=input("")
            if player_choice=="7":
                pass
            elif player_choice=="6":
                if data[2]['Weapon']=="none":
                    print("You don't have a weapon equipped")
                else:
                    x=[i for i in data[2]["Weapon"] if i.isdigit()]
                    weapon=''.join([i for i in data[2]["Weapon"] if not i.isdigit()])
                    data[1][f"tier{x[0]}eq"][weapon]+=1
                    print(actionchoice.weaponamedisplay(f"tier{x[0]}eq", weapon),": ",data[1][f"tier{x[0]}eq"][weapon])
                    data[2]['Weapon']="none"
                    print(data[2]['Weapon'])
            else:
                for touhou in data[1]:
                    numberselection=[i for i in touhou if i.isdigit()]
                    print(f"{numberselection[0]}, {actionchoice.weaponamedisplay(touhou, actionchoice.weaponchecktypedisplay(player_choice))}: {data[1][touhou][actionchoice.weaponchecktypedisplay(player_choice)]}")
                print("4. Exit")
                this_remember_what_weapon_we_are_on=actionchoice.weaponchecktypedisplay(player_choice)
                player_choice=input("")
                if player_choice=="4":
                    pass
                elif int(player_choice)>=1 and int(player_choice)<=3:
                    if data[2]['Weapon']
                        print("ahjah")
    def choice(total_step, weight_chance, enemyencounter, menu_location):
        player_choice=input("1. Walk\n2.Open inventory")
        if player_choice=="1":
            actionchoice.walking(total_step, weight_chance, enemyencounter)
        else:]
            actionchoice.inventorydisplay()
            actionchoice.equip_and_unequip()
while True:
    actionchoice.choice(1, 2, 3, 4)