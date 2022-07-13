from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from sudokoui import *
from sudokobase import *
from main1516 import *
import sys


class SudokoWindow(QMainWindow):
    def __init__(self,  user, parent=None):
        super().__init__(parent)
        self.user = user
        self.ui = Ui_sudoko()
        self.ui.setupUi(self)
        self.corrects = []
        self.rightSudoko = sudoko1
        self.pencil = [self.ui.btn1, self.ui.btn1_2, self.ui.btn1_3, self.ui.btn1_4, self.ui.btn1_5,
                       self.ui.btn1_6, self.ui.btn1_7, self.ui.btn1_8, self.ui.btn1_9, self.ui.btn1_10,
                       self.ui.btn1_11, self.ui.btn1_12, self.ui.btn1_13, self.ui.btn1_14, self.ui.btn1_15,
                       self.ui.btn1_16, self.ui.btn1_17, self.ui.btn1_18, self.ui.btn1_19, self.ui.btn1_20,
                       self.ui.btn1_21, self.ui.btn1_22, self.ui.btn1_23, self.ui.btn1_24,
                       self.ui.btn1_25, self.ui.btn1_26, self.ui.btn1_27, self.ui.btn1_28, self.ui.btn1_29,
                       self.ui.btn1_30, self.ui.btn1_31, self.ui.btn1_32, self.ui.btn1_33, self.ui.btn1_34,
                       self.ui.btn1_35, self.ui.btn1_36, self.ui.btn1_37, self.ui.btn1_38, self.ui.btn1_39,
                       self.ui.btn1_40, self.ui.btn1_41, self.ui.btn1_42, self.ui.btn1_43, self.ui.btn1_44,
                       self.ui.btn1_45, self.ui.btn1_46, self.ui.btn1_47, self.ui.btn1_48, self.ui.btn1_4_9,
                       self.ui.btn1_50, self.ui.btn1_51, self.ui.btn1_52, self.ui.btn1_53, self.ui.btn1_54,
                       self.ui.btn1_5_5, self.ui.btn1_56, self.ui.btn1_57, self.ui.btn1_58, self.ui.btn1_59,
                       self.ui.btn1_60, self.ui.btn1_61, self.ui.btn1_62, self.ui.btn1_63, self.ui.btn1_158,
                       self.ui.btn1_159, self.ui.btn1_160, self.ui.btn1_161, self.ui.btn1_162, self.ui.btn1_163,
                       self.ui.btn1_164, self.ui.btn1_165, self.ui.btn1_166, self.ui.btn1_167, self.ui.btn1_168,
                       self.ui.btn1_169, self.ui.btn1_170, self.ui.btn1_171, self.ui.btn1_172, self.ui.btn1_173,
                       self.ui.btn1_174, self.ui.btn1_175]

        self.lines = [self.ui.line1, self.ui.line1_2, self.ui.line1_3, self.ui.line1_4, self.ui.line1_5,
                       self.ui.line1_6, self.ui.line1_7, self.ui.line1_8, self.ui.line1_9, self.ui.line1_10,
                       self.ui.line1_11, self.ui.line1_12, self.ui.line1_13, self.ui.line1_14, self.ui.line1_15,
                       self.ui.line1_16, self.ui.line1_17, self.ui.line1_18, self.ui.line1_19, self.ui.line1_20,
                       self.ui.line1_21, self.ui.line1_22, self.ui.line1_23, self.ui.line1_24,
                       self.ui.line1_25, self.ui.line1_26, self.ui.line1_27, self.ui.line1_28, self.ui.line1_29,
                       self.ui.line1_30, self.ui.line1_31, self.ui.line1_32, self.ui.line1_33, self.ui.line1_34,
                       self.ui.line1_35, self.ui.line1_36, self.ui.line1_37, self.ui.line1_38, self.ui.line1_39,
                       self.ui.line1_40, self.ui.line1_41, self.ui.line1_42, self.ui.line1_43, self.ui.line1_44,
                       self.ui.line1_45, self.ui.line1_46, self.ui.line1_47, self.ui.line1_48, self.ui.line1_4_9,
                       self.ui.line1_50, self.ui.line1_51, self.ui.line1_52, self.ui.line1_53, self.ui.line1_54,
                       self.ui.line1_5_5, self.ui.line1_56, self.ui.line1_57, self.ui.line1_58, self.ui.line1_59,
                       self.ui.line1_60, self.ui.line1_61, self.ui.line1_62, self.ui.line1_63, self.ui.line1_158,
                       self.ui.line1_159, self.ui.line1_160, self.ui.line1_161, self.ui.line1_162, self.ui.line1_163,
                       self.ui.line1_164, self.ui.line1_165, self.ui.line1_166, self.ui.line1_167, self.ui.line1_168,
                       self.ui.line1_169, self.ui.line1_170, self.ui.line1_171, self.ui.line1_172, self.ui.line1_173,
                       self.ui.line1_174, self.ui.line1_175]
        self.start()

        self.pencil[0].clicked.connect(lambda: self.pencilPressed(self.pencil[0]))
        self.pencil[1].clicked.connect(lambda: self.pencilPressed(self.pencil[1]))
        self.pencil[2].clicked.connect(lambda: self.pencilPressed(self.pencil[2]))
        self.pencil[3].clicked.connect(lambda: self.pencilPressed(self.pencil[3]))
        self.pencil[4].clicked.connect(lambda: self.pencilPressed(self.pencil[4]))
        self.pencil[5].clicked.connect(lambda: self.pencilPressed(self.pencil[5]))
        self.pencil[6].clicked.connect(lambda: self.pencilPressed(self.pencil[6]))
        self.pencil[7].clicked.connect(lambda: self.pencilPressed(self.pencil[7]))
        self.pencil[8].clicked.connect(lambda: self.pencilPressed(self.pencil[8]))
        self.pencil[9].clicked.connect(lambda: self.pencilPressed(self.pencil[9]))
        self.pencil[10].clicked.connect(lambda: self.pencilPressed(self.pencil[10]))
        self.pencil[11].clicked.connect(lambda: self.pencilPressed(self.pencil[11]))
        self.pencil[12].clicked.connect(lambda: self.pencilPressed(self.pencil[12]))
        self.pencil[13].clicked.connect(lambda: self.pencilPressed(self.pencil[13]))
        self.pencil[14].clicked.connect(lambda: self.pencilPressed(self.pencil[14]))
        self.pencil[15].clicked.connect(lambda: self.pencilPressed(self.pencil[15]))
        self.pencil[16].clicked.connect(lambda: self.pencilPressed(self.pencil[16]))
        self.pencil[17].clicked.connect(lambda: self.pencilPressed(self.pencil[17]))
        self.pencil[18].clicked.connect(lambda: self.pencilPressed(self.pencil[18]))
        self.pencil[19].clicked.connect(lambda: self.pencilPressed(self.pencil[19]))
        self.pencil[20].clicked.connect(lambda: self.pencilPressed(self.pencil[20]))
        self.pencil[21].clicked.connect(lambda: self.pencilPressed(self.pencil[21]))
        self.pencil[22].clicked.connect(lambda: self.pencilPressed(self.pencil[22]))
        self.pencil[23].clicked.connect(lambda: self.pencilPressed(self.pencil[23]))
        self.pencil[24].clicked.connect(lambda: self.pencilPressed(self.pencil[24]))
        self.pencil[25].clicked.connect(lambda: self.pencilPressed(self.pencil[25]))
        self.pencil[26].clicked.connect(lambda: self.pencilPressed(self.pencil[26]))
        self.pencil[27].clicked.connect(lambda: self.pencilPressed(self.pencil[27]))
        self.pencil[28].clicked.connect(lambda: self.pencilPressed(self.pencil[28]))
        self.pencil[29].clicked.connect(lambda: self.pencilPressed(self.pencil[29]))
        self.pencil[30].clicked.connect(lambda: self.pencilPressed(self.pencil[30]))
        self.pencil[31].clicked.connect(lambda: self.pencilPressed(self.pencil[31]))
        self.pencil[32].clicked.connect(lambda: self.pencilPressed(self.pencil[32]))
        self.pencil[33].clicked.connect(lambda: self.pencilPressed(self.pencil[33]))
        self.pencil[34].clicked.connect(lambda: self.pencilPressed(self.pencil[34]))
        self.pencil[35].clicked.connect(lambda: self.pencilPressed(self.pencil[35]))
        self.pencil[36].clicked.connect(lambda: self.pencilPressed(self.pencil[36]))
        self.pencil[37].clicked.connect(lambda: self.pencilPressed(self.pencil[37]))
        self.pencil[38].clicked.connect(lambda: self.pencilPressed(self.pencil[38]))
        self.pencil[39].clicked.connect(lambda: self.pencilPressed(self.pencil[39]))
        self.pencil[40].clicked.connect(lambda: self.pencilPressed(self.pencil[40]))
        self.pencil[41].clicked.connect(lambda: self.pencilPressed(self.pencil[41]))
        self.pencil[42].clicked.connect(lambda: self.pencilPressed(self.pencil[42]))
        self.pencil[43].clicked.connect(lambda: self.pencilPressed(self.pencil[43]))
        self.pencil[44].clicked.connect(lambda: self.pencilPressed(self.pencil[44]))
        self.pencil[45].clicked.connect(lambda: self.pencilPressed(self.pencil[45]))
        self.pencil[46].clicked.connect(lambda: self.pencilPressed(self.pencil[46]))
        self.pencil[47].clicked.connect(lambda: self.pencilPressed(self.pencil[47]))
        self.pencil[48].clicked.connect(lambda: self.pencilPressed(self.pencil[48]))
        self.pencil[49].clicked.connect(lambda: self.pencilPressed(self.pencil[49]))
        self.pencil[50].clicked.connect(lambda: self.pencilPressed(self.pencil[50]))
        self.pencil[51].clicked.connect(lambda: self.pencilPressed(self.pencil[51]))
        self.pencil[52].clicked.connect(lambda: self.pencilPressed(self.pencil[52]))
        self.pencil[53].clicked.connect(lambda: self.pencilPressed(self.pencil[53]))
        self.pencil[54].clicked.connect(lambda: self.pencilPressed(self.pencil[54]))
        self.pencil[55].clicked.connect(lambda: self.pencilPressed(self.pencil[55]))
        self.pencil[56].clicked.connect(lambda: self.pencilPressed(self.pencil[56]))
        self.pencil[57].clicked.connect(lambda: self.pencilPressed(self.pencil[57]))
        self.pencil[58].clicked.connect(lambda: self.pencilPressed(self.pencil[58]))
        self.pencil[59].clicked.connect(lambda: self.pencilPressed(self.pencil[59]))
        self.pencil[60].clicked.connect(lambda: self.pencilPressed(self.pencil[60]))
        self.pencil[61].clicked.connect(lambda: self.pencilPressed(self.pencil[61]))
        self.pencil[62].clicked.connect(lambda: self.pencilPressed(self.pencil[62]))
        self.pencil[63].clicked.connect(lambda: self.pencilPressed(self.pencil[63]))
        self.pencil[64].clicked.connect(lambda: self.pencilPressed(self.pencil[64]))
        self.pencil[65].clicked.connect(lambda: self.pencilPressed(self.pencil[65]))
        self.pencil[66].clicked.connect(lambda: self.pencilPressed(self.pencil[66]))
        self.pencil[67].clicked.connect(lambda: self.pencilPressed(self.pencil[67]))
        self.pencil[68].clicked.connect(lambda: self.pencilPressed(self.pencil[68]))
        self.pencil[69].clicked.connect(lambda: self.pencilPressed(self.pencil[69]))
        self.pencil[70].clicked.connect(lambda: self.pencilPressed(self.pencil[70]))
        self.pencil[71].clicked.connect(lambda: self.pencilPressed(self.pencil[71]))
        self.pencil[72].clicked.connect(lambda: self.pencilPressed(self.pencil[72]))
        self.pencil[73].clicked.connect(lambda: self.pencilPressed(self.pencil[73]))
        self.pencil[74].clicked.connect(lambda: self.pencilPressed(self.pencil[74]))
        self.pencil[75].clicked.connect(lambda: self.pencilPressed(self.pencil[75]))
        self.pencil[76].clicked.connect(lambda: self.pencilPressed(self.pencil[76]))
        self.pencil[77].clicked.connect(lambda: self.pencilPressed(self.pencil[77]))
        self.pencil[78].clicked.connect(lambda: self.pencilPressed(self.pencil[78]))
        self.pencil[79].clicked.connect(lambda: self.pencilPressed(self.pencil[79]))
        self.pencil[80].clicked.connect(lambda: self.pencilPressed(self.pencil[80]))


        self.lines[0].textChanged.connect(lambda: self.lineChanged(self.lines[0]))
        self.lines[1].textChanged.connect(lambda: self.lineChanged(self.lines[1]))
        self.lines[2].textChanged.connect(lambda: self.lineChanged(self.lines[2]))
        self.lines[3].textChanged.connect(lambda: self.lineChanged(self.lines[3]))
        self.lines[4].textChanged.connect(lambda: self.lineChanged(self.lines[4]))
        self.lines[5].textChanged.connect(lambda: self.lineChanged(self.lines[5]))
        self.lines[6].textChanged.connect(lambda: self.lineChanged(self.lines[6]))
        self.lines[7].textChanged.connect(lambda: self.lineChanged(self.lines[7]))
        self.lines[8].textChanged.connect(lambda: self.lineChanged(self.lines[8]))
        self.lines[9].textChanged.connect(lambda: self.lineChanged(self.lines[9]))
        self.lines[10].textChanged.connect(lambda: self.lineChanged(self.lines[10]))
        self.lines[11].textChanged.connect(lambda: self.lineChanged(self.lines[11]))
        self.lines[12].textChanged.connect(lambda: self.lineChanged(self.lines[12]))
        self.lines[13].textChanged.connect(lambda: self.lineChanged(self.lines[13]))
        self.lines[14].textChanged.connect(lambda: self.lineChanged(self.lines[14]))
        self.lines[15].textChanged.connect(lambda: self.lineChanged(self.lines[15]))
        self.lines[16].textChanged.connect(lambda: self.lineChanged(self.lines[16]))
        self.lines[17].textChanged.connect(lambda: self.lineChanged(self.lines[17]))
        self.lines[18].textChanged.connect(lambda: self.lineChanged(self.lines[18]))
        self.lines[19].textChanged.connect(lambda: self.lineChanged(self.lines[19]))
        self.lines[20].textChanged.connect(lambda: self.lineChanged(self.lines[20]))
        self.lines[21].textChanged.connect(lambda: self.lineChanged(self.lines[21]))
        self.lines[22].textChanged.connect(lambda: self.lineChanged(self.lines[22]))
        self.lines[23].textChanged.connect(lambda: self.lineChanged(self.lines[23]))
        self.lines[24].textChanged.connect(lambda: self.lineChanged(self.lines[24]))
        self.lines[25].textChanged.connect(lambda: self.lineChanged(self.lines[25]))
        self.lines[26].textChanged.connect(lambda: self.lineChanged(self.lines[26]))
        self.lines[27].textChanged.connect(lambda: self.lineChanged(self.lines[27]))
        self.lines[28].textChanged.connect(lambda: self.lineChanged(self.lines[28]))
        self.lines[29].textChanged.connect(lambda: self.lineChanged(self.lines[29]))
        self.lines[30].textChanged.connect(lambda: self.lineChanged(self.lines[30]))
        self.lines[31].textChanged.connect(lambda: self.lineChanged(self.lines[31]))
        self.lines[32].textChanged.connect(lambda: self.lineChanged(self.lines[32]))
        self.lines[33].textChanged.connect(lambda: self.lineChanged(self.lines[33]))
        self.lines[34].textChanged.connect(lambda: self.lineChanged(self.lines[34]))
        self.lines[35].textChanged.connect(lambda: self.lineChanged(self.lines[35]))
        self.lines[36].textChanged.connect(lambda: self.lineChanged(self.lines[36]))
        self.lines[37].textChanged.connect(lambda: self.lineChanged(self.lines[37]))
        self.lines[38].textChanged.connect(lambda: self.lineChanged(self.lines[38]))
        self.lines[39].textChanged.connect(lambda: self.lineChanged(self.lines[39]))
        self.lines[40].textChanged.connect(lambda: self.lineChanged(self.lines[40]))
        self.lines[41].textChanged.connect(lambda: self.lineChanged(self.lines[41]))
        self.lines[42].textChanged.connect(lambda: self.lineChanged(self.lines[42]))
        self.lines[43].textChanged.connect(lambda: self.lineChanged(self.lines[43]))
        self.lines[44].textChanged.connect(lambda: self.lineChanged(self.lines[44]))
        self.lines[45].textChanged.connect(lambda: self.lineChanged(self.lines[45]))
        self.lines[46].textChanged.connect(lambda: self.lineChanged(self.lines[46]))
        self.lines[47].textChanged.connect(lambda: self.lineChanged(self.lines[47]))
        self.lines[48].textChanged.connect(lambda: self.lineChanged(self.lines[48]))
        self.lines[49].textChanged.connect(lambda: self.lineChanged(self.lines[49]))
        self.lines[50].textChanged.connect(lambda: self.lineChanged(self.lines[50]))
        self.lines[51].textChanged.connect(lambda: self.lineChanged(self.lines[51]))
        self.lines[52].textChanged.connect(lambda: self.lineChanged(self.lines[52]))
        self.lines[53].textChanged.connect(lambda: self.lineChanged(self.lines[53]))
        self.lines[54].textChanged.connect(lambda: self.lineChanged(self.lines[54]))
        self.lines[55].textChanged.connect(lambda: self.lineChanged(self.lines[55]))
        self.lines[56].textChanged.connect(lambda: self.lineChanged(self.lines[56]))
        self.lines[57].textChanged.connect(lambda: self.lineChanged(self.lines[57]))
        self.lines[58].textChanged.connect(lambda: self.lineChanged(self.lines[58]))
        self.lines[59].textChanged.connect(lambda: self.lineChanged(self.lines[59]))
        self.lines[60].textChanged.connect(lambda: self.lineChanged(self.lines[60]))
        self.lines[61].textChanged.connect(lambda: self.lineChanged(self.lines[61]))
        self.lines[62].textChanged.connect(lambda: self.lineChanged(self.lines[62]))
        self.lines[63].textChanged.connect(lambda: self.lineChanged(self.lines[63]))
        self.lines[64].textChanged.connect(lambda: self.lineChanged(self.lines[64]))
        self.lines[65].textChanged.connect(lambda: self.lineChanged(self.lines[65]))
        self.lines[66].textChanged.connect(lambda: self.lineChanged(self.lines[66]))
        self.lines[67].textChanged.connect(lambda: self.lineChanged(self.lines[67]))
        self.lines[68].textChanged.connect(lambda: self.lineChanged(self.lines[68]))
        self.lines[69].textChanged.connect(lambda: self.lineChanged(self.lines[69]))
        self.lines[70].textChanged.connect(lambda: self.lineChanged(self.lines[70]))
        self.lines[71].textChanged.connect(lambda: self.lineChanged(self.lines[71]))
        self.lines[72].textChanged.connect(lambda: self.lineChanged(self.lines[72]))
        self.lines[73].textChanged.connect(lambda: self.lineChanged(self.lines[73]))
        self.lines[74].textChanged.connect(lambda: self.lineChanged(self.lines[74]))
        self.lines[75].textChanged.connect(lambda: self.lineChanged(self.lines[75]))
        self.lines[76].textChanged.connect(lambda: self.lineChanged(self.lines[76]))
        self.lines[77].textChanged.connect(lambda: self.lineChanged(self.lines[77]))
        self.lines[78].textChanged.connect(lambda: self.lineChanged(self.lines[78]))
        self.lines[79].textChanged.connect(lambda: self.lineChanged(self.lines[79]))
        self.lines[80].textChanged.connect(lambda: self.lineChanged(self.lines[80]))

        self.ui.btntest.clicked.connect(self.checkForWin)
        self.ui.btnsubmit.clicked.connect(self.warningMsg)

    def restart(self):
        for line, btn in zip(self.lines, self.pencil):
            line.setText("")
            btn.setText("🖊")
            line.setStyleSheet("color: rgb(0, 0, 0);\n background-color: rgb(255, 255, 255);")
        self.corrects = []
        self.rightSudoko = sudoko1
        self.currentSudoko = zerog


    def start(self):
        self.currentSudoko = generateZeros(self.rightSudoko)
        for i in range(len(self.lines)):
            y = i // 9
            x = i % 9
            if self.currentSudoko[y][x] != 0:
                self.lines[i].setText(str(self.currentSudoko[y][x]))
                self.corrects.append(self.lines[i])
                self.lines[i].unsetCursor()

    def warningMsg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Warning!!!")
        msg.setText("Do you really want to submit?\n"
                    "If you do so what you have done will be gone\n"
                    "and your score will be added to your credits")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Yes:
            # score will be added users database
            score = self.checkForWin()
            self.user.setScore(score)
            while True:
                sleep(3)
                break
            self.restart()
            # self.start()
            print(self.currentSudoko)

    def checkForWin(self):
        try:
            isWin = True
            score = 0
            for i in range(len(self.lines)):
                y = i // 9
                x = i % 9
                line = self.lines[i]

                num = line.text()
                if not num.isdigit():
                    isWin = False
                    continue

                if self.rightSudoko[y][x] == int(num):
                    line.setStyleSheet("color: rgb(87, 227, 137);\n background-color: rgb(255, 255, 255);")
                    score += 1
                else:
                    isWin = False
                    line.setStyleSheet("color: rgb(246, 97, 81);\n background-color: rgb(255, 255, 255);")

            return 100 if isWin else score - 30 if score > 30 else 0
        except Exception as ex:
            print(ex)

    def pencilPressed(self, btn: QtWidgets.QPushButton):
        text = self.lines[self.pencil.index(btn)].text()
        if text != "":
            btn.setText(text)


    def lineChanged(self, ledit: QtWidgets.QLineEdit):
        text = ledit.text()
        if ledit in self.corrects and text != "":
            ledit.setText(text[0])
        elif text != "" and text.isdigit() and ledit not in self.corrects:
            ledit.setText(text[-1])
        elif text != "":
            ledit.setText(text[:-1])

# def main():
#     app = QApplication([])
#     window = SudokoWindow(1)
#     window.show()
#     sys.exit(app.exec())
#
# if __name__ == "__main__":
#     main()

