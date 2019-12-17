import sqlite3

class DataHandler(object):
    username = ""
    glob_table =""
    def __init__(self, db_file):
        self.dh = sqlite3.connect(db_file)
        self.c = self.dh.cursor()

    def AuthUser(self, user):
        print(user)
        DataHandler.username = user
        self.c.execute("SELECT ID FROM users WHERE username=?", (user,))
        id = self.c.fetchone()
        print(id)
        if id is None:
            return False
        else:
            return True

    def AuthPass(self):
        self.c.execute("SELECT pass FROM users WHERE username=?", (DataHandler.username,))
        password, = self.c.fetchone()
        self.c.execute("SELECT job FROM users WHERE username=?", (DataHandler.username,))
        jobPosition, = self.c.fetchone()
        return password, jobPosition

    def getMenu(self, table):
        DataHandler.glob_table = table
        self.sql = "SELECT menu, price FROM "+ table
        self.c.execute(self.sql)
        results = self.c.fetchall()
        return results

    def AddUser(self,newUser,passWord,job):
        self.c.execute("INSERT INTO users (username, pass, job) VALUES (?, ?, ?)",(newUser,passWord,job))
        self.dh.commit()
#menu = a.getMenu('breakfast')


#price = a.getPrice('Tapsi')
#print(price)