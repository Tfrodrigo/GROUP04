# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMenu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMenuItem(object):
    def setupUi(self, addMenuItem):
        addMenuItem.setObjectName("addMenuItem")
        addMenuItem.resize(615, 507)
        font = QtGui.QFont()
        font.setPointSize(14)
        addMenuItem.setFont(font)
        addMenuItem.setStyleSheet("background: rgb(200,100,100)")
        self.centralwidget = QtWidgets.QWidget(addMenuItem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addMenu_mealCombo = QtWidgets.QComboBox(self.centralwidget)
        self.addMenu_mealCombo.setGeometry(QtCore.QRect(170, 90, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addMenu_mealCombo.setFont(font)
        self.addMenu_mealCombo.setStyleSheet("background-color: rgb(250, 100, 100);")
        self.addMenu_mealCombo.setObjectName("addMenu_mealCombo")
        self.addMenu_mealCombo.addItem("")
        self.addMenu_mealCombo.addItem("")
        self.addMenu_mealCombo.addItem("")
        self.chosen_meal = QtWidgets.QLabel(self.centralwidget)
        self.chosen_meal.setGeometry(QtCore.QRect(200, 150, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chosen_meal.setFont(font)
        self.chosen_meal.setObjectName("chosen_meal")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.new_menuItem = QtWidgets.QLineEdit(self.centralwidget)
        self.new_menuItem.setGeometry(QtCore.QRect(10, 250, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_menuItem.setFont(font)
        self.new_menuItem.setStyleSheet("background-color: rgb(250, 100, 100);")
        self.new_menuItem.setObjectName("new_menuItem")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.add_price = QtWidgets.QLineEdit(self.centralwidget)
        self.add_price.setGeometry(QtCore.QRect(120, 320, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_price.setFont(font)
        self.add_price.setStyleSheet("background-color: rgb(250, 100, 100);")
        self.add_price.setObjectName("add_price")
        self.save_menuItem = QtWidgets.QPushButton(self.centralwidget)
        self.save_menuItem.setGeometry(QtCore.QRect(240, 390, 131, 51))
        self.save_menuItem.setStyleSheet("background-color: rgb(250, 100, 100);")
        self.save_menuItem.setObjectName("save_menuItem")
        self.chosen_meal_2 = QtWidgets.QLabel(self.centralwidget)
        self.chosen_meal_2.setGeometry(QtCore.QRect(140, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chosen_meal_2.setFont(font)
        self.chosen_meal_2.setObjectName("chosen_meal_2")
        addMenuItem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addMenuItem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 26))
        self.menubar.setObjectName("menubar")
        addMenuItem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addMenuItem)
        self.statusbar.setObjectName("statusbar")
        addMenuItem.setStatusBar(self.statusbar)

        self.retranslateUi(addMenuItem)
        QtCore.QMetaObject.connectSlotsByName(addMenuItem)

    def retranslateUi(self, addMenuItem):
        _translate = QtCore.QCoreApplication.translate
        addMenuItem.setWindowTitle(_translate("addMenuItem", "Add Menu Item"))
        self.label.setText(_translate("addMenuItem", "<html><head/><body><p><span style=\" font-weight:600;\">Meal Time:</span></p></body></html>"))
        self.addMenu_mealCombo.setItemText(0, _translate("addMenuItem", "breakfast"))
        self.addMenu_mealCombo.setItemText(1, _translate("addMenuItem", "lunch"))
        self.addMenu_mealCombo.setItemText(2, _translate("addMenuItem", "snack"))
        self.chosen_meal.setText(_translate("addMenuItem", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Breakfast</span></p></body></html>"))
        self.label_3.setText(_translate("addMenuItem", "<html><head/><body><p><span style=\" font-weight:600;\">Enter New Item Below</span></p></body></html>"))
        self.label_4.setText(_translate("addMenuItem", "<html><head/><body><p><span style=\" font-weight:600;\">Price: P</span></p></body></html>"))
        self.save_menuItem.setText(_translate("addMenuItem", "SAVE"))
        self.chosen_meal_2.setText(_translate("addMenuItem", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">VMES CANTEEN</span></p></body></html>"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addMenuItem = QtWidgets.QMainWindow()
    ui = Ui_addMenuItem()
    ui.setupUi(addMenuItem)
    addMenuItem.show()
    sys.exit(app.exec_())
