import json
import Drink as drinks
import Pump as pumps
import time
#from scale.hx711 import HX711
class Bartender:
    pumpLocation = dict()
    drinkList = dict()
    #scale = HX711(16,12)
    recipeList = dict()
    def __init__(self):
        self.getPumps()
        self.getDrinks()
        #self.scale.set_reading_format("MSB", "MSB")
        #self.scale.set_reference_unit(453)

    def getPumps(self):
        #Set a place where I can do invalidate a drink if a pump is not there
        pumpLink = open('./src/pump.json')
        pumpJson = json.load(pumpLink)
        gpioPins = json.load(open('./src/pins.json'))
        print(gpioPins)
        for pump in pumpJson: 
            #self.pumpLocation[pumpJson[pump]] = pumps.Pump(int(pump))
            self.pumpLocation[pumpJson[pump]] = pumps.Pump(int(gpioPins[pump]))
            self.pumpLocation[pumpJson[pump]].stopPump()

    def getDrinks(self):
        recipesLink = open('./src/recipe.json')
        recipeList = json.load(recipesLink)
        for drink in recipeList:
             self.drinkList[drink]=drinks.Drink(drink)
             for ingredient in recipeList[drink]:
                  self.drinkList[drink].addIngredient(ingredient, recipeList[drink][ingredient])
    def getList(self):
        return self.drinkList

    def makeDrink(self,drink):
        for ingredient in self.drinkList[drink].getRecipe():
            #self.scale.reset()
            #self.scale.tare()
            #while self.scale.get_weight(5) < self.drinkList[drink].getAmount(ingredient):
                #self.pumpLocation[ingredient].runPump()
                #self.scale.power_down()
                #self.scale.power_up()
                #time.sleep(0.1)
            self.pumpLocation[ingredient].stopPump()

