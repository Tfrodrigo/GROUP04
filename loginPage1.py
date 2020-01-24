# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 496)
        MainWindow.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 411, 81))
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
        self.blank_usr = QtWidgets.QLineEdit(self.centralwidget)
        self.blank_usr.setGeometry(QtCore.QRect(20, 250, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blank_usr.setFont(font)
        self.blank_usr.setStyleSheet("background:rgb(255, 255, 255)")
        self.blank_usr.setObjectName("blank_usr")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(150, 330, 131, 61))
        self.btn1.setStyleSheet("")
        self.btn1.setObjectName("btn1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 411, 91))
        self.label_3.setStyleSheet("image: url(:/newPrefix/VMES.png);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " VMES CANTEEN"))
        self.label_2.setText(_translate("MainWindow", "ENTER USERNAME"))
        self.btn1.setText(_translate("MainWindow", "CONTINUE"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
