from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addNew(object):
    def regMain(self):
        from regMain import Ui_regMain
        self.regmain = QtWidgets.QDialog()
        self.ui = Ui_regMain()
        self.ui.setupUi(self.regmain)
        self.regmain.show()

    def setupUi(self, addNew):
        addNew.setObjectName("addNew")
        addNew.resize(480, 800)
        self.lineEdit = QtWidgets.QLineEdit(addNew)
        self.lineEdit.setGeometry(QtCore.QRect(100, 430, 281, 41))
        self.lineEdit.setStyleSheet("background-color: gba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(addNew)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 510, 281, 41))
        self.lineEdit_2.setStyleSheet("background-color: gba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"padding-bottom:7px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(addNew)
        self.label.setGeometry(QtCore.QRect(100, 40, 271, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addNew)
        self.label_2.setGeometry(QtCore.QRect(170, 640, 121, 91))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addNew)
        self.label_3.setGeometry(QtCore.QRect(150, 170, 151, 121))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.back = QtWidgets.QPushButton(addNew, clicked = lambda: self.regMain())
        self.back.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("image: url(:/backButtonVector/backButtonVec.png);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.retranslateUi(addNew)
        self.back.clicked.connect(addNew.close)
        QtCore.QMetaObject.connectSlotsByName(addNew)

    def retranslateUi(self, addNew):
        _translate = QtCore.QCoreApplication.translate
        addNew.setWindowTitle(_translate("addNew", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("addNew", "Enter Name"))
        self.lineEdit_2.setPlaceholderText(_translate("addNew", "Enter a Valid Employee ID"))
        self.label.setText(_translate("addNew", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">New Registration</span></p></body></html>"))
        self.label_2.setText(_translate("addNew", "Finger ID"))
        self.label_3.setText(_translate("addNew", "camera"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addNew = QtWidgets.QDialog()
    ui = Ui_addNew()
    ui.setupUi(addNew)
    addNew.show()
    sys.exit(app.exec_())
