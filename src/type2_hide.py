# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '여러개.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Hanja_load import *
import random
import time

class HideDialog(object):
    def setupUi(self, Dialog, loader):

        buttonsize = 25
        self.loader = loader
        Dialog.setObjectName("Dialog")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(buttonsize)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(Dialog)

        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)

        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_revert = QtWidgets.QPushButton(Dialog)
        self.pushButton_revert.setObjectName("pushButton_revert")

        self.label = QtWidgets.QLabel(Dialog)

        # Geometry
        Dialog.resize(928, 630)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 150, 771, 451))
        self.pushButton.setGeometry(QtCore.QRect(830, 310, 75, 131))
        self.pushButton_2.setGeometry(QtCore.QRect(830, 160, 75, 131))
        self.pushButton_revert.setGeometry(QtCore.QRect(830, 460, 75, 131))
        self.lcdNumber.setGeometry(QtCore.QRect(730, 40, 161, 71))
        self.label.setGeometry(QtCore.QRect(580, 30, 131, 91))



        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")



        self.retranslateUi(Dialog)

        # My setting
        self.btn_grp = QtWidgets.QButtonGroup()
        self.buttonSetting()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton_revert.setFont(font)

        # 한자 프로그램
        self.make_Hanjafile()
        self.do_problems()

        # Variable
        self.reverted_word = ""
        self.see_on = False
        self.next = False

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_8.setText(_translate("Dialog", "PushButton"))
        self.pushButton_5.setText(_translate("Dialog", "PushButton"))
        self.pushButton_6.setText(_translate("Dialog", "PushButton"))
        self.pushButton_7.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "NEXT"))
        self.pushButton_2.setText(_translate("Dialog", "SEE"))
        self.pushButton_revert.setText(_translate("Dialog", "REVERT"))
        self.label.setText(_translate("Dialog", "LEFT"))


    def buttonSetting(self):
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton_3, 1)
        self.btn_grp.addButton(self.pushButton_5, 2)
        self.btn_grp.addButton(self.pushButton_4, 3)
        self.btn_grp.addButton(self.pushButton_6, 4)
        self.btn_grp.addButton(self.pushButton_7, 5)
        self.btn_grp.addButton(self.pushButton_8, 6)

        self.btn_grp.buttonClicked[int].connect(self.clicked_Button)
        for button in self.btn_grp.buttons():
            button.setStyleSheet("background-color: white")
            button.setStyleSheet("QPushButton { text-align: left; }")

        self.pushButton.setStyleSheet("background-color: yellow")
        self.pushButton_2.setStyleSheet("background-color: green")
        self.pushButton_revert.setStyleSheet("background-color: orange")
        self.pushButton.clicked.connect(self.next_button_action)
        self.pushButton_2.clicked.connect(self.see_button_action)
        self.pushButton_revert.clicked.connect(self.revert_button_action)

    def make_Hanjafile(self):
        self.loader.readfile()
        self.problems = self.loader.text_to_list().copy()
        self.lcdNumber.display(len(self.problems))


    def do_problems(self):
        if len(self.problems)>0 :
            self.buttonText = []
            for button in self.btn_grp.buttons():
                choose = random.choice(self.problems)
                self.buttonText.append(choose.rstrip())
                button.setText(choose[0])
                if ":" in choose:
                    button.setText(choose[:choose.find(":")])
                button.setStyleSheet("background-color: white; text-align: left;")
                button.repaint()
            self.lcdNumber.display(len(self.problems))
            self.lcdNumber.repaint()




    def clicked_Button(self,id):
        for i,button in enumerate(self.btn_grp.buttons()):
            if button is self.btn_grp.button(id):
                button.setStyleSheet("background-color: skyblue; text-align: left;")
                button.setText(self.buttonText[i])
                button.repaint()
                time.sleep(1)
                self.reverted_word = self.buttonText[i]
                self.loader.remove(self.problems, button.text()[0])
                self.do_problems()


    def next_button_action(self):
        self.see_on = False
        self.do_problems()



    def see_button_action(self):
        if not self.see_on:
            for i,button in enumerate(self.btn_grp.buttons()):
                button.setText(self.buttonText[i])
                button.setStyleSheet("background-color: white; text-align: left;")
                button.repaint()
            self.see_on = True
        else:
            for i,button in enumerate(self.btn_grp.buttons()):
                button.setText(self.buttonText[i][:self.buttonText[i].find(":")])
                button.repaint()
            self.see_on = False


    def revert_button_action(self):
        if self.reverted_word not in self.problems:
            self.problems.append(self.reverted_word)
        self.lcdNumber.display(len(self.problems))
        self.pushButton_revert.repaint()