ingredients = ["Beef", "Soup"]
meals = ["wellin"]
recipes = ["Beef + Soup"]

craft_meal = input("Do you want to make a meal (y or n): ")
if craft_meal == 'y':
    print (meals)
    choose_meal = input("What meal do you want to make: ")
    if choose_meal in meals:
        craft_ingredients = ingredients(input("Put the ingredients needed for this recipe: "))
        if craft_ingredients in recipes:
            print ((meals), ('has been made'))


craft_meal()