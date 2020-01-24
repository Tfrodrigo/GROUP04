from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import enrollUser, home, accManagement, menuManagement, orderedItems, customerType, manageAthlete, athleteOrderedItems

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import admin_ui


class Main(QtWidgets.QMainWindow, admin_ui.Ui_adminPage):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)
		self.user_reg_btn.clicked.connect(self.enroll)
		self.hmpg_btn.clicked.connect(self.goHome)
		self.menu_mngBtn.clicked.connect(self.manageMenu)
		self.acc_mngBtn.clicked.connect(self.manageAccount)
		self.logout_btn.clicked.connect(self.end)
		self.totalEarn_btn.clicked.connect(self.showEarnings)
		self.manageAthlete_btn.clicked.connect(self.manageAth)
		self.orderedItems_btn.clicked.connect(self.orderedItemsAth)

	def goHome(self):
		self.win1 = customerType.Main()
		self.win1.show()

	def manageMenu(self):
		self.win2 = menuManagement.Main()
		self.win2.show()

	def showEarnings(self):
		self.win3 = orderedItems.Main()
		self.win3.show()

	def manageAth(self):
		self.win4 = manageAthlete.Main()
		self.win4.show()

	def orderedItemsAth(self):
		self.win5 = athleteOrderedItems.Main()
		self.win5.show()

	def enroll(self):
		self.win6 = enrollUser.Main()
		self.win6.show()

	def manageAccount(self):
		self.win7 = accManagement.Main()
		self.win7.show()
		
	def end(self):
		app = QtWidgets.QApplication.instance()
		app.closeAllWindows()
    
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	form = Main()
	form.show()
	sys.exit(app.exec_())