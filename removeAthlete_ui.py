# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeAthlete_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteAthlete(object):
    def setupUi(self, deleteAthlete):
        deleteAthlete.setObjectName("deleteAthlete")
        deleteAthlete.resize(471, 468)
        deleteAthlete.setStyleSheet("background: gray;")
        self.centralwidget = QtWidgets.QWidget(deleteAthlete)
        self.centralwidget.setObjectName("centralwidget")
        self.athlete_lbl = QtWidgets.QLabel(self.centralwidget)
        self.athlete_lbl.setGeometry(QtCore.QRect(30, 190, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.athlete_lbl.setFont(font)
        self.athlete_lbl.setObjectName("athlete_lbl")
        self.athlist_combo = QtWidgets.QComboBox(self.centralwidget)
        self.athlist_combo.setGeometry(QtCore.QRect(20, 130, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.athlist_combo.setFont(font)
        self.athlist_combo.setStyleSheet("background: rgb(200, 200, 200)")
        self.athlist_combo.setObjectName("athlist_combo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 30pt \"Modern No. 20\";\n"
"selection-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(0, 200, 0)\n"
"")
        self.label_2.setObjectName("label_2")
        self.deleteAthlete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAthlete_btn.setGeometry(QtCore.QRect(160, 320, 131, 51))
        self.deleteAthlete_btn.setStyleSheet("background: rgb(200, 200, 200)")
        self.deleteAthlete_btn.setObjectName("deleteAthlete_btn")
        deleteAthlete.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deleteAthlete)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 26))
        self.menubar.setObjectName("menubar")
        deleteAthlete.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(deleteAthlete)
        self.statusbar.setObjectName("statusbar")
        deleteAthlete.setStatusBar(self.statusbar)

        self.retranslateUi(deleteAthlete)
        QtCore.QMetaObject.connectSlotsByName(deleteAthlete)

    def retranslateUi(self, deleteAthlete):
        _translate = QtCore.QCoreApplication.translate
        deleteAthlete.setWindowTitle(_translate("deleteAthlete", "Remove Athlete"))
        self.athlete_lbl.setText(_translate("deleteAthlete", "ATHLETE"))
        self.label_2.setText(_translate("deleteAthlete", "VMES CANTEEN"))
        self.deleteAthlete_btn.setText(_translate("deleteAthlete", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteAthlete = QtWidgets.QMainWindow()
    ui = Ui_deleteAthlete()
    ui.setupUi(deleteAthlete)
    deleteAthlete.show()
    sys.exit(app.exec_())
