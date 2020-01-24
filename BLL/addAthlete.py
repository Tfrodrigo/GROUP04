from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial


sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import addAthlete_ui

class Main(QtWidgets.QMainWindow, addAthlete_ui.Ui_addAthlete):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.confirm_btn.clicked.connect(self.takeAthleteInfo)

    def takeAthleteInfo(self):
        name = self.athlete_name.text()
        studentNum = self.student_number.text()
        allowance = self.allowance_line.text()

        if(name == "" or studentNum == "" or allowance == ""):
            self.err = QMessageBox()
            self.err.setIcon(QMessageBox.Warning)
            self.err.setWindowTitle("WARNING!")
            self.err.setText("Incomplete Information!")
            x = self.err.exec()
        else:
            studentNum = int(studentNum)
            allowance = float(allowance)
            dh.newAthlete(name,studentNum,allowance)
            self.msg = QMessageBox()
            self.msg.setWindowTitle("SUCCESS")
            self.msg.setText("Successfully added "+name)
            z = self.msg.exec()

        
        
        
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())