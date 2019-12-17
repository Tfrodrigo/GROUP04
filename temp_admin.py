# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminPage(object):
    def setupUi(self, adminPage):
        adminPage.setObjectName("adminPage")
        adminPage.resize(422, 551)
        self.centralwidget = QtWidgets.QWidget(adminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 181, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("adminpic.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 310, 181, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("adminpic.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.user_reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_reg_btn.setGeometry(QtCore.QRect(40, 90, 321, 41))
        self.user_reg_btn.setObjectName("user_reg_btn")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(40, 190, 321, 41))
        self.logout_btn.setObjectName("logout_btn")
        self.hmpg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hmpg_btn.setGeometry(QtCore.QRect(40, 140, 321, 41))
        self.hmpg_btn.setObjectName("hmpg_btn")
        adminPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 26))
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
        self.label.setText(_translate("adminPage", "VMES CANTEEN"))
        self.user_reg_btn.setText(_translate("adminPage", "USER REGISTRATION"))
        self.logout_btn.setText(_translate("adminPage", "LOGOUT"))
        self.hmpg_btn.setText(_translate("adminPage", "HOMEPAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminPage = QtWidgets.QMainWindow()
    ui = Ui_adminPage()
    ui.setupUi(adminPage)
    adminPage.show()
    sys.exit(app.exec_())
