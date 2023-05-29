import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

def topband(self , windowtitle):
    label1 = QLabel(self)
    pixmap1 = QPixmap('Epitage.png')
    label1.setPixmap(pixmap1.scaled(100, 150,aspectRatioMode=True))
    label1.move(50, 20)

    label2 = QLabel(self)
    pixmap2 = QPixmap('sudarshanlogo.png')
    label2.setPixmap(pixmap2.scaled(100, 150,aspectRatioMode=True))
    label2.move(300, 20)

    label3 = QLabel(windowtitle, self)
    label3.move(240, 20)




