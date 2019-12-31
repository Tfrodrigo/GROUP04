from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, os

from handler import DataHandler

dh = DataHandler('VMES.db')

import admin_ui, enroll_ui, admin

class Main(QtWidgets.QMainWindow, enroll_ui.Ui_userRegistration):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.save_reg.clicked.connect(self.getInfo)

    def getInfo(self):
        newUser = self.username_reg.text()
        passWord = self.pass_reg.text()
        passWord2 = self.pass2_reg.text()
        job = self.job_combo.currentText()
        print(passWord)
        print(passWord2)
        print(job)
        if(passWord == passWord2):
            print("equals")
            dh.AddUser(newUser,passWord,job)
            self.msg = QMessageBox()
            self.msg.setWindowTitle("ENROLLED SUCCESSFULY!")
            self.msg.setText("Thank You!")
            x = self.msg.exec()
            app = QtWidgets.QApplication.instance()
            app.closeAllWindows()
            self.win = admin.Main()
            self.win.show
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("ERROR!")
            self.msg.setText("Doesn't Match! Try again")
            self.msg.setIcon(QMessageBox.Critical)
            self.x = self.msg.exec_()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())