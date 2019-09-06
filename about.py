# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(177, 267)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 111, 101))
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 81, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/itba.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        About.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(About)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 177, 21))
        self.menubar.setObjectName("menubar")
        About.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Circuit Solver"))
        self.label.setText(_translate("About", "About"))
        self.label_2.setText(_translate("About", "Creado y diseñado por Ian Diaz el segundo cuatrimestre de 2019 en la materia Teoría de Circuitos en el Instituto Tecnológico de Buenos Aires"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
