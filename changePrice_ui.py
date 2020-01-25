# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePrice_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changePrice(object):
    def setupUi(self, changePrice):
        changePrice.setObjectName("changePrice")
        changePrice.resize(586, 485)
        changePrice.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(changePrice)
        self.centralwidget.setObjectName("centralwidget")
        self.save_price = QtWidgets.QPushButton(self.centralwidget)
        self.save_price.setGeometry(QtCore.QRect(250, 380, 131, 51))
        self.save_price.setObjectName("save_price")
        self.chngPrc_bfastBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chngPrc_bfastBtn.setGeometry(QtCore.QRect(60, 110, 151, 61))
        self.chngPrc_bfastBtn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.chngPrc_bfastBtn.setObjectName("chngPrc_bfastBtn")
        self.chngPrc_lunchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chngPrc_lunchBtn.setGeometry(QtCore.QRect(220, 110, 151, 61))
        self.chngPrc_lunchBtn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.chngPrc_lunchBtn.setObjectName("chngPrc_lunchBtn")
        self.chngPrc_snackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chngPrc_snackBtn.setGeometry(QtCore.QRect(380, 110, 151, 61))
        self.chngPrc_snackBtn.setStyleSheet("font: 50 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.chngPrc_snackBtn.setObjectName("chngPrc_snackBtn")
        self.chngPrc_menuCombo = QtWidgets.QComboBox(self.centralwidget)
        self.chngPrc_menuCombo.setGeometry(QtCore.QRect(60, 190, 471, 41))
        self.chngPrc_menuCombo.setStyleSheet("background:rgb(255, 255, 255)")
        self.chngPrc_menuCombo.setObjectName("chngPrc_menuCombo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 290, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.chngPrc_currentPrice = QtWidgets.QLabel(self.centralwidget)
        self.chngPrc_currentPrice.setGeometry(QtCore.QRect(170, 290, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chngPrc_currentPrice.setFont(font)
        self.chngPrc_currentPrice.setStyleSheet("color: white;")
        self.chngPrc_currentPrice.setObjectName("chngPrc_currentPrice")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 330, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.chngPrc_newPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.chngPrc_newPrice.setGeometry(QtCore.QRect(240, 320, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chngPrc_newPrice.setFont(font)
        self.chngPrc_newPrice.setStyleSheet("\n"
"background: white")
        self.chngPrc_newPrice.setObjectName("chngPrc_newPrice")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.food_lbl = QtWidgets.QLabel(self.centralwidget)
        self.food_lbl.setGeometry(QtCore.QRect(150, 240, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.food_lbl.setFont(font)
        self.food_lbl.setStyleSheet("background:white")
        self.food_lbl.setObjectName("food_lbl")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"font:81 15pt \"Wide Latin\";\n"
"color: YELLOW;\n"
"")
        self.label_4.setObjectName("label_4")
        changePrice.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changePrice)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 26))
        self.menubar.setObjectName("menubar")
        changePrice.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changePrice)
        self.statusbar.setObjectName("statusbar")
        changePrice.setStatusBar(self.statusbar)

        self.retranslateUi(changePrice)
        QtCore.QMetaObject.connectSlotsByName(changePrice)

    def retranslateUi(self, changePrice):
        _translate = QtCore.QCoreApplication.translate
        changePrice.setWindowTitle(_translate("changePrice", "Change Item Price"))
        self.save_price.setText(_translate("changePrice", "SAVE"))
        self.chngPrc_bfastBtn.setText(_translate("changePrice", "Breakfast"))
        self.chngPrc_lunchBtn.setText(_translate("changePrice", "Lunch"))
        self.chngPrc_snackBtn.setText(_translate("changePrice", "Snack"))
        self.label.setText(_translate("changePrice", "PRICE: P"))
        self.chngPrc_currentPrice.setText(_translate("changePrice", "0.00"))
        self.label_3.setText(_translate("changePrice", "NEW PRICE: P"))
        self.label_2.setText(_translate("changePrice", "FOOD: "))
        self.food_lbl.setText(_translate("changePrice", "None"))
        self.label_4.setText(_translate("changePrice", " VMES CANTEEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changePrice = QtWidgets.QMainWindow()
    ui = Ui_changePrice()
    ui.setupUi(changePrice)
    changePrice.show()
    sys.exit(app.exec_())
