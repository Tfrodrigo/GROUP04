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
        self.label_2.setGeometry(QtCore.QRect(30, 100, 371, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("adminpic.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminPage = QtWidgets.QMainWindow()
    ui = Ui_adminPage()
    ui.setupUi(adminPage)
    adminPage.show()
    sys.exit(app.exec_())
