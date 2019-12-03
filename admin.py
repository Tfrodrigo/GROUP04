from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from handler import DataHandler

dh = DataHandler('VMES.db')

import temp_admin

class Main(QtWidgets.QMainWindow, temp_admin.Ui_adminPage):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())