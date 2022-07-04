from PyQt6.QtWidgets import QApplication, QMainWindow
from config import *
from sighnupui import *
import sys
import pymysql.cursors

class SignUpWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SignUpWindow, self).__init__(parent)
        self.ui = Ui_Sign_up()
        self.ui.setupUi(self)
        self.db_connection()
        self.createTable()
        self.ui.btnsignup.clicked.connect(self.sign_up)

    def db_connection(self):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password,
                                          database=database, port=port, charset="utf8mb4",
                                         cursorclass=pymysql.cursors.DictCursor)
            print("connected")
        except Exception as ex:
            print(ex)

    def isRightEmail(self, email):
        return email.endswith("@gmail.com")


    def checkForErrors(self, f_name, email, username, password):
        self.resetError()
        if f_name == "":
            self.ui.lfname.setStyleSheet("color: rgb(246, 97, 81);")
            return False
        elif not self.isRightEmail(email):
            self.ui.lemail.setStyleSheet("color: rgb(246, 97, 81);")
            return False
        elif not self.isUniqueUsername(username):
            self.ui.lUsername.setStyleSheet("color: rgb(246, 97, 81);")
            return False
        elif password == "":
            self.ui.lpassword.setStyleSheet("color: rgb(246, 97, 81);")
            return False
        elif not self.ui.rbf.isChecked() and not self.ui.rbm.isChecked():
            self.ui.rbf.setStyleSheet("color: rgb(246, 97, 81);")
            self.ui.rbm.setStyleSheet("color: rgb(246, 97, 81);")
            return False
        return True

    def resetError(self):
        self.ui.rbf.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.rbm.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.lemail.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.lfname.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.lpassword.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.lUsername.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")


    def selectAllUsers(self):
        try:
            sql = "SELECT  * from users"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)

    def isUniqueUsername(self, username):
        usernames = list(map(lambda x:x["u_username"], self.selectAllUsers()))
        return not username in usernames

    def createTable(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "CREATE TABLE IF NOT EXISTS users(user_id int primary key auto_increment, " \
                      "u_fname varchar(50) NOT NULL, u_lname varchar(50), u_email varchar(50) NOT NULL, " \
                      "u_username varchar(50) not null, u_password varchar(50) NOT NULL, u_gender varchar(10) not null)"
                cursor.execute(sql)
                print("Table Created")
        except Exception as ex:
            print(ex)

    def sign_up(self):
        fname = self.ui.lfname.text()
        lname = self.ui.llname.text()
        email = self.ui.lemail.text()
        user_name = self.ui.lUsername.text()
        password = self.ui.lpassword.text()
        gender = self.ui.rbf.text() if self.ui.rbf.isChecked() else self.ui.rbm.text()
        if self.checkForErrors(fname, email, user_name, password):
            self.Insert(self.connection, fname, email, user_name, password,gender,lname=lname)
            self.clearLines()

    def clearLines(self):
        self.ui.lfname.setText("")
        self.ui.llname.setText("")
        self.ui.lemail.setText("")
        self.ui.lpassword.setText("")
        self.ui.lUsername.setText("")

    @staticmethod
    def Insert(connection, f_name, email, username, password, gender,lname=" "):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (u_fname, u_lname, u_email, u_username, u_password, u_gender) " \
                      "values(%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (f_name, lname, email, username,password, gender))
        except Exception as ex:
            print(ex)
        finally:
            connection.commit()


def mainSignUP():
    app = QApplication([])
    window = SignUpWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    mainSignUP()