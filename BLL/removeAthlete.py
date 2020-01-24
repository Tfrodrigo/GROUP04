from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial


sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import removeAthlete_ui

class Main(QtWidgets.QMainWindow, removeAthlete_ui.Ui_deleteAthlete):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.idMap = {}
        self.athletes = dh.getAllAthlete()
        for x in self.athletes:
            self.athlist_combo.addItem(x[1])
            self.idMap[x[1]] = x[0]

        self.athlist_combo.activated.connect(self.curAthlete)
        self.deleteAthlete_btn.clicked.connect(self.delSelected)

    def curAthlete(self):
        self.name = ""
        self.name = self.athlist_combo.currentText()

    def delSelected(self):
        self.name = self.athlist_combo.currentText()
        self.id = self.idMap[self.name]
        dh.delAthlete(self.id)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("SUCCESS")
        self.msg.setText(self.name+" is removed from the database")
        z = self.msg.exec()

        self.close()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())