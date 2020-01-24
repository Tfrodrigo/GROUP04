from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem
import sys
from functools import partial

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import viewAllowance_ui

class Main(QtWidgets.QMainWindow, viewAllowance_ui.Ui_viewAllowance):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.resetAllowance_btn.clicked.connect(self.resetAllowance)
        self.idMap = {}
        self.allowanceMap = {}
        self.remainingMap = {}
        self.n = []         #name
        self.a = []         #allowance
        self.r = []         #remaining
        self.results = dh.getAllAthlete()

        for x in self.results:
            self.idMap[x[1]] = x[0]
            self.allowanceMap[x[1]] = x[4]
            self.remainingMap[x[1]] = x[3]
            self.n.append(x[1])
            self.a.append(x[4])
            self.r.append(x[3])

        print(self.a)
        print(self.r)



        self.tableWidget.setRowCount(len(self.n))
        self.tableWidget.setColumnCount(3)

        m = 0
        for a in self.n:
            self.tableWidget.setItem(m,0, QTableWidgetItem(a))

            m += 1

        m = 0
        for b in self.a:
            self.tableWidget.setItem(m,1, QTableWidgetItem(str(b)))
            m += 1

        m = 0
        for c in self.r:
            self.tableWidget.setItem(m,2, QTableWidgetItem(str(c)))
            m += 1

    def resetAllowance(self):
        dh.resetAllowance()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("SUCCESS")
        self.msg.setText("Allowance Restored")
        x = self.msg.exec()
        self.end()
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