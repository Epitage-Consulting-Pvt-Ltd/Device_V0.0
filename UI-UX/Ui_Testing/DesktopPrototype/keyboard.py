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

    def focusOutEvent(self, e):
        subprocess.Popen(["killall", "matchbox-keyboard"])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            subprocess.Popen(["killall", "matchbox-keyboard"])
        else:
            super().keyPressEvent(event)


