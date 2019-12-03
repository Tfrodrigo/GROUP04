import sqlite3

class DataHandler(object):
    username = ""
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
