import os
import json
""" 
from ingredients import test_ingredients
shop = (test_ingredients)

class shopitems:
    shop = [test_ingredients]
    openshop = print (input("Would you like to open the shop? (Y/N): "))
    if openshop == 'Y':
        print(shop)
        buy_item = print("What would you like to buy?")
        if buy_item in shop:
            print (test_ingredients)
    else:
            print("Shop closed")


 """
with open("json/ingredients.json", "r") as f:
# Serialize the updated Python list to a JSON string
    poop = json.load(f)

class ingredients():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


while True:
    name = input("Name of the Pokemon: ")
    price = input("price of the Pokemon: ")
    description = input("description: ")
    new_pokemon = ingredients(name, price, description)
    poop.append(new_pokemon.__dict__)
    addanotherpokemon = input("Do you want to make another pokemon? y/n: ")
    if addanotherpokemon.upper() != "Y":
        break

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(poop)

    #"Write the JSON string to the new JSON file"

    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("json/ingredients.json")
os.rename(new_file, "json/ingredients.json")