# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accManagement_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_acctManagement(object):
    def setupUi(self, acctManagement):
        acctManagement.setObjectName("acctManagement")
        acctManagement.resize(646, 660)
        acctManagement.setStyleSheet("*{background:\n"
"qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font: 90 15pt \"MS Shell Dlg 2\";    \n"
"color: black;\n"
" }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(acctManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.mng_userCombo = QtWidgets.QComboBox(self.centralwidget)
        self.mng_userCombo.setGeometry(QtCore.QRect(300, 40, 271, 41))
        self.mng_userCombo.setObjectName("mng_userCombo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: black;\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"\n"
"background: whiteqconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: white")
        self.label_2.setObjectName("label_2")
        self.mng_username = QtWidgets.QLabel(self.centralwidget)
        self.mng_username.setGeometry(QtCore.QRect(130, 130, 491, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.mng_username.setFont(font)
        self.mng_username.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_username.setObjectName("mng_username")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.mng_password = QtWidgets.QLabel(self.centralwidget)
        self.mng_password.setGeometry(QtCore.QRect(200, 200, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.mng_password.setFont(font)
        self.mng_password.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_password.setObjectName("mng_password")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.mng_new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.mng_new_password.setGeometry(QtCore.QRect(260, 280, 361, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.mng_new_password.setFont(font)
        self.mng_new_password.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_new_password.setObjectName("mng_new_password")
        self.mng_saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mng_saveBtn.setGeometry(QtCore.QRect(50, 520, 211, 61))
        self.mng_saveBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_saveBtn.setObjectName("mng_saveBtn")
        self.mng_deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mng_deleteBtn.setGeometry(QtCore.QRect(340, 520, 211, 61))
        self.mng_deleteBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_deleteBtn.setObjectName("mng_deleteBtn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.mng_accType = QtWidgets.QLabel(self.centralwidget)
        self.mng_accType.setGeometry(QtCore.QRect(280, 360, 341, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.mng_accType.setFont(font)
        self.mng_accType.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_accType.setObjectName("mng_accType")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 430, 301, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.mng_new_accTypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.mng_new_accTypeCombo.setGeometry(QtCore.QRect(330, 430, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.mng_new_accTypeCombo.setFont(font)
        self.mng_new_accTypeCombo.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.mng_new_accTypeCombo.setObjectName("mng_new_accTypeCombo")
        self.mng_new_accTypeCombo.addItem("")
        self.mng_new_accTypeCombo.addItem("")
        self.mng_new_accTypeCombo.addItem("")
        acctManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(acctManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 36))
        self.menubar.setObjectName("menubar")
        acctManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(acctManagement)
        self.statusbar.setObjectName("statusbar")
        acctManagement.setStatusBar(self.statusbar)

        self.retranslateUi(acctManagement)
        QtCore.QMetaObject.connectSlotsByName(acctManagement)

    def retranslateUi(self, acctManagement):
        _translate = QtCore.QCoreApplication.translate
        acctManagement.setWindowTitle(_translate("acctManagement", "Account Management"))
        self.label.setText(_translate("acctManagement", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">VMES ACCOUNTS</span></p></body></html>"))
        self.label_2.setText(_translate("acctManagement", "USER:"))
        self.mng_username.setText(_translate("acctManagement", "NA"))
        self.label_4.setText(_translate("acctManagement", "PASSWORD:"))
        self.mng_password.setText(_translate("acctManagement", "NA"))
        self.label_6.setText(_translate("acctManagement", "NEW PASSWORD:"))
        self.mng_saveBtn.setText(_translate("acctManagement", "SAVE CHANGES"))
        self.mng_deleteBtn.setText(_translate("acctManagement", "DELETE ACCOUNT"))
        self.label_7.setText(_translate("acctManagement", "ACCOUNT TYPE:"))
        self.mng_accType.setText(_translate("acctManagement", "NA"))
        self.label_9.setText(_translate("acctManagement", "NEW ACCOUNT TYPE:"))
        self.mng_new_accTypeCombo.setItemText(0, _translate("acctManagement", "--SELECT--"))
        self.mng_new_accTypeCombo.setItemText(1, _translate("acctManagement", "admin"))
        self.mng_new_accTypeCombo.setItemText(2, _translate("acctManagement", "regular"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    acctManagement = QtWidgets.QMainWindow()
    ui = Ui_acctManagement()
    ui.setupUi(acctManagement)
    acctManagement.show()
    sys.exit(app.exec_())
