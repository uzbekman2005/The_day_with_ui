from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from poliudisUi import *
from config import *
import sys
import pymysql.cursors

class PolyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PolyWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_connection()
        self.createTable()
        self.showQuestion()
        self.mainPoly()
        self.answers = []
        self.ui.btnOk.clicked.connect(self.addPressed)
        self.ansTextDis()
        self.ui.btnaddQuestion.clicked.connect(self.addQuestionPressed)
        self.ui.btnadd.clicked.connect(self.addQuestion)

    def db_connection(self):
        try:
            self.connection = pymysql.connect(host=host, user=user, database=database
                                              , password=password, port=port, charset="utf8mb4",
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print(ex)

    def createTable(self):
        try:
            sql = "CREATE TABLE IF NOT EXISTS polichudis(q_id int primary key auto_increment, " \
                  "question TEXT(500) NOT NULL, answer varchar(50) NOT NULL)"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                print("Table created")
        except Exception as ex:
            print(ex)

    def selectFromPolDatabase(self):
        try:
            sql = "SELECT * FROM polichudis"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as ex:
            print(ex)

    def showQuestion(self):
        all = self.selectFromPolDatabase()
        one = all[randint(0, len(all) - 1)]
        self.current_question = one["question"]
        self.current_answer = one["answer"]
        # print(self.current_question)
        # print(self.current_answer)

    def mainPoly(self):
        self.showQuestion()
        self.ui.labelquestion.setText(self.current_question)

    def ansTextDis(self, text="?"):
        self.mainPoly()
        answer = list(self.current_answer.lower())
        ansText = ["?" for j in range(len(answer))]
        print(ansText)
        if text in answer:
            if text == answer:
                ansText = list(text)
            else:
                if len(text) == 1 and text not in self.answers:
                    ansText[answer.index(text)] = text
                    self.answers.append(text)

        for i in range(len(answer)):
            if answer[i] in self.answers:
                ansText[i] = answer[i]
            else:
                ansText[i] = "?"
        if "".join(ansText) == "".join(answer):
            print("Congratulations")
            self.ui.btnOk.hide()
        self.ui.labelanswer.setText(" | ".join(ansText))
        self.ui.lanswer.setText("")

    def addPressed(self):
        text = self.ui.lanswer.text()
        if text != "":
            self.ansTextDis(text)


    # Add Questions
    def addQuestionPressed(self):
        # self.addQuestion()
        pass

    def addQuestion(self):
        question = self.ui.plainTextEdit.toPlainText().title()
        answer = self.ui.lineaddanswer.text().title()
        try:
            if question == "" or answer == "":
                raise ValueError
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO polichudis (question, answer) " \
                      "values(%s, %s)"
                cursor.execute(sql, (question, answer))
                self.ui.lineaddanswer.setText("")
                self.ui.plainTextEdit.setPlainText("")
        except Exception as ex:
            print(ex)
        finally:
            self.connection.commit()


def mainPolicudis():
    app = QApplication([])
    window = PolyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    mainPolicudis()
