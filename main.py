from PyQt5.QtWidgets import QApplication

import Bartender as bar
import Menu as menu

import sys
from PyQt5 import QtWidgets
a = bar.Bartender()
print(a.getList())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = menu.MainWindow(a)
    sys.exit(app.exec_())