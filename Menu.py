import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, QScrollArea, QListWidget, \
    QScrollBar, QHBoxLayout
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
            #pybutton.setIcon(QtGui.QIcon('media/drinks/empty.png'))
            pybutton.setStyleSheet(
                """
            background: url(media/drinks/empty.png);"""
            )
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


