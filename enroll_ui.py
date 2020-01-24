# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enroll_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userRegistration(object):
    def setupUi(self, userRegistration):
        userRegistration.setObjectName("userRegistration")
        userRegistration.resize(800, 597)
        userRegistration.setStyleSheet("*{background:\n"
"qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font: 90 15pt \"MS Shell Dlg 2\";    \n"
"color: black;\n"
" }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(userRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.job_combo = QtWidgets.QComboBox(self.centralwidget)
        self.job_combo.setGeometry(QtCore.QRect(320, 360, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.job_combo.setFont(font)
        self.job_combo.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.job_combo.setObjectName("job_combo")
        self.job_combo.addItem("")
        self.job_combo.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 360, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.username_reg.setGeometry(QtCore.QRect(320, 80, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.username_reg.setFont(font)
        self.username_reg.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.username_reg.setObjectName("username_reg")
        self.pass_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_reg.setGeometry(QtCore.QRect(320, 170, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.pass_reg.setFont(font)
        self.pass_reg.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.pass_reg.setObjectName("pass_reg")
        self.pass2_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.pass2_reg.setGeometry(QtCore.QRect(320, 270, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.pass2_reg.setFont(font)
        self.pass2_reg.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.pass2_reg.setObjectName("pass2_reg")
        self.save_reg = QtWidgets.QPushButton(self.centralwidget)
        self.save_reg.setGeometry(QtCore.QRect(330, 440, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.save_reg.setFont(font)
        self.save_reg.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(210, 232, 12)")
        self.save_reg.setObjectName("save_reg")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: black;\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"\n"
"background: whiteqconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        userRegistration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(userRegistration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        userRegistration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(userRegistration)
        self.statusbar.setObjectName("statusbar")
        userRegistration.setStatusBar(self.statusbar)

        self.retranslateUi(userRegistration)
        QtCore.QMetaObject.connectSlotsByName(userRegistration)

    def retranslateUi(self, userRegistration):
        _translate = QtCore.QCoreApplication.translate
        userRegistration.setWindowTitle(_translate("userRegistration", "USER REGISTRATION"))
        self.label.setText(_translate("userRegistration", "USERNAME:"))
        self.label_2.setText(_translate("userRegistration", "PASSWORD:"))
        self.label_3.setText(_translate("userRegistration", "RETYPE PASSWORD:"))
        self.job_combo.setItemText(0, _translate("userRegistration", "admin"))
        self.job_combo.setItemText(1, _translate("userRegistration", "regular"))
        self.label_4.setText(_translate("userRegistration", "ACCOUNT TYPE:"))
        self.save_reg.setText(_translate("userRegistration", "SAVE"))
        self.label_5.setText(_translate("userRegistration", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">VMES CANTEEN</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userRegistration = QtWidgets.QMainWindow()
    ui = Ui_userRegistration()
    ui.setupUi(userRegistration)
    userRegistration.show()
    sys.exit(app.exec_())
