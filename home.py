from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, os

from handler import DataHandler

dh = DataHandler('VMES.db')

import temp_home

class Main(QtWidgets.QMainWindow, temp_home.Ui_home):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())