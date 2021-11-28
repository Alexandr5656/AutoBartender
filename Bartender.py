import json
import Drink as drinks
import Pump as pumps
from scale.hx711 import HX711
class Bartender:
    pumpLocation = dict()
    drinkList = dict()
    scale = HX711(5,6)

    def __init__(self):
        self.getPumps()
        self.getDrinks()
        self.scale.set_reading_format("MSB", "MSB")
        self.scale.set_reference_unit(113)
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
            self.scale.reset()
            self.scale.tare()
            ###Maybe I should make a starting tare
            while self.scale.get_gain(5) < drinkRecipe[ingredient]:
                self.pumpLocation[ingredient].run
                self.scale.power_down()
                self.scale.power_up()
                self.scale.sleep(0.1)


