# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(460, 496)
        MainWindow2.setStyleSheet("*{\n"
"background-color: black;\n"
"}\n"
"QPushButton\n"
"{\n"
"background: red;\n"
"border-radius:60px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: black;\n"
"}")

        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"font:81 15pt \"Wide Latin\";\n"
"color: YELLOW;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.blank_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.blank_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.blank_pass.setGeometry(QtCore.QRect(20, 250, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blank_pass.setFont(font)
        self.blank_pass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blank_pass.setObjectName("blank_pass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(150, 330, 151, 51))
        self.btn_login.setObjectName("btn_login")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 411, 91))
        self.label_3.setStyleSheet("image: url(:/newPrefix/VMES.png);")
        self.label_3.setObjectName("label_3")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "AUTHENTICATION"))
        self.label.setText(_translate("MainWindow2", "VMES CANTEEN"))
        self.label_2.setText(_translate("MainWindow2", "ENTER PASSWORD"))
        self.btn_login.setText(_translate("MainWindow2", "LOGIN"))
        
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
