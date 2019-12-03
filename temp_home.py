# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(841, 596)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 721, 421))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("homepic.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 26))
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
        self.label.setText(_translate("home", "VMES CANTEEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
