from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial
from random import randint

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import homepageAthlete_ui

class Main(QtWidgets.QMainWindow, homepageAthlete_ui.Ui_home):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.allAthlete = dh.getAllAthlete()
        self.idMap = {}
        self.allowanceMap = {}
        self.athlete = ""
        for x in self.allAthlete:
            self.athlete_combo.addItem(x[1])
            self.idMap[x[1]] = x[0]
            self.allowanceMap[x[1]] = x[3]

        self.athlete_combo.activated.connect(self.greetAthlete)

        self.total = 0
        self.bf_btn.clicked.connect(partial(self.showMenu,"breakfast"))
        self.lun_btn.clicked.connect(partial(self.showMenu,"lunch"))
        self.snk_btn.clicked.connect(partial(self.showMenu,"snack"))
        self.map = {}
        self.lstmap = {}
        self.idmap = {}
        self.final_list = []
        self.current_choice = ""
        self.price = 0
        self.listCount  = 0
        self.menu_combo.activated.connect(self.showPrice)
        self.complete_btn.clicked.connect(self.completeOrder)
        self.remove_btn.clicked.connect(self.removeItem)
        self.add_btn.clicked.connect(self.orderList)
        self.reset_btn.clicked.connect(self.resetOrder)

    def greetAthlete(self):
        #self.athlete = ""
        self.athlete = self.athlete_combo.currentText()
        self.athlete_lbl.setText(self.athlete)
        self.remaining_allowance.setText(str(self.allowanceMap[self.athlete]))

    def showMenu(self,mealTime):
        print("showMenu")
        self.map = {}
        self.menu_combo.clear()
        self.pricedMenu = dh.getMenu(mealTime)
        for x in self.pricedMenu:
            self.menu_combo.addItem(x[0])
            self.map[x[0]] = x[1]
        print("selfmap: ",self.map)
        f = self.menu_combo.currentText()
        print("f: ",f)

    def showPrice(self):
        self.current_choice = ""
        self.current_choice = self.menu_combo.currentText()
        print(self.map)
        print("current choice:",self.current_choice)
        print("showPrice")
        
        self.price = 0
        print(self.map)
        self.price = self.map[self.current_choice]
        self.price_lbl.setText(str(self.price)+"0")
        print("pricelbl")

    def orderList(self):
        print("orderList")
        print(self.current_choice)
        print(self.price)
        if(self.current_choice == ""):
            self.err1 = QMessageBox()
            self.err1.setIcon(QMessageBox.Warning)
            self.err1.setWindowTitle("ERROR")
            self.err1.setText("NO ORDER YET!")
            z= self.err1.exec()
        else:
            self.total = self.total + self.price
            self.order_list.addItem(self.current_choice)
            self.listCount += 1
            self.lstmap[self.current_choice]=self.price
            self.total_cost.setText(str(self.total))

            if(self.total > self.allowanceMap[self.athlete]):
                self.remaining_allowance.setStyleSheet("color: rgb(255, 0, 0);")


    def removeItem(self):
        print("removeItem")
        print(self.lstmap)
        listItems=self.order_list.selectedItems()
        self.listCount -= 1
        if not listItems: return        
        for item in listItems:
            s = self.order_list.takeItem(self.order_list.row(item))
            self.total = self.total - self.lstmap[item.text()]  
            self.total_cost.setText(str(self.total))
            if(self.total < self.allowanceMap[self.athlete]):
                self.remaining_allowance.setStyleSheet("color: rgb(0, 0, 0);")



    def completeOrder(self):
        print("completeOrder")
        self.value = randint(0, 9)
        if(self.listCount == 0):
            self.err1 = QMessageBox()
            self.err1.setIcon(QMessageBox.Warning)
            self.err1.setWindowTitle("ERROR")
            self.err1.setText("NO ORDER YET!")
            x= self.err1.exec()
        else:

            if(self.total < self.allowanceMap[self.athlete]):
                self.allowanceMap[self.athlete] = self.allowanceMap[self.athlete]-self.total

                for index in range(self.order_list.count()):
                    print("ath: ",self.athlete)
                    dh.saveAthleteOrder(str(self.order_list.item(index).text()),self.lstmap[str(self.order_list.item(index).text())],str(self.athlete_combo.currentText()),self.value)
        
                print(self.idMap[self.athlete])
                dh.updateRemaining(int(self.idMap[self.athlete]),float(self.allowanceMap[self.athlete]))
                self.msg = QMessageBox()
                self.msg.setWindowTitle("ORDER SUCCESSFUL!")
                self.msg.setText("Order has been completed!")
                y = self.msg.exec()
                print("end")
                self.resetOrder()
            else:
                self.err2 = QMessageBox()
                self.err2.setIcon(QMessageBox.Warning)
                self.err2.setWindowTitle("ERROR")
                self.err2.setText("Not Enough Balance! Switch to Regular Mode for excess items")
                z= self.err2.exec()

    def resetOrder(self):
        self.close()
        self.win2 = Main()
        self.win2.show()
    
    
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())