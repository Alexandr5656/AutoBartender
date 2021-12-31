#from PyQt5.QtWidgets import QApplication

import Bartender as bar
#import Menu as menu

import sys
#from PyQt5 import QtWidgets
a = bar.Bartender()
if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #w = menu.MainWindow(a)
    #sys.exit(app.exec_())
    while 1==1:
        name = input('Choose a drink \n')
        a.makeDrink(name)
