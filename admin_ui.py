# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminPage(object):
    def setupUi(self, adminPage):
        adminPage.setObjectName("adminPage")
        adminPage.resize(458, 572)
        adminPage.setStyleSheet("*{\n"
"background-color: black;\n"
"}\n"
"QPushButton\n"
"{\n"
"background: yellow;\n"
"border-radius:60px;\n"
"font: 81 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(adminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.user_reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_reg_btn.setGeometry(QtCore.QRect(70, 350, 321, 41))
        self.user_reg_btn.setObjectName("user_reg_btn")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(70, 450, 321, 41))
        self.logout_btn.setObjectName("logout_btn")
        self.hmpg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hmpg_btn.setGeometry(QtCore.QRect(70, 100, 321, 41))
        self.hmpg_btn.setObjectName("hmpg_btn")
        self.acc_mngBtn = QtWidgets.QPushButton(self.centralwidget)
        self.acc_mngBtn.setGeometry(QtCore.QRect(70, 400, 321, 41))
        self.acc_mngBtn.setObjectName("acc_mngBtn")
        self.menu_mngBtn = QtWidgets.QPushButton(self.centralwidget)
        self.menu_mngBtn.setGeometry(QtCore.QRect(70, 150, 321, 41))
        self.menu_mngBtn.setObjectName("menu_mngBtn")
        self.totalEarn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.totalEarn_btn.setGeometry(QtCore.QRect(70, 200, 321, 41))
        self.totalEarn_btn.setObjectName("totalEarn_btn")
        self.manageAthlete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.manageAthlete_btn.setGeometry(QtCore.QRect(70, 250, 321, 41))
        self.manageAthlete_btn.setObjectName("manageAthlete_btn")
        self.orderedItems_btn = QtWidgets.QPushButton(self.centralwidget)
        self.orderedItems_btn.setGeometry(QtCore.QRect(70, 300, 321, 41))
        self.orderedItems_btn.setObjectName("orderedItems_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"font:81 15pt \"Wide Latin\";\n"
"color: red;\n"
"")
        self.label.setObjectName("label")
        adminPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 26))
        self.menubar.setObjectName("menubar")
        adminPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminPage)
        self.statusbar.setObjectName("statusbar")
        adminPage.setStatusBar(self.statusbar)

        self.retranslateUi(adminPage)
        QtCore.QMetaObject.connectSlotsByName(adminPage)

    def retranslateUi(self, adminPage):
        _translate = QtCore.QCoreApplication.translate
        adminPage.setWindowTitle(_translate("adminPage", "ADMIN PAGE"))
        self.user_reg_btn.setText(_translate("adminPage", "USER REGISTRATION"))
        self.logout_btn.setText(_translate("adminPage", "LOGOUT"))
        self.hmpg_btn.setText(_translate("adminPage", "HOMEPAGE"))
        self.acc_mngBtn.setText(_translate("adminPage", "ACCOUNT MANAGEMENT"))
        self.menu_mngBtn.setText(_translate("adminPage", "MENU MANAGEMENT"))
        self.totalEarn_btn.setText(_translate("adminPage", "TOTAL EARNINGS"))
        self.manageAthlete_btn.setText(_translate("adminPage", "MANAGE ATHLETES"))
        self.orderedItems_btn.setText(_translate("adminPage", "ORDERED ITEMS (ATHLETES)"))
        self.label.setText(_translate("adminPage", "VMES CANTEEN"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminPage = QtWidgets.QMainWindow()
    ui = Ui_adminPage()
    ui.setupUi(adminPage)
    adminPage.show()
    sys.exit(app.exec_())
