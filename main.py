import Bartender as bar
import Menu as menu

import sys
from PyQt5 import QtWidgets
a = bar.Bartender()
print(a.getList())
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = menu.AutoBartender(a)
    mainWin.show()
    sys.exit( app.exec_() )