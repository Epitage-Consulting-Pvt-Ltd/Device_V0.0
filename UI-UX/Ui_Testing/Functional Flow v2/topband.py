from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

def topband(self):
    label1 = QLabel(self)
    pixmap1 = QPixmap('gsk.jpg').scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label1.setPixmap(pixmap1)
    label1.move(18, 10)

    label2 = QLabel(self)
    pixmap2 = QPixmap('epitage.jpg').scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label2.setPixmap(pixmap2)
    label2.move(370, 10)


