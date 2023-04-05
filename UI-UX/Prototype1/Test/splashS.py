from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        splashScreen.setObjectName("splashScreen")
        splashScreen.resize(480, 800)
        font = QtGui.QFont()
        font.setPointSize(1)
        splashScreen.setFont(font)
        self.centralwidget = QtWidgets.QWidget(splashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
"background-color: rgb(149, 149, 149);\n"
"}\n"
"")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(100, 570, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(20, 33, 43);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.58, x2:0.985915, y2:0.574, stop:0 rgba(255, 55, 0, 255), stop:1 rgba(20, 33, 43, 255));\n"
"}\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(90, 400, 281, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(20, 33, 43);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(-10, 0, 471, 451))
        self.label.setStyleSheet("background-image: url(:/newPrefix/Buy Professional 3D Models.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        splashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        _translate = QtCore.QCoreApplication.translate
        splashScreen.setWindowTitle(_translate("splashScreen", "MainWindow"))
        self.label_2.setText(_translate("splashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">WELCOME</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splashScreen = QtWidgets.QMainWindow()
    ui = Ui_splashScreen()
    ui.setupUi(splashScreen)
    splashScreen.show()
    sys.exit(app.exec_())
