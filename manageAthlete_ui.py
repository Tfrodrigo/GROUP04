# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageAthlete_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manageAthlete(object):
    def setupUi(self, manageAthlete):
        manageAthlete.setObjectName("manageAthlete")
        manageAthlete.resize(302, 394)
        manageAthlete.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(manageAthlete)
        self.centralwidget.setObjectName("centralwidget")
        self.add_athleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.add_athleteBtn.setGeometry(QtCore.QRect(40, 100, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_athleteBtn.setFont(font)
        self.add_athleteBtn.setObjectName("add_athleteBtn")
        self.rem_athleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rem_athleteBtn.setGeometry(QtCore.QRect(40, 260, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rem_athleteBtn.setFont(font)
        self.rem_athleteBtn.setObjectName("rem_athleteBtn")
        self.viewAllowance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.viewAllowance_btn.setGeometry(QtCore.QRect(40, 180, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewAllowance_btn.setFont(font)
        self.viewAllowance_btn.setObjectName("viewAllowance_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.label.setStyleSheet("image: url(:/newPrefix/VMES.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 131, 61))
        self.label_2.setStyleSheet("font: 75 17pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        manageAthlete.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(manageAthlete)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 26))
        self.menubar.setObjectName("menubar")
        manageAthlete.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(manageAthlete)
        self.statusbar.setObjectName("statusbar")
        manageAthlete.setStatusBar(self.statusbar)

        self.retranslateUi(manageAthlete)
        QtCore.QMetaObject.connectSlotsByName(manageAthlete)

    def retranslateUi(self, manageAthlete):
        _translate = QtCore.QCoreApplication.translate
        manageAthlete.setWindowTitle(_translate("manageAthlete", "Manage Athlete"))
        self.add_athleteBtn.setText(_translate("manageAthlete", "ADD ATHLETE"))
        self.rem_athleteBtn.setText(_translate("manageAthlete", "REMOVE ATHLETE"))
        self.viewAllowance_btn.setText(_translate("manageAthlete", "VIEW ALLOWANCE"))
        self.label_2.setText(_translate("manageAthlete", "CANTEEN"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manageAthlete = QtWidgets.QMainWindow()
    ui = Ui_manageAthlete()
    ui.setupUi(manageAthlete)
    manageAthlete.show()
    sys.exit(app.exec_())
