from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QResource, QFile, QIODevice
from regMain import Ui_regMain


class Ui_Menu(object):
    QResource.registerResource('userRegIMG.qrc')

    def regMain(self):
        self.regmain = QtWidgets.QDialog()
        self.ui = Ui_regMain()
        self.ui.setupUi(self.regmain)
        self.regmain.show()

    def setupUi(self, Menu):

        Menu.setObjectName("Menu")
        Menu.resize(480, 800)
        self.label = QtWidgets.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(110, 40, 271, 71))
        self.label.setObjectName("label")
        self.userReg = QtWidgets.QPushButton(Menu, clicked = lambda: self.regMain())
        self.userReg.setGeometry(QtCore.QRect(70, 140, 151, 151))
        self.userReg.clicked.connect(Menu.close)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userReg.setFont(font)
        self.userReg.setAutoFillBackground(False)
        self.userReg.setStyleSheet("image: url(user-plus.svg);")
        self.userReg.setText("User Registeration")
        self.userReg.setObjectName("userReg")
        self.attendance = QtWidgets.QPushButton(Menu)
        self.attendance.setGeometry(QtCore.QRect(280, 140, 151, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.attendance.setFont(font)
        self.attendance.setStyleSheet("image: url(:/attendance/attendanceICON.png);")
        self.attendance.setText("")
        self.attendance.setObjectName("attendance")
        self.canteen = QtWidgets.QPushButton(Menu)
        self.canteen.setGeometry(QtCore.QRect(70, 330, 151, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.canteen.setFont(font)
        self.canteen.setStyleSheet("image: url(:/canteen/Group 27.png);")
        self.canteen.setText("")
        self.canteen.setObjectName("canteen")
        self.diagnostic = QtWidgets.QPushButton(Menu)
        self.diagnostic.setGeometry(QtCore.QRect(280, 330, 151, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diagnostic.setFont(font)
        self.diagnostic.setStyleSheet("image: url(:/diagnostic/Group 26.png);")
        self.diagnostic.setText("")
        self.diagnostic.setObjectName("diagnostic")
        self.misc = QtWidgets.QPushButton(Menu)
        self.misc.setGeometry(QtCore.QRect(70, 520, 151, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.misc.setFont(font)
        self.misc.setObjectName("misc")
        self.label.raise_()
        self.attendance.raise_()
        self.canteen.raise_()
        self.diagnostic.raise_()
        self.misc.raise_()
        self.userReg.raise_()

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)


    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.label.setText(_translate("Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Menu</span></p></body></html>"))
        self.misc.setText(_translate("Menu", "Misc"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
