# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewAllowance_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewAllowance(object):
    def setupUi(self, viewAllowance):
        viewAllowance.setObjectName("viewAllowance")
        viewAllowance.resize(435, 577)
        viewAllowance.setStyleSheet("*{\n"
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
"color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(viewAllowance)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 411, 391))
        self.tableWidget.setStyleSheet("background: white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.resetAllowance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.resetAllowance_btn.setGeometry(QtCore.QRect(310, 10, 111, 41))
        self.resetAllowance_btn.setObjectName("resetAllowance_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        viewAllowance.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewAllowance)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 26))
        self.menubar.setObjectName("menubar")
        viewAllowance.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewAllowance)
        self.statusbar.setObjectName("statusbar")
        viewAllowance.setStatusBar(self.statusbar)

        self.retranslateUi(viewAllowance)
        QtCore.QMetaObject.connectSlotsByName(viewAllowance)

    def retranslateUi(self, viewAllowance):
        _translate = QtCore.QCoreApplication.translate
        viewAllowance.setWindowTitle(_translate("viewAllowance", "VIEW ALLOWANCE"))
        self.label_2.setText(_translate("viewAllowance", "NAME"))
        self.label_3.setText(_translate("viewAllowance", "REMAINING"))
        self.label_4.setText(_translate("viewAllowance", "ALLOWANCE"))
        self.resetAllowance_btn.setText(_translate("viewAllowance", "RESET"))
        self.label.setText(_translate("viewAllowance", "VMES CANTEEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewAllowance = QtWidgets.QMainWindow()
    ui = Ui_viewAllowance()
    ui.setupUi(viewAllowance)
    viewAllowance.show()
    sys.exit(app.exec_())
