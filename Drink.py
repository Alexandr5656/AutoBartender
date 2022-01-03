class Drink:
    recipe = dict()
    def __init__(self,name):
        self.name = name

    def addIngredient(self, ingredient, amount):
        self.recipe[ingredient] = int(amount*28.3495)

    def getRecipe(self):
        return self.recipe

    def getName(self):
        return self.name

    def getAmount(self,ingredient):
        return self.recipe[ingredient]


