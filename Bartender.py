import json
import Drink as drinks
import Pump as pumps
class Bartender:
    pumpLocation = dict()
    drinkList = dict()
    scale = float()
    def __init__(self):
        self.getPumps()
        self.getDrinks()
    def getPumps(self):
        #Set a place where I can do invalidate a drink if a pump is not there
        pumpLink = open('./src/pump.json')
        pumpJson = json.load(pumpLink)
        for pump in pumpJson:
            self.pumpLocation[pumpJson[pump]] = pumps.Pump(pump)


    def getDrinks(self):
        recipesLink = open('./src/recipe.json')
        recipeList = json.load(recipesLink)
        for drink in recipeList:
            self.drinkList[drink]=(drinks.Drink(drink))
            for ingredient in recipeList[drink]:
                self.drinkList[drink].addIngredient(ingredient,recipeList[drink][ingredient])
    def getList(self):
        return self.drinkList

    def makeDrink(self,drink):
        #Create thread to get scale weight
        drinkRecipe = self.drinkList[drink].getRecipe()
        for ingredient in drinkRecipe:
            while self.scale < drinkRecipe[ingredient]:
                self.pumpLocation[ingredient].run

