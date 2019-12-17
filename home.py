from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, os
from functools import partial

from handler import DataHandler

dh = DataHandler('VMES.db')

import Homepage

class Main(QtWidgets.QMainWindow, Homepage.Ui_home):
    def __init__(self):
        super(Main, self).__init__()
        b = "breakfast"
        l = "lunch"
        s = "snack"
        self.setupUi(self)
        self.total = 0
        self.choice = ""
        self.bf_btn.clicked.connect(self.breakfastMenu)
        self.lun_btn.clicked.connect(self.lunchMenu)
        self.snk_btn.clicked.connect(self.snackMenu)
        self.map = {}

    #def showMenu(self,mealTime):
    #	print("showMenu")
    #	self.map = {}
    #	self.menu_combo.clear()
    #	self.pricedMenu = dh.getMenu(mealTime)
    #	for x in self.pricedMenu:
    #		self.menu_combo.addItem(x[0])
    #		self.map[x[0]] = x[1]
    #	print("selfmap: ",self.map)
    #	f = self.menu_combo.currentText()
    #	print("f: ",f)
    #	self.menu_combo.activated.connect(self.showPrice)

    def breakfastMenu(self):
    	self.map = {}
    	self.menu_combo.clear()
    	self.pricedMenu = dh.getMenu("breakfast")
    	for x in self.pricedMenu:
    		self.menu_combo.addItem(x[0])
    		self.map[x[0]] = x[1]
    	print("selfmap: ",self.map)
    	self.menu_combo.view().pressed.connect(self.showPrice)

    def lunchMenu(self):
    	self.map = {}
    	self.menu_combo.clear()
    	self.pricedMenu = dh.getMenu("lunch")
    	for x in self.pricedMenu:
    		self.menu_combo.addItem(x[0])
    		self.map[x[0]] = x[1]
    	print("selfmap: ",self.map)
    	self.menu_combo.view().pressed.connect(self.showPrice)

    def snackMenu(self):
    	self.map = {}
    	self.menu_combo.clear()
    	self.pricedMenu = dh.getMenu("breakfast")
    	for x in self.pricedMenu:
    		self.menu_combo.addItem(x[0])
    		self.map[x[0]] = x[1]
    	print("selfmap: ",self.map)
    	self.menu_combo.view().pressed.connect(self.showPrice)

    def showPrice(self):
    	self.current_choice = ""
    	self.current_choice = self.menu_combo.currentText()
    	print("current choice:",self.current_choice)
    	print("showPrice")
    	
    	self.price = 0
    	print(self.map)
    	self.price = self.map[self.current_choice]
    	self.price_lbl.setText(str(self.price)+"0")
    	print("pricelbl")
    	self.add_btn.clicked.connect(partial(self.orderList,self.current_choice,self.price))

    def orderList(self,meal,cost):
    	print("orderList")
    	print(meal)
    	print(cost)
    	
    	self.total = self.total + cost
    	self.order_list.addItem(meal)
    	self.total_cost.setText(str(self.total))

    	self.complete_btn.clicked.connect(self.completeOrder)

    def completeOrder(self):
    	print("completeOrder")
    	self.msg = QMessageBox()
    	self.msg.setWindowTitle("ORDER SUCCESSFUL!")
    	self.msg.setText("Order has been completed!")
    	x = self.msg.exec()
    	app = QtWidgets.QApplication.instance()
    	app.closeAllWindows()
    	self.Win2 = Main()
    	self.Win2.show()
		
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())