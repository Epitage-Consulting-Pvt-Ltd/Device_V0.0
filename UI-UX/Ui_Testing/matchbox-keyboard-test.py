import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MatchBoxLineEdit(QLineEdit):
    def focusInEvent(self, e):
        try:
            subprocess.Popen(["matchbox-keyboard"])
        except FileNotFoundError:
            pass

    def focusOutEvent(self,e):
        subprocess.Popen(["killall","matchbox-keyboard"])

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("UI_Testing")
        self.resize(480, 800)

    def initUI(self):
        self.setWindowTitle('GUI TESTS')

        widget = QWidget()
        self.setCentralWidget(widget)
        lay = QVBoxLayout(widget)

        self.userNameLabel = QLabel("What is your name?")
        self.nameInput = MatchBoxLineEdit()

        lay.addWidget(self.userNameLabel)
        lay.addWidget(self.nameInput)

        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,self.sizeHint(),
                qApp.desktop().availableGeometry()
                )
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())