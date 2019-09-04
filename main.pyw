import StringParser as sp
import CircuitSolver as cs 
import sympy as sy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

# load ui file
baseUIClass, baseUIWidget = uic.loadUiType("UserInterface.ui")

# use loaded ui file in the logic class
class Logic(baseUIWidget, baseUIClass):
    def __init__(self, parent=None):
        super(Logic, self).__init__(parent)
        self.setupUi(self)
        self.circuitSolver = cs.circuitSolver()
        self.stringParser = sp.stringParser()

        self.setConfigurationsButton.clicked.connect(self.setConfigurations)
        self.clearAllButton.clicked.connect(self.clearAll)
        self.goButton.clicked.connect(self.resolve)
        self.eqCreatorsList = [self.eqCreator_1,self.eqCreator_2,self.eqCreator_3,self.eqCreator_4,self.eqCreator_5,self.eqCreator_6]
        self.addButton.clicked.connect(self.addEquation)
        self.clearAll()


    def setConfigurations(self):
        self.stringParser.eraseEq()
        self.stringParser.eraseUnk()
        self.stringParser.eraseVariables()

        temp = self.imaginaryVariablesLineEdit.text()
        if temp != '':
            self.stringParser.setImaginaryVariables(temp)
        else:
            self.lblStatus.setText("ERROR")
        temp = self.realVariablesLineEdit.text()
        if temp != '':
            self.stringParser.setRealVariables(temp,False)
        else:
            self.lblStatus.setText("ERROR")

        temp = self.realPosVariablesLineEdit.text()
        if temp != '':
            self.stringParser.setRealVariables(temp,True)
        else:
            self.lblStatus.setText("ERROR")
        
        self.numVarLabel.setText(str(len(self.stringParser.getVarList())))
        
        for i in range(0,len(self.eqCreatorsList)):
            temp = self.eqCreatorsList[i].text()
            if(temp != ""):
                self.stringParser.decode(temp)
            self.numEqLabel.setText(str(len(self.stringParser.getExpressionList())))
        if len(self.stringParser.getExpressionList()) == 0:
            self.lblStatus.setText("ERROR")
            self.numEqLabel.setText('0')
        
        temp = self.unkCreator.text()
        if temp != '':
            self.stringParser.setUnknowns(temp)
        else:
            self.lblStatus.setText("ERROR")

        if len(self.stringParser.getVarList()) != 0 and len(self.stringParser.getUnknowns()) != 0 and len(self.stringParser.getExpressionList()) != 0:
            self.lblStatus.setText("OK")
        return
    
    def clearAll(self):
        self.stringParser.reset()
        self.circuitSolver.reset()
        self.lblStatus.setText("ERROR")
        self.numEqLabel.setText('0')
        self.numVarLabel.setText('0')
        _translate = QtCore.QCoreApplication.translate
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
        self.phaseResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Module or Phase Result</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return

    def resolve(self):
        if self.lblStatus.text() == "OK":
            self.circuitSolver.reset()
            self.circuitSolver.setEquations(self.stringParser.getExpressionList())
            self.circuitSolver.setUnknowns(self.stringParser.getUnknowns())
            self.circuitSolver.solveCircuit()
            laTex = True
            if self.prettyViewButton.isChecked():
                laTex = False
            mod = False
            if self.modChkBox.isChecked():
                mod = True
            
            if self.transferenceChkBox.isChecked():
                self.showTransferFunction(laTex,mod)
            if self.phaseCheckBox.isChecked():
                self.showPhaseFunction(laTex)
            if self.zInpChkBox.isChecked():
                self.showZInputFunction(laTex)
            if self.zOutChkBox.isChecked():
                self.showZOutputFunction(laTex)
            
        return

    def showTransferFunction(self, isLatex, isMod):
        if isMod == False:
            temp = self.circuitSolver.getH()
        else:
            temp = self.circuitSolver.getMod()
        if isLatex:
            temp = sy.latex(temp)
        else:
            temp = sy.pretty(temp)
            temp = temp.replace('\n','<br/>')
        _translate = QtCore.QCoreApplication.translate
        self.transferenceResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+ temp +"</p></body></html>"))
        return

    def showZInputFunction(self, isLatex):
        temp = self.circuitSolver.getZinp()
        if isLatex:
            temp = sy.latex(temp)
        else:
            temp = sy.pretty(temp)
            temp = temp.replace('\n','<br/>')
        _translate = QtCore.QCoreApplication.translate
        self.zInpResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+temp+"</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return

    def showZOutputFunction(self, isLatex):
        temp = self.circuitSolver.getZout()
        if isLatex:
            temp = sy.latex(temp)
        else:
            temp = sy.pretty(temp)
            temp = temp.replace('\n','<br/>')
        _translate = QtCore.QCoreApplication.translate
        self.zOutResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+temp+"</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return

    def showPhaseFunction(self,isLatex):
        temp = self.circuitSolver.getPhase()
        if isLatex:
            temp = sy.latex(temp)
        else:
            temp = sy.pretty(temp)
            temp = temp.replace('\n','<br/>')
        _translate = QtCore.QCoreApplication.translate
        self.phaseResultTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+temp+"</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return

    def addEquation(self):
        temp = self.extraEquationsLineEdit.text()
        if temp != '':
            self.stringParser.decode(temp)
            self.numEqLabel.setText(str(len(self.stringParser.getExpressionList())))
        self.extraEquationsLineEdit.setText('')
        return


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Logic(None)
    ui.show()
    sys.exit(app.exec_())
        
    
main()