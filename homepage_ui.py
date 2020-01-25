# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(1118, 677)
        home.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.menu_combo = QtWidgets.QComboBox(self.centralwidget)
        self.menu_combo.setGeometry(QtCore.QRect(20, 360, 471, 41))
        self.menu_combo.setStyleSheet("background: white")
        self.menu_combo.setObjectName("menu_combo")
        self.bf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bf_btn.setGeometry(QtCore.QRect(20, 260, 151, 61))
        self.bf_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.bf_btn.setObjectName("bf_btn")
        self.lun_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lun_btn.setGeometry(QtCore.QRect(190, 260, 151, 61))
        self.lun_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.lun_btn.setObjectName("lun_btn")
        self.snk_btn = QtWidgets.QPushButton(self.centralwidget)
        self.snk_btn.setGeometry(QtCore.QRect(360, 260, 151, 61))
        self.snk_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.snk_btn.setObjectName("snk_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 560, 151, 61))
        self.add_btn.setObjectName("add_btn")
        self.complete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.complete_btn.setGeometry(QtCore.QRect(910, 560, 151, 61))
        self.complete_btn.setObjectName("complete_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.order_list = QtWidgets.QListWidget(self.centralwidget)
        self.order_list.setGeometry(QtCore.QRect(570, 100, 511, 391))
        self.order_list.setStyleSheet("background: white")
        self.order_list.setObjectName("order_list")
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setGeometry(QtCore.QRect(900, 60, 181, 31))
        self.remove_btn.setObjectName("remove_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")
        self.price_lbl = QtWidgets.QLabel(self.centralwidget)
        self.price_lbl.setGeometry(QtCore.QRect(190, 490, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.price_lbl.setFont(font)
        self.price_lbl.setStyleSheet("color:white")
        self.price_lbl.setObjectName("price_lbl")
        self.total_cost = QtWidgets.QLabel(self.centralwidget)
        self.total_cost.setGeometry(QtCore.QRect(710, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.total_cost.setFont(font)
        self.total_cost.setStyleSheet("color:white")
        self.total_cost.setObjectName("total_cost")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(570, 60, 93, 31))
        self.reset_btn.setObjectName("reset_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 231, 91))
        self.label_3.setStyleSheet("image: url(:/newPrefix/VMES.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 26))
        self.menubar.setObjectName("menubar")
        home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(home)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "HOME"))
        self.label.setText(_translate("home", "<html><head/><body><p><span style=\" font-weight:600;\">VMES CANTEEN</span></p></body></html>"))
        self.bf_btn.setText(_translate("home", "Breakfast"))
        self.lun_btn.setText(_translate("home", "Lunch"))
        self.snk_btn.setText(_translate("home", "Snack"))
        self.add_btn.setText(_translate("home", "ADD "))
        self.complete_btn.setText(_translate("home", "COMPLETE"))
        self.label_4.setText(_translate("home", "TOTAL: P"))
        self.remove_btn.setText(_translate("home", "REMOVE "))
        self.label_5.setText(_translate("home", "PRICE:  P"))
        self.price_lbl.setText(_translate("home", "0.00"))
        self.total_cost.setText(_translate("home", "0.00"))
        self.reset_btn.setText(_translate("home", "RESET"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
