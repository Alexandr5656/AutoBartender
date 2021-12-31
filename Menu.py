import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QScrollArea, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from Bartender import Bartender
from Drink import *


class MainMenu(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIWindow")
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.CPSBTN = QPushButton('text', self.centralwidget)
        self.CPSBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)


class DrinkMenu(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIToolTab")
        self.centralwidget = QWidget(MainWindow)
        self.ToolsBTN = QPushButton("text2", self.centralwidget)
        self.ToolsBTN.move(100, 350)
        #self.createButtons()
        #self.createButtons(MainMenu)
        self.alex()
        MainWindow.setCentralWidget(self.centralwidget)
    def alex(self):

    def createButtons(self):
        self.bartender = Bartender()
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

        #mainWindow.setCentralWidget(self.scroll)
``

class MainWindow(QMainWindow):
    def __init__(self, bartender, parent=None,):
        super(MainWindow, self).__init__(parent)
        self.uiMainMenu = MainMenu()
        self.uiDrinkMenu = DrinkMenu()
        self.startMainMenu()

    def startMainMenu(self):
        self.uiMainMenu.setupUI(self)
        self.uiMainMenu.CPSBTN.clicked.connect(self.startDrinkMenu)
        self.show()

    def startDrinkMenu(self):
        self.uiDrinkMenu.setupUI(self)
        self.uiDrinkMenu.ToolsBTN.clicked.connect(self.startMainMenu)
        self.uiDrinkMenu.createButtons()
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

