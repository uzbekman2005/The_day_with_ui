from polychusback import *
from sighnupui import *
from config import *
from loginmain import *
from main1516 import *
from Thedaymainui import *
from person import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainTheday()
        self.ui.setupUi(self)
        self.current_user = None
        self.login = LoginWindow()
        self.signUp = SignUpWindow()
        self.puzzle1516 = None
        self.ui.btnlogin.clicked.connect(self.loginPressedInMain)
        self.ui.btnsignup.clicked.connect(self.signUpPressed)
        self.ui.btn1516.clicked.connect(self.puzzle1516Pressed)
        self.currentUser()
        self.ui.btnupdate.clicked.connect(self.updatePressed)

    def updatePressed(self):
        if self.current_user is not None:
            self.current_user = Person(self.current_user.get_userID())
            print("update pressed")
            self.showScore()

    def puzzle1516Pressed(self):
        if self.current_user != None:
            self.puzzle1516 = FifWindow(self.current_user.get_userID())
            self.puzzle1516.show()

        if self.current_user != None:
            self.showScore()

    def signUpPressed(self):
        self.signUp.show()

    def loginPressedInMain(self):
        self.login.show()
        self.login.ui.btnlogin.clicked.connect(self.currentUser)


    def currentUser(self):
        temp = self.login.getCurrentUser()
        if temp != None:
            self.current_user = temp
            self.showScore()
            self.login.hide()

    def showScore(self):
        self.ui.scoreDisplay.setText(str(self.current_user.get_score()))
        self.ui.curuser_username.setText(self.current_user.get_username())



def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()






