# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuManagement_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuManagement(object):
    def setupUi(self, menuManagement):
        menuManagement.setObjectName("menuManagement")
        menuManagement.resize(295, 392)
        menuManagement.setStyleSheet("*{\n"
"background-color: black;\n"
"    }\n"
"QPushButton\n"
"{\n"
"background: red;\n"
"border-radius:60px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(menuManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.add_menu = QtWidgets.QPushButton(self.centralwidget)
        self.add_menu.setGeometry(QtCore.QRect(20, 120, 261, 51))
        self.add_menu.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.add_menu.setObjectName("add_menu")
        self.change_price = QtWidgets.QPushButton(self.centralwidget)
        self.change_price.setGeometry(QtCore.QRect(20, 190, 261, 51))
        self.change_price.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.change_price.setObjectName("change_price")
        self.delete_menu = QtWidgets.QPushButton(self.centralwidget)
        self.delete_menu.setGeometry(QtCore.QRect(20, 260, 261, 51))
        self.delete_menu.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.delete_menu.setObjectName("delete_menu")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 141, 51))
        self.label.setStyleSheet("image: url(:/newPrefix/VMES.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 131, 61))
        self.label_2.setStyleSheet("font: 75 17pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        menuManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menuManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 26))
        self.menubar.setObjectName("menubar")
        menuManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menuManagement)
        self.statusbar.setObjectName("statusbar")
        menuManagement.setStatusBar(self.statusbar)

        self.retranslateUi(menuManagement)
        QtCore.QMetaObject.connectSlotsByName(menuManagement)

    def retranslateUi(self, menuManagement):
        _translate = QtCore.QCoreApplication.translate
        menuManagement.setWindowTitle(_translate("menuManagement", "Manage Menu"))
        self.add_menu.setText(_translate("menuManagement", "Add Menu Item"))
        self.change_price.setText(_translate("menuManagement", "Change Price"))
        self.delete_menu.setText(_translate("menuManagement", "Delete Menu Item"))
        self.label_2.setText(_translate("menuManagement", "CANTEEN"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuManagement = QtWidgets.QMainWindow()
    ui = Ui_menuManagement()
    ui.setupUi(menuManagement)
    menuManagement.show()
    sys.exit(app.exec_())
