import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def topband(self):
    label1 = QLabel(self)
    pixmap1 = QPixmap('Epitage.png')
    label1.setPixmap(pixmap1.scaled(100, 150 ,Qt.KeepAspectRatio, Qt.SmoothTransformation))
    label1.move(50, 50)
    label1.setAlignment(Qt.AlignLeft)

    label2 = QLabel(self)
    pixmap2 = QPixmap('sudarshanlogo.png')
    label2.setPixmap(pixmap2.scaled(100, 150,Qt.KeepAspectRatio, Qt.SmoothTransformation))
    label2.move(300, 50)
    label2.setAlignment(Qt.AlignRight)

    label3 = QLabel(self)
    label3.setText(windowtitle)
    label3.move(200, 50)
    label3.setAlignment(Qt.AlignCenter)
