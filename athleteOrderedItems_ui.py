# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'athleteOrderedItems_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_athete_orderedItems(object):
    def setupUi(self, athete_orderedItems):
        athete_orderedItems.setObjectName("athete_orderedItems")
        athete_orderedItems.resize(553, 577)
        athete_orderedItems.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(athete_orderedItems)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.total_lbl = QtWidgets.QLabel(self.centralwidget)
        self.total_lbl.setGeometry(QtCore.QRect(160, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.total_lbl.setFont(font)
        self.total_lbl.setStyleSheet("background:white;\n"
"color: black;")
        self.total_lbl.setObjectName("total_lbl")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 531, 391))
        self.tableWidget.setStyleSheet("background:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(410, 20, 111, 41))
        self.del_btn.setObjectName("del_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        athete_orderedItems.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(athete_orderedItems)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 26))
        self.menubar.setObjectName("menubar")
        athete_orderedItems.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(athete_orderedItems)
        self.statusbar.setObjectName("statusbar")
        athete_orderedItems.setStatusBar(self.statusbar)

        self.retranslateUi(athete_orderedItems)
        QtCore.QMetaObject.connectSlotsByName(athete_orderedItems)

    def retranslateUi(self, athete_orderedItems):
        _translate = QtCore.QCoreApplication.translate
        athete_orderedItems.setWindowTitle(_translate("athete_orderedItems", "Athlete Orders"))
        self.label.setText(_translate("athete_orderedItems", "TOTAL: P"))
        self.total_lbl.setText(_translate("athete_orderedItems", "0.00"))
        self.label_2.setText(_translate("athete_orderedItems", "DATE"))
        self.label_3.setText(_translate("athete_orderedItems", "PRICE"))
        self.label_4.setText(_translate("athete_orderedItems", "ITEM"))
        self.del_btn.setText(_translate("athete_orderedItems", "DELETE ALL"))
        self.label_5.setText(_translate("athete_orderedItems", "NAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    athete_orderedItems = QtWidgets.QMainWindow()
    ui = Ui_athete_orderedItems()
    ui.setupUi(athete_orderedItems)
    athete_orderedItems.show()
    sys.exit(app.exec_())
