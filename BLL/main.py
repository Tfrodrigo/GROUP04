Tin
        self.btn1.clicked.connect(self.conti)

    def conti(self):
        user = self.blank_usr.text()
        user = user.replace(" ","")
        print(user)
        
        exist = dh.AuthUser(user)
        print(exist)
        if (exist is True):
            username = user
            self.close()
            self.newWin = main2.Main()
            self.newWin.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR!")
            msg.setText(user+" Not Found! Try again")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())