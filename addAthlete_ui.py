# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAthlete_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAthlete(object):
    def setupUi(self, addAthlete):
        addAthlete.setObjectName("addAthlete")
        addAthlete.resize(735, 498)
        addAthlete.setStyleSheet("background: gray;")
        self.centralwidget = QtWidgets.QWidget(addAthlete)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.athlete_name = QtWidgets.QLineEdit(self.centralwidget)
        self.athlete_name.setGeometry(QtCore.QRect(120, 150, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.athlete_name.setFont(font)
        self.athlete_name.setStyleSheet("background: rgb(200, 200, 200)")
        self.athlete_name.setObjectName("athlete_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.student_number = QtWidgets.QLineEdit(self.centralwidget)
        self.student_number.setGeometry(QtCore.QRect(290, 210, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student_number.setFont(font)
        self.student_number.setStyleSheet("background: rgb(200, 200, 200)")
        self.student_number.setObjectName("student_number")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.allowance_line = QtWidgets.QLineEdit(self.centralwidget)
        self.allowance_line.setGeometry(QtCore.QRect(200, 270, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.allowance_line.setFont(font)
        self.allowance_line.setStyleSheet("background: rgb(200, 200, 200)")
        self.allowance_line.setObjectName("allowance_line")
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(280, 360, 151, 51))
        self.confirm_btn.setStyleSheet("background: rgb(200, 200, 200)")
        self.confirm_btn.setObjectName("confirm_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 30pt \"Modern No. 20\";\n"
"selection-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(0, 200, 0)\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 70, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"font:81 15pt \"Times New Roman\";\n"
"color: YELLOW;\n"
"")
        self.label_5.setObjectName("label_5")
        addAthlete.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addAthlete)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 26))
        self.menubar.setObjectName("menubar")
        addAthlete.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addAthlete)
        self.statusbar.setObjectName("statusbar")
        addAthlete.setStatusBar(self.statusbar)

        self.retranslateUi(addAthlete)
        QtCore.QMetaObject.connectSlotsByName(addAthlete)

    def retranslateUi(self, addAthlete):
        _translate = QtCore.QCoreApplication.translate
        addAthlete.setWindowTitle(_translate("addAthlete", "ADD NEW ATHLETE"))
        self.label.setText(_translate("addAthlete", "<html><head/><body><p><span style=\" font-weight:600;\">NAME</span></p></body></html>"))
        self.label_2.setText(_translate("addAthlete", "<html><head/><body><p><span style=\" font-weight:600;\">STUDENT NUMBER:</span></p></body></html>"))
        self.label_3.setText(_translate("addAthlete", "<html><head/><body><p><span style=\" font-weight:600;\">ALLOWANCE</span></p></body></html>"))
        self.confirm_btn.setText(_translate("addAthlete", "CONFIRM"))
        self.label_4.setText(_translate("addAthlete", "<html><head/><body><p><span style=\" font-weight:600;\">VMES CANTEEN</span></p></body></html>"))
        self.label_5.setText(_translate("addAthlete", "<html><head/><body><p><span style=\" font-weight:600;\">ADD NEW ATHLETE</span></p></body></html>"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addAthlete = QtWidgets.QMainWindow()
    ui = Ui_addAthlete()
    ui.setupUi(addAthlete)
    addAthlete.show()
    sys.exit(app.exec_())
