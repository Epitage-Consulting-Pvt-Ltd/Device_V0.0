import sys
import platform
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from splashS import Ui_splashScreen
from menu import Ui_Menu

counter = 0

class MainMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        self.show()

    def progress(self):

        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()

            self.main = MainMenu()
            self.main.show()

            self.close()

        counter += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
