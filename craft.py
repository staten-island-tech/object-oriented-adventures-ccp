ingredients = ["a", "b"]
meals = []
recipes = ["ab"]

craft_meal = input("Do you want to make a meal (y or n): ")
if craft_meal == 'y':
    ingredients_craft = input("Put ingredients you want to use (Use '+' between each ingredient): ")
    """ split = ingredients_craft.split('+') """
    if ingredients_craft in recipes:
        print ("Success")

craft_meal()