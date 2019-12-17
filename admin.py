from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, os

from handler import DataHandler

dh = DataHandler('VMES.db')

import temp_admin, enroll_ui, enrollUser, home

class Main(QtWidgets.QMainWindow, temp_admin.Ui_adminPage):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.user_reg_btn.clicked.connect(self.enroll)
        self.hmpg_btn.clicked.connect(self.goHome)
        self.logout_btn.clicked.connect(self.end)

    def goHome(self):
        self.win1 = home.Main()
        self.win1.show()

    def enroll(self):
        self.Win = enrollUser.Main()
        self.Win.show()
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())