#Cooks will drop recipes and ingredients, ingredients can be combined by following a recipe to create dishes

class recipe():
    def __init__(self, name, heal, attack, buff, debuff):
        self.name = name
        self.heal = heal
        self.attack = attack
        self.buff = buff
        self.debuff = debuff

recipe_template = recipe("Name", 10, 10, 10, 10)