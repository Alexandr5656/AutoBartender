import sys
from functools import partial

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QScrollArea, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from Bartender import Bartender
from Drink import *

# TODO: Create selection menu
# TODO: On selection menu have a stronger weaker normal and virgin option
class MainMenu(object):
    def setupUI(self, MainWindow, bartender):
        MainWindow.setWindowTitle("AutoBartender Main Menu")
        self.centralwidget = QWidget(MainWindow)
        self.AutoMenu = QPushButton('Drink Menu', self.centralwidget)
        self.AutoMenu.move(int(MainWindow.size().width() / 10), int(MainWindow.size().height()/10))
        self.AutoMenu.setFixedSize(int(MainWindow.size().width()/3),int(MainWindow.size().height()/4*3))
        self.SettingMenu = QPushButton('Settings Menu', self.centralwidget)
        self.SettingMenu.move(int(MainWindow.size().width() / 10 * 5), int(MainWindow.size().height() / 10))
        self.SettingMenu.setFixedSize(int(MainWindow.size().width() / 3), int(MainWindow.size().height() / 4 * 3))
        MainWindow.setCentralWidget(self.centralwidget)

class DrinkSelection(object):

    #TODO:Set up indiviual liquor levels
    #TODO:Set up cup size levels
    def setupUI(self, MainWindow, bartender, drink):
        self.bartender = bartender
        self.drink = drink
        self.level = 1
        MainWindow.setWindowTitle("Drink Selection")
        self.centralwidget = QWidget(MainWindow)

        #Strength Label
        self.StrengthLevel = QLabel("Strength Level: 1 ", self.centralwidget)
        self.StrengthLevel.move(int(MainWindow.size().width()/2),10)

        #Increase
        self.makeStrongerBTN = QPushButton("Make Stronger", self.centralwidget)
        self.makeStrongerBTN.setFixedSize(100,100)
        self.makeStrongerBTN.move((int(MainWindow.size().width()/4) * 3), 10)
        self.makeStrongerBTN.clicked.connect(self.increase)

        #Decrease
        self.makeWeakerBTN = QPushButton("Make Weaker", self.centralwidget)
        self.makeWeakerBTN.setFixedSize(100, 100)
        self.makeWeakerBTN.move(int((MainWindow.size().width() / 4)), 10)
        self.makeWeakerBTN.clicked.connect(self.decrease)

        #Drink Button
        self.makeDrinkBTN = QPushButton(f"Make {drink}", self.centralwidget)
        self.makeDrinkBTN.move(int(MainWindow.size().width() / 3), int(MainWindow.size().height() / 10))
        self.makeDrinkBTN.setFixedSize(int(MainWindow.size().width() / 3), int(MainWindow.size().height() / 4 * 3))
        self.makeDrinkBTN.clicked.connect(partial(bartender.makeDrink, drink=drink,level=self.level))
        #self.makeDrinkBTN.clicked.connect(self.makeThisDrink)

        #Back Button
        self.backButton = QPushButton("Back", self.centralwidget)
        self.backButton.move(10, 10)
        MainWindow.setCentralWidget(self.centralwidget)
    def decrease(self):
        if self.level<=0:
            return
        self.level = self.level-1
        self.StrengthLevel.setText(f"Strength Level: {self.level}")

    def increase(self):
        if self.level>=3:
            return
        self.level = self.level+1
        self.StrengthLevel.setText(f"Strength Level: {self.level}")

    def makeThisDrink(self,drink,level):
        self.bartender.makeDrink(drink,level)


class DrinkMenu(object):
    def setupUI(self, MainWindow, bartender, app):
        self.MainWindow = MainWindow
        MainWindow.setGeometry(0, 0, app.primaryScreen().size().width(), app.primaryScreen().size().height())
        MainWindow.setFixedSize(app.primaryScreen().size().width(), app.primaryScreen().size().height())
        MainWindow.setWindowTitle("UIToolTab")
        self.centralwidget = QWidget(MainWindow)
        self.ToolsBTN = QPushButton("Back", self.centralwidget)
        self.ToolsBTN.move(10, 10)
        self.button_width = int(app.primaryScreen().size().width() / 3)
        self.button_height = int(app.primaryScreen().size().height() / 3)
        self.createButtons()
        MainWindow.setCentralWidget(self.centralwidget)

    def createButtons(self):
        self.bartender = Bartender()
        drinks = self.bartender.getList()
        self.scroll = QScrollArea(self.centralwidget)
        self.widget = QWidget()
        self.hbox = QHBoxLayout()
        self.buttons = []
        for drink in drinks:
            self.buttons.append(QPushButton())
            self.buttons[-1].setText(drink)
            self.buttons[-1].setFixedWidth(self.button_width)
            self.buttons[-1].setFixedHeight(self.button_height*2)
            self.buttons[-1].clicked.connect(partial(self.MainWindow.startDrinkSelector, drinkPicked=drink))
            self.buttons[-1].setIcon(QtGui.QIcon('media/drinks/empty.png'))
            self.buttons[-1].setIconSize(QSize(int(self.button_width/3),int(self.button_height/3)))
            self.hbox.addWidget(self.buttons[-1])

        self.widget.setLayout(self.hbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setFixedWidth(self.button_width*3)
        self.scroll.setFixedHeight(self.button_height*2)
        self.scroll.move(0,int(self.button_height/2))

class MainWindow(QMainWindow):
    def __init__(self, bartender, app, parent=None,):
        super(MainWindow, self).__init__(parent)
        self.bartender = bartender
        self.setFixedWidth(app.primaryScreen().size().width())
        self.setFixedHeight(app.primaryScreen().size().height())
        self.app = app
        self.uiMainMenu = MainMenu()
        self.uiDrinkMenu = DrinkMenu()
        self.uiDrinkSelector = DrinkSelection()
        self.startMainMenu()

    def startMainMenu(self):
        self.uiMainMenu.setupUI(self, self.bartender)
        self.uiMainMenu.AutoMenu.clicked.connect(self.startDrinkMenu)
        self.show()

    def startDrinkMenu(self):
        self.uiDrinkMenu.setupUI(self, self.bartender, self.app)
        self.uiDrinkMenu.ToolsBTN.clicked.connect(self.startMainMenu)
        self.uiDrinkMenu.createButtons()
        self.show()
    def startDrinkSelector(self, drinkPicked):
        self.uiDrinkSelector.setupUI(self, self.bartender, drinkPicked)
        self.uiDrinkSelector.backButton.clicked.connect(self.startDrinkMenu)
        self.show()

# TODO: Make menu object
class AutoBartender(QWidget):

    def __init__(self, bartender,app):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com")
        self.bartender = bartender
        self.button_width = int(app.primaryScreen().size().width()/3)
        self.button_height = int(app.primaryScreen().size().height()/3)
        self.createButtons()
        self.showMaximized()
        # TODO: Create Dynamic Buttons

    def createButtons(self):
        drinks = self.bartender.getList()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.hbox = QHBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for x in range(len(drinks)):
            pybutton = QPushButton()
            pybutton.setText(drinks[x].getName())
            pybutton.clicked.connect(lambda: self.bartender.makeDrink(drinks[x]))
            # TODO: Work on button positioning and multiple pages?
            pybutton.setFixedWidth(self.button_width)
            pybutton.setFixedHeight(self.button_height)
            pybutton.setLayoutDirection(QtCore.Qt.RightToLeft)
            pybutton.setIcon(QtGui.QIcon('media/drinks/empty.png'))
            pybutton.setIconSize(QSize(int(self.button_width/3),int(self.button_height/3)))
            self.hbox.addWidget(pybutton)

        self.widget.setLayout(self.hbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        #self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()
        return


    def clickMethod(self):
        print('Clicked Pyqt button.')

    def clickerMethod(self):
        print('Clicked Pyqeeet button.')
    # TODO: Create system to weigh cups
    def tareGlass(self):
        pass

    # TODO: Create way to set see weight
    def getWeight(self):
        pass

    # TODO: Cup Selection menu?
    def createCupMenu(self):
        pass

    def makeDrink(self, drink):
        drink.makeDrink()
    # TODO: Get ip button (for parents to send me info to fix)
    def ipButton(self):
        pass

