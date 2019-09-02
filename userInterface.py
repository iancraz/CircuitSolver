# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import StringParser as sp
import CircuitSolver as cs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 389)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel_eq = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_eq.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainLabel_eq.setFont(font)
        self.mainLabel_eq.setObjectName("mainLabel_eq")
        self.lblStatus_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus_1.setGeometry(QtCore.QRect(50, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus_1.setFont(font)
        self.lblStatus_1.setObjectName("lblStatus_1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 40, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.eqCreator_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_1.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.eqCreator_1.setObjectName("eqCreator_1")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(100, 260, 51, 21))
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
        self.mainLabel_unk = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_unk.setGeometry(QtCore.QRect(240, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainLabel_unk.setFont(font)
        self.mainLabel_unk.setObjectName("mainLabel_unk")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 40, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.unkCreator = QtWidgets.QLineEdit(self.centralwidget)
        self.unkCreator.setGeometry(QtCore.QRect(250, 60, 113, 20))
        self.unkCreator.setObjectName("unkCreator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(400, 20, 16, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.transferenceChkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.transferenceChkBox.setGeometry(QtCore.QRect(250, 180, 111, 17))
        self.transferenceChkBox.setObjectName("transferenceChkBox")
        self.zInpChkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.zInpChkBox.setGeometry(QtCore.QRect(250, 210, 70, 17))
        self.zInpChkBox.setObjectName("zInpChkBox")
        self.zOutChkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.zOutChkBox.setGeometry(QtCore.QRect(250, 240, 70, 17))
        self.zOutChkBox.setObjectName("zOutChkBox")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(50, 290, 75, 23))
        self.goButton.setObjectName("goButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.prettyViewButton = QtWidgets.QRadioButton(self.centralwidget)
        self.prettyViewButton.setGeometry(QtCore.QRect(250, 300, 82, 17))
        self.prettyViewButton.setObjectName("prettyViewButton")
        self.latexButton = QtWidgets.QRadioButton(self.centralwidget)
        self.latexButton.setGeometry(QtCore.QRect(250, 320, 82, 17))
        self.latexButton.setObjectName("latexButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.transferenceResultTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.transferenceResultTextEdit.setGeometry(QtCore.QRect(430, 80, 401, 51))
        self.transferenceResultTextEdit.setObjectName("transferenceResultTextEdit")
        self.zInpResultTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.zInpResultTextEdit.setGeometry(QtCore.QRect(430, 170, 401, 51))
        self.zInpResultTextEdit.setObjectName("zInpResultTextEdit")
        self.zOutResultTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.zOutResultTextEdit.setGeometry(QtCore.QRect(430, 260, 401, 51))
        self.zOutResultTextEdit.setObjectName("zOutResultTextEdit")
        self.eqCreator_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_2.setGeometry(QtCore.QRect(30, 85, 113, 20))
        self.eqCreator_2.setObjectName("eqCreator_2")
        self.eqCreator_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_3.setGeometry(QtCore.QRect(30, 110, 113, 20))
        self.eqCreator_3.setObjectName("eqCreator_3")
        self.eqCreator_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_4.setGeometry(QtCore.QRect(30, 135, 113, 20))
        self.eqCreator_4.setObjectName("eqCreator_4")
        self.eqCreator_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_5.setGeometry(QtCore.QRect(30, 160, 113, 20))
        self.eqCreator_5.setObjectName("eqCreator_5")
        self.eqCreator_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.eqCreator_6.setGeometry(QtCore.QRect(30, 185, 113, 20))
        self.eqCreator_6.setObjectName("eqCreator_6")
        self.setEqButton = QtWidgets.QPushButton(self.centralwidget)
        self.setEqButton.setGeometry(QtCore.QRect(30, 220, 111, 23))
        self.setEqButton.setObjectName("setEqButton")
        self.clearAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearAllButton.setGeometry(QtCore.QRect(50, 320, 75, 23))
        self.clearAllButton.setObjectName("clearAllButton")
        self.setUnknownsButton = QtWidgets.QPushButton(self.centralwidget)
        self.setUnknownsButton.setGeometry(QtCore.QRect(260, 100, 91, 23))
        self.setUnknownsButton.setObjectName("setUnknownsButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.circuitSolver = cs.circuitSolver()
        self.stringParser = sp.stringParser()

        self.setEqButton.clicked.connect(self.setEquations)
        self.clearAllButton.clicked.connect(self.clearAll)
        self.setUnknownsButton.clicked.connect(self.setUnknowns)
        self.goButton.clicked.connect(self.resolve)

    def setEquations(self):
        for i in range(0,5):
            temp = self.eqCreator_1.text()
            if(temp != ""):
                self.stringParser.decode(temp)
        if len(self.stringParser.getExpressionList()) == 0:
            self.lblStatus.setText("ERROR")
        else:
            self.lblStatus.setText("OK")
        return
    
    def clearAll(self):
        self.stringParser.reset()
        self.circuitSolver.reset()
        self.lblStatus.setText("ERROR")
        return

    def setUnknowns(self):
        temp = self.unkCreator.text()
        if(temp != ""):
            self.stringParser.setUnknowns(temp)
        else:
            self.lblStatus.setText("ERROR")
        return

    def resolve(self):
        if self.lblStatus.text() == "OK":
            self.circuitSolver.reset()
            self.circuitSolver.setEquations(self.stringParser.getExpressionList())
            self.circuitSolver.setUnknowns(self.stringParser.getUnknowns())
            self.circuitSolver.solveCircuit()
        return








    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Circuit Solver 1.0"))
        self.mainLabel_eq.setText(_translate("MainWindow", "Please, set the equations"))
        self.lblStatus_1.setText(_translate("MainWindow", "Status "))
        self.lblStatus.setText(_translate("MainWindow", "OK"))
        self.mainLabel_unk.setText(_translate("MainWindow", "Please, set the unknowns"))
        self.label.setText(_translate("MainWindow", "Calculate:"))
        self.transferenceChkBox.setText(_translate("MainWindow", "Transference H(s)"))
        self.zInpChkBox.setText(_translate("MainWindow", "Z input"))
        self.zOutChkBox.setText(_translate("MainWindow", "Z output"))
        self.goButton.setText(_translate("MainWindow", "Go!"))
        self.label_2.setText(_translate("MainWindow", "Set Parameters"))
        self.prettyViewButton.setText(_translate("MainWindow", "Pretty View"))
        self.latexButton.setText(_translate("MainWindow", "Latex"))
        self.label_3.setText(_translate("MainWindow", "Results"))
        self.label_5.setText(_translate("MainWindow", "Transference H(s):"))
        self.label_7.setText(_translate("MainWindow", "Z input:"))
        self.label_9.setText(_translate("MainWindow", "Z output:"))
        self.transferenceResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Transference Result</p></body></html>"))
        self.zInpResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z input Result</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.zOutResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z output Result</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.setEqButton.setText(_translate("MainWindow", "Set Equations"))
        self.clearAllButton.setText(_translate("MainWindow", "Clear All"))
        self.setUnknownsButton.setText(_translate("MainWindow", "Set Unknowns"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
