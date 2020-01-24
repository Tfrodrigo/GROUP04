from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial

import home, homepageAthlete

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import customerType_ui

class Main(QtWidgets.QMainWindow, customerType_ui.Ui_customerType):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.reg_btn.clicked.connect(self.regularApp)
        self.athlete_btn.clicked.connect(self.athleteApp)

    def regularApp(self):
        self.win1 = home.Main()
        self.win1.show()

    def athleteApp(self):
        self.win2 = homepageAthlete.Main()
        self.win2.show()
        
        
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())