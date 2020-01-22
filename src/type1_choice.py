# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '한자.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Hanja_load import *
import time
import random

class ChoiceDialog(object):
    def __init__(self):
        self.total=20
        self.right=0

    def setupUi(self, Dialog, loader):

        self.loader = loader

        Dialog.setObjectName("Dialog")
        Dialog.resize(678, 582)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 270, 621, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 80, 171, 161))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(100)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(510, 232, 141, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")


        #Button
        """
        self.pushButton.clicked.connect(self.clicked_Button)
        """
        self.btn_grp = QtWidgets.QButtonGroup()
        self.buttonSetting()
        self.clicked = 0
        self.prob = [1,2,3,4,5]
        # HANJA
        self.make_Hanjafile()

        self.retranslateUi(Dialog)
        self.do_problems()
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def buttonSetting(self):
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton, 1)
        self.btn_grp.addButton(self.pushButton_2, 2)
        self.btn_grp.addButton(self.pushButton_3, 3)
        self.btn_grp.addButton(self.pushButton_4, 4)
        self.btn_grp.addButton(self.pushButton_5, 5)
        self.btn_grp.buttonClicked[int].connect(self.clicked_Button)
        for button in self.btn_grp.buttons():
            button.setStyleSheet("background-color: white")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Press Button"))
        self.pushButton_3.setText(_translate("Dialog", "ㅁ"))
        self.pushButton_4.setText(_translate("Dialog", "ㅁ"))
        self.pushButton_5.setText(_translate("Dialog", "ㅁ"))
        self.pushButton.setText(_translate("Dialog", "ㅁ"))
        self.label.setText(_translate("Dialog", "★"))



    def make_Hanjafile(self):
        self.problems = []
        self.problems = self.loader.text_to_list().copy()
        self.mychoice = " "
        self.Problem_len = len(self.problems)
        if self.problems[0].find(":")>=3:
            font = QtGui.QFont()
            font.setFamily("Adobe Arabic")
            font.setPointSize(30)
            self.label.setFont(font)
            font.setPointSize(10)
            for button in self.btn_grp.buttons():
                button.setFont(font)
                button.setStyleSheet("background-color: white; text-align: left;")
            for  i,j in enumerate(self.problems):
                self.problems[i] =j[:4]+j[9:]

    def do_problems(self):
        if self.problems :
            self.prob = random.choices(self.problems,k=5)
            self.pushButton_2.setText(self.prob[2][self.prob[2].find(":")+1:].rstrip())
            self.pushButton_3.setText(self.prob[3][self.prob[3].find(":")+1:].rstrip())
            self.pushButton_4.setText(self.prob[4][self.prob[4].find(":")+1:].rstrip())
            self.pushButton_5.setText(self.prob[0][self.prob[0].find(":")+1:].rstrip())
            self.pushButton.setText(self.prob[1][self.prob[1].find(":")+1:].rstrip())
            self.mychoice = random.choice(self.prob)
            self.label.setText(self.mychoice[:self.mychoice.find(":")].rstrip())
            self.pushButton.repaint()


    def clicked_Button(self,id):
        for button in self.btn_grp.buttons():
            if button is self.btn_grp.button(id):
                if button.text() == self.mychoice[self.mychoice.find(":")+1:].rstrip():
                    self.right +=1
                    self.loader.remove(self.problems, button.text())
            if button.text() != self.mychoice[self.mychoice.find(":")+1:].rstrip():
                button.setStyleSheet("background-color: red; text-align: left;")
            self.pushButton.repaint()
        time.sleep(2)

        self.do_problems()
        for button in self.btn_grp.buttons():
            button.setStyleSheet("background-color: white; text-align: left;")
        self.progressBar.setProperty("value", (self.right)/self.Problem_len*100)
        self.progressBar.repaint()
