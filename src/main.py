# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from type1_choice import *
from type2_hide import *
from problem_generate import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # Main Winodw
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # LAYOUTS
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 190, 661, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 500, 661, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Buttons
        self.Choice_Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Hide_Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.XXXX_Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)

        self.Choice_Btn.setObjectName("Choice_Btn")
        self.Hide_Btn.setObjectName("Hide_Btn")
        self.XXXX_Btn.setObjectName("XXXX_Btn")

        self.verticalLayout.addWidget(self.Choice_Btn)
        self.verticalLayout.addWidget(self.Hide_Btn)
        self.verticalLayout.addWidget(self.XXXX_Btn)

        # Labels
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(210, 40, 391, 131))

        self.InputLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.InputLabel.setObjectName("InputLabel")
        self.horizontalLayout.addWidget(self.InputLabel)

        self.TxtInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.TxtInput.setObjectName("TxtInput")
        self.horizontalLayout.addWidget(self.TxtInput)

        self.InputButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.InputButton.setObjectName("InputButton")
        self.horizontalLayout.addWidget(self.InputButton)
        self.InputButton.setText("Enter")

        #Buttons
        Buttonfont = QtGui.QFont()
        Buttonfont.setFamily("Adobe Arabic")
        Buttonfont.setPointSize(30)
        self.Choice_Btn.setFont(Buttonfont)
        self.Hide_Btn.setFont(Buttonfont)
        self.XXXX_Btn.setFont(Buttonfont)

        #Label
        LabelFont = QtGui.QFont()
        LabelFont.setFamily("Adobe Arabic")
        LabelFont.setPointSize(70)
        self.MainLabel.setFont(LabelFont)
        self.MainLabel.setObjectName("self.MainLabel")

        # Connect Buttons
        self.Choice_Btn.clicked.connect(self.Hanja_clicked)
        self.Hide_Btn.clicked.connect(self.Multi_clicked)
        self.InputButton.clicked.connect(self.input_button_clicked)


        # Loader
        self.loader = ProblemGenerator()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def Hanja_clicked(self):
        self.ui = ChoiceDialog()
        self.ChoiceDialog = QtWidgets.QDialog()
        self.ui.setupUi(self.ChoiceDialog, self.loader)
        self.ChoiceDialog.show()


    def Multi_clicked(self):
        self.HideDialog = QtWidgets.QDialog()
        self.ui2 = HideDialog()
        self.ui2.setupUi(self.HideDialog, self.loader)
        self.HideDialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Choice_Btn.setText(_translate("MainWindow", "Choose"))
        self.Hide_Btn.setText(_translate("MainWindow", "Hide"))
        self.XXXX_Btn.setText(_translate("MainWindow", "-NO PLAN-"))
        self.MainLabel.setText(_translate("MainWindow", "Study Helper"))
        self.InputLabel.setText(_translate("MainWindow", " INPUT"))
        self.TxtInput.setText(_translate("MainWindow", "test"))



    def input_button_clicked(self):
        self.loader._file = self.TxtInput.text()+'.txt'
        self.loader.readfile()
        print(self.loader._file)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

