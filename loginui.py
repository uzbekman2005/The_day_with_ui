# Form implementation generated from reading ui file 'loginui.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainlogin(object):
    def setupUi(self, mainlogin):
        mainlogin.setObjectName("mainlogin")
        mainlogin.resize(469, 374)
        self.centralwidget = QtWidgets.QWidget(mainlogin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 471, 361))
        self.widget.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.widget.setObjectName("widget")
        self.lloginUsername = QtWidgets.QLineEdit(self.widget)
        self.lloginUsername.setGeometry(QtCore.QRect(60, 70, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lloginUsername.setFont(font)
        self.lloginUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lloginUsername.setObjectName("lloginUsername")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.loginpassword = QtWidgets.QLineEdit(self.widget)
        self.loginpassword.setGeometry(QtCore.QRect(60, 170, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loginpassword.setFont(font)
        self.loginpassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loginpassword.setObjectName("loginpassword")
        self.btnlogin = QtWidgets.QPushButton(self.widget)
        self.btnlogin.setGeometry(QtCore.QRect(60, 260, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btnlogin.setFont(font)
        self.btnlogin.setObjectName("btnlogin")
        mainlogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainlogin)
        QtCore.QMetaObject.connectSlotsByName(mainlogin)

    def retranslateUi(self, mainlogin):
        _translate = QtCore.QCoreApplication.translate
        mainlogin.setWindowTitle(_translate("mainlogin", "MainWindow"))
        self.label_5.setText(_translate("mainlogin", "Password *"))
        self.label_4.setText(_translate("mainlogin", "Username *"))
        self.btnlogin.setText(_translate("mainlogin", "Log in"))
