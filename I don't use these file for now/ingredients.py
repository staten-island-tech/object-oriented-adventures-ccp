test_ingredients = ('H')

['Salt', "Pepper", 'Habanero', "Chicken", 'Oil', 'Watermelon', 'Koolaid', 'Bell Pepper', 'Steak']

class ingredients():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

all_ingredients = []

Salt = ingredients('Salt', 1, 'Salty')
Pepper = ingredients('Pepper', 1, 'Peppery')
Habanero = ingredients('Habanero', 5, 'Spicy')
Chicken = ingredients('Chicken', 7, 'Meaty')
Oil = ingredients('Oil', 5, 'Greasy')
Watermelon = ingredients('Watermelon', 10, 'Juicy')
Koolaid = ingredients('Kool aid', 8, 'Juicy')
Bell_Pepper = ingredients('Bell_Pepper', 4, 'Can be used to craft spicier peppers')
Steak = ingredients('Steak', 2, 'Meat')

print (all_ingredients)
