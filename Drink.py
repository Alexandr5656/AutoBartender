class Drink:
    recipe = dict()
    def __init__(self,name):
        self.name = name

    def addIngredient(self, ingredient, amount):
        self.recipe[ingredient] = amount
    def getRecipe(self):
        return self.recipe
    def getName(self):
        return self.name


