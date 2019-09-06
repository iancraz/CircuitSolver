# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/itba.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(530, 20, 16, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(390, 260, 135, 61))
        self.goButton.setObjectName("goButton")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(410, 230, 81, 16))
        self.label_14.setObjectName("label_14")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 157, 315))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainLabel_eq = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainLabel_eq.setFont(font)
        self.mainLabel_eq.setObjectName("mainLabel_eq")
        self.gridLayout.addWidget(self.mainLabel_eq, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.eqCreator_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_1.setObjectName("eqCreator_1")
        self.gridLayout.addWidget(self.eqCreator_1, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.eqCreator_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_2.setObjectName("eqCreator_2")
        self.gridLayout.addWidget(self.eqCreator_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.eqCreator_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_3.setObjectName("eqCreator_3")
        self.gridLayout.addWidget(self.eqCreator_3, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)
        self.eqCreator_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_4.setObjectName("eqCreator_4")
        self.gridLayout.addWidget(self.eqCreator_4, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)
        self.eqCreator_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_5.setObjectName("eqCreator_5")
        self.gridLayout.addWidget(self.eqCreator_5, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 1, 1, 1)
        self.eqCreator_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eqCreator_6.setObjectName("eqCreator_6")
        self.gridLayout.addWidget(self.eqCreator_6, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 8, 0, 1, 1)
        self.extraEquationsLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.extraEquationsLineEdit.setObjectName("extraEquationsLineEdit")
        self.gridLayout.addWidget(self.extraEquationsLineEdit, 9, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 9, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 10, 0, 1, 1)
        self.setConfigurationsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.setConfigurationsButton.setObjectName("setConfigurationsButton")
        self.gridLayout.addWidget(self.setConfigurationsButton, 11, 0, 1, 1)
        self.clearAllButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearAllButton.setObjectName("clearAllButton")
        self.gridLayout.addWidget(self.clearAllButton, 12, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 120, 191, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.transferenceChkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.transferenceChkBox.setChecked(True)
        self.transferenceChkBox.setObjectName("transferenceChkBox")
        self.verticalLayout.addWidget(self.transferenceChkBox)
        self.modChkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.modChkBox.setChecked(True)
        self.modChkBox.setObjectName("modChkBox")
        self.verticalLayout.addWidget(self.modChkBox)
        self.phaseCheckBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.phaseCheckBox.setObjectName("phaseCheckBox")
        self.verticalLayout.addWidget(self.phaseCheckBox)
        self.zInpChkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.zInpChkBox.setObjectName("zInpChkBox")
        self.verticalLayout.addWidget(self.zInpChkBox)
        self.zOutChkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.zOutChkBox.setObjectName("zOutChkBox")
        self.verticalLayout.addWidget(self.zOutChkBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.prettyViewButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.prettyViewButton.setCheckable(True)
        self.prettyViewButton.setChecked(True)
        self.prettyViewButton.setAutoExclusive(True)
        self.prettyViewButton.setObjectName("prettyViewButton")
        self.verticalLayout.addWidget(self.prettyViewButton)
        self.latexButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.latexButton.setObjectName("latexButton")
        self.verticalLayout.addWidget(self.latexButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblStatus_1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus_1.setFont(font)
        self.lblStatus_1.setObjectName("lblStatus_1")
        self.horizontalLayout.addWidget(self.lblStatus_1)
        self.lblStatus = QtWidgets.QLabel(self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lblStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setObjectName("lblStatus")
        self.horizontalLayout.addWidget(self.lblStatus)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(390, 10, 137, 202))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)
        self.numEqLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.numEqLabel.setObjectName("numEqLabel")
        self.gridLayout_2.addWidget(self.numEqLabel, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)
        self.numVarLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.numVarLabel.setObjectName("numVarLabel")
        self.gridLayout_2.addWidget(self.numVarLabel, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.imaginaryVariablesLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.imaginaryVariablesLineEdit.setObjectName("imaginaryVariablesLineEdit")
        self.verticalLayout_2.addWidget(self.imaginaryVariablesLineEdit)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.realVariablesLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.realVariablesLineEdit.setObjectName("realVariablesLineEdit")
        self.verticalLayout_2.addWidget(self.realVariablesLineEdit)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.realPosVariablesLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.realPosVariablesLineEdit.setObjectName("realPosVariablesLineEdit")
        self.verticalLayout_2.addWidget(self.realPosVariablesLineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(550, 10, 441, 321))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.transferenceResultTextEdit = QtWidgets.QTextEdit(self.layoutWidget3)
        self.transferenceResultTextEdit.setObjectName("transferenceResultTextEdit")
        self.verticalLayout_5.addWidget(self.transferenceResultTextEdit)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.phaseResultTextEdit = QtWidgets.QTextEdit(self.layoutWidget3)
        self.phaseResultTextEdit.setObjectName("phaseResultTextEdit")
        self.verticalLayout_5.addWidget(self.phaseResultTextEdit)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.zInpResultTextEdit = QtWidgets.QTextEdit(self.layoutWidget3)
        self.zInpResultTextEdit.setObjectName("zInpResultTextEdit")
        self.verticalLayout_5.addWidget(self.zInpResultTextEdit)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.zOutResultTextEdit = QtWidgets.QTextEdit(self.layoutWidget3)
        self.zOutResultTextEdit.setObjectName("zOutResultTextEdit")
        self.verticalLayout_5.addWidget(self.zOutResultTextEdit)
        self.line_8 = QtWidgets.QFrame(self.layoutWidget3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.mainLabel_unk = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_unk.setGeometry(QtCore.QRect(190, 10, 187, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainLabel_unk.setFont(font)
        self.mainLabel_unk.setObjectName("mainLabel_unk")
        self.unkCreator = QtWidgets.QLineEdit(self.centralwidget)
        self.unkCreator.setGeometry(QtCore.QRect(290, 30, 81, 20))
        self.unkCreator.setObjectName("unkCreator")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(190, 40, 47, 13))
        self.label_22.setObjectName("label_22")
        self.voLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.voLineEdit.setGeometry(QtCore.QRect(230, 30, 31, 20))
        self.voLineEdit.setObjectName("voLineEdit")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(230, 47, 31, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.viLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.viLineEdit.setGeometry(QtCore.QRect(230, 60, 31, 20))
        self.viLineEdit.setObjectName("viLineEdit")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(270, 30, 16, 51))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(290, 60, 31, 16))
        self.label_23.setObjectName("label_23")
        self.iinpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.iinpLineEdit.setGeometry(QtCore.QRect(320, 60, 51, 20))
        self.iinpLineEdit.setObjectName("iinpLineEdit")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(290, 90, 31, 16))
        self.label_24.setObjectName("label_24")
        self.ioutLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ioutLineEdit.setGeometry(QtCore.QRect(320, 90, 51, 20))
        self.ioutLineEdit.setObjectName("ioutLineEdit")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(175, 10, 16, 321))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(375, 10, 20, 311))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(910, 0, 91, 41))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("resources/Logo.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Circuit Solver 1.0"))
        self.goButton.setText(_translate("MainWindow", "Go!"))
        self.label_14.setText(_translate("MainWindow", "Ian Diaz 2019"))
        self.mainLabel_eq.setText(_translate("MainWindow", "Please, set the equations"))
        self.label_4.setText(_translate("MainWindow", "=0"))
        self.label_6.setText(_translate("MainWindow", "=0"))
        self.label_8.setText(_translate("MainWindow", "=0"))
        self.label_10.setText(_translate("MainWindow", "=0"))
        self.label_11.setText(_translate("MainWindow", "=0"))
        self.label_12.setText(_translate("MainWindow", "=0"))
        self.label_18.setText(_translate("MainWindow", "Extra Equations:"))
        self.label_19.setText(_translate("MainWindow", "=0"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.setConfigurationsButton.setText(_translate("MainWindow", "Set Configurations"))
        self.clearAllButton.setText(_translate("MainWindow", "Clear All"))
        self.label.setText(_translate("MainWindow", "Calculate:"))
        self.transferenceChkBox.setText(_translate("MainWindow", "Transference H(s)"))
        self.modChkBox.setText(_translate("MainWindow", "In module"))
        self.phaseCheckBox.setText(_translate("MainWindow", "Phase"))
        self.zInpChkBox.setText(_translate("MainWindow", "Z input"))
        self.zOutChkBox.setText(_translate("MainWindow", "Z output"))
        self.label_2.setText(_translate("MainWindow", "Set Parameters"))
        self.prettyViewButton.setText(_translate("MainWindow", "Pretty View"))
        self.latexButton.setText(_translate("MainWindow", "Latex"))
        self.lblStatus_1.setText(_translate("MainWindow", "Status "))
        self.lblStatus.setText(_translate("MainWindow", "ERROR"))
        self.label_20.setText(_translate("MainWindow", "Number of equations"))
        self.numEqLabel.setText(_translate("MainWindow", "nro"))
        self.label_21.setText(_translate("MainWindow", "Number of Variables"))
        self.numVarLabel.setText(_translate("MainWindow", "nro"))
        self.label_15.setText(_translate("MainWindow", "Imaginary Variables:"))
        self.label_16.setText(_translate("MainWindow", "Real Variables:"))
        self.label_17.setText(_translate("MainWindow", "Real Positive variables:"))
        self.label_3.setText(_translate("MainWindow", "Results"))
        self.label_5.setText(_translate("MainWindow", "Transference H(s):"))
        self.transferenceResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Transference Result</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Phase H(s)"))
        self.phaseResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Phase Result</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Z input:"))
        self.zInpResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z input Result</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Z output:"))
        self.zOutResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z output Result</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mainLabel_unk.setText(_translate("MainWindow", "Please, set the unknowns"))
        self.label_22.setText(_translate("MainWindow", "H(S)="))
        self.label_23.setText(_translate("MainWindow", "Iinp="))
        self.label_24.setText(_translate("MainWindow", "Iout="))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())