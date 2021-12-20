import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from Drink import *


# count = 0
# drinks = 10
# for r in range(drinks):
#    Button(root, text='count', height = 100, width = 100).grid(row=r,column=1)
#    count+=1
#    print(r)
#
# scrollbar = Scrollbar(root,orient='horizontal')
# scrollbar.pack(side=BOTTOM, fill=X)
#
# root.mainloop()


# TODO: Make menu object
class AutoBartender(QMainWindow):

    def __init__(self, bartender):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com")
        self.bartender = bartender
        self.createButtons()
        self.showMaximized()

        # TODO: Create Dynamic Buttons

    def createButtons(self):
        drinks = self.bartender.getList()
        for r in range(len(drinks)):
            pybutton = QPushButton(drinks[r].getName(), self)
            pybutton.clicked.connect(lambda: self.bartender.makeDrink(drinks[r]))
            pybutton.resize(100, 32)
            # TODO: Work on button positioning and multiple pages?
            pybutton.move(50, 50+(r*50))

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


