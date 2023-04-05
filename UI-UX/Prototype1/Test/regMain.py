from PyQt5 import QtCore, QtGui, QtWidgets
from addNew import Ui_addNew
from editList import Ui_editList
from viewList import Ui_viewList


class Ui_regMain(object):

    def menuPg(self):
        from menu import Ui_Menu
        self.menu = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def addNew(self):
        self.addnew = QtWidgets.QDialog()
        self.ui = Ui_addNew()
        self.ui.setupUi(self.addnew)
        self.addnew.show()

    def editList(self):
        self.editlist = QtWidgets.QDialog()
        self.ui = Ui_editList()
        self.ui.setupUi(self.editlist)
        self.editlist.show()

    def viewList(self):
        self.viewList = QtWidgets.QDialog()
        self.ui = Ui_viewList()
        self.ui.setupUi(self.viewList)
        self.viewList.show()

    def setupUi(self, regMain):
        regMain.setObjectName("regMain")
        regMain.resize(480, 800)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        regMain.setFont(font)
        self.addN = QtWidgets.QPushButton(regMain , clicked = lambda: self.addNew())
        self.addN.setGeometry(QtCore.QRect(100, 180, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addN.setFont(font)
        self.addN.setObjectName("addN")
        self.addN.clicked.connect(regMain.close)
        self.viewL = QtWidgets.QPushButton(regMain , clicked = lambda: self.viewList())
        self.viewL.setGeometry(QtCore.QRect(100, 380, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.viewL.setFont(font)
        self.viewL.setObjectName("viewL")
        self.viewL.clicked.connect(regMain.close)
        self.editL = QtWidgets.QPushButton(regMain , clicked = lambda: self.editList())
        self.editL.setGeometry(QtCore.QRect(100, 580, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.editL.setFont(font)
        self.editL.setObjectName("editL")
        self.editL.clicked.connect(regMain.close)
        self.back = QtWidgets.QPushButton(regMain, clicked = lambda: self.menuPg())
        self.back.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("image: url(:/backButtonVector/backButtonVec.png);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.back.clicked.connect(regMain.close)
        self.retranslateUi(regMain)
        QtCore.QMetaObject.connectSlotsByName(regMain)

    def retranslateUi(self, regMain):
        _translate = QtCore.QCoreApplication.translate
        regMain.setWindowTitle(_translate("regMain", "Dialog"))
        self.addN.setText(_translate("regMain", "Add New Members"))
        self.viewL.setText(_translate("regMain", "View List"))
        self.editL.setText(_translate("regMain", "Edit List"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regMain = QtWidgets.QDialog()
    ui = Ui_regMain()
    ui.setupUi(regMain)
    regMain.show()
    sys.exit(app.exec_())
