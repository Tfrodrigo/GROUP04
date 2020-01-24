# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerType_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customerType(object):
    def setupUi(self, customerType):
        customerType.setObjectName("customerType")
        customerType.resize(340, 288)
        customerType.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 27, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:0.835821 rgba(172, 0, 31, 147), stop:1 rgba(0, 169, 255, 147));")
        self.centralwidget = QtWidgets.QWidget(customerType)
        self.centralwidget.setObjectName("centralwidget")
        self.athlete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.athlete_btn.setGeometry(QtCore.QRect(50, 140, 241, 51))
        self.athlete_btn.setStyleSheet("background:white;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.athlete_btn.setObjectName("athlete_btn")
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(50, 60, 241, 51))
        self.reg_btn.setStyleSheet("background: white;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.reg_btn.setObjectName("reg_btn")
        customerType.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customerType)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        customerType.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customerType)
        self.statusbar.setObjectName("statusbar")
        customerType.setStatusBar(self.statusbar)

        self.retranslateUi(customerType)
        QtCore.QMetaObject.connectSlotsByName(customerType)

    def retranslateUi(self, customerType):
        _translate = QtCore.QCoreApplication.translate
        customerType.setWindowTitle(_translate("customerType", "Customer"))
        self.athlete_btn.setText(_translate("customerType", "ATHLETE"))
        self.reg_btn.setText(_translate("customerType", "REGULAR"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customerType = QtWidgets.QMainWindow()
    ui = Ui_customerType()
    ui.setupUi(customerType)
    customerType.show()
    sys.exit(app.exec_())
