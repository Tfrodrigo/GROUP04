from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial

import addAthlete, removeAthlete, allowance

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import manageAthlete_ui

class Main(QtWidgets.QMainWindow, manageAthlete_ui.Ui_manageAthlete):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.add_athleteBtn.clicked.connect(self.goAdd)
        self.rem_athleteBtn.clicked.connect(self.goRemove)
        self.viewAllowance_btn.clicked.connect(self.view_allowance)

    def goAdd(self):
        self.win1 = addAthlete.Main()
        self.win1.show()

    def goRemove(self):
        self.win2 = removeAthlete.Main()
        self.win2.show()

    def view_allowance(self):
        self.win3 = allowance.Main()
        self.win3.show()
        
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())