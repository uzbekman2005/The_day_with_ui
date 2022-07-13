from loginui import *
from config import *
from person import *
import pymysql.cursors
import sys


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.ui = Ui_mainlogin()
        self.ui.setupUi(self)
        self.current_user = None
        self.db_connection()
        self.ui.btnlogin.clicked.connect(self.loginPressed)

    def db_connection(self):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password,
                                              charset="utf8mb4", port=port, database=database,
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print(ex)

    def selectAllUsers(self, username, password):
        try:
            sql = f"SELECT  * from users where u_username = '{username}' and u_password = '{password}'"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            # self.errReset()

            return False

    def reportError(self):
        self.ui.loginpassword.setStyleSheet("color: rgb(246, 97, 81);")
        self.ui.lloginUsername.setStyleSheet("color: rgb(246, 97, 81);")

    def errReset(self):
        self.ui.loginpassword.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.ui.lloginUsername.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")

    def loginPressed(self):
        username = self.ui.lloginUsername.text()
        password = self.ui.loginpassword.text()
        user_cur = self.selectAllUsers(username, password)
        if user_cur:
            self.current_user = Person(user_cur[0]["user_id"])
            print(self.current_user.get_f_name())
        else:
            self.current_user = None
            self.reportError()
            print("NOOO")

    def getCurrentUser(self):
        return self.current_user

def main():
    app = QApplication([])
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

