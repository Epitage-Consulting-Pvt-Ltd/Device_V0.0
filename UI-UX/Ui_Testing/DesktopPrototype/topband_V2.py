import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def topband(self ,windowtitle):
    label1 = QLabel(self)
    pixmap1 = QPixmap('Epitage.png').scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation )
    label1.setPixmap(pixmap1)
    label1.move(50, 50)
    label1.setAlignment(Qt.AlignLeft)
    #pixmap1 = QPixmap("images/ethos.png").scaled(370, 370, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    label2 = QLabel(self)
    pixmap2 = QPixmap('sudarshanlogo.png').scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
    label2.setPixmap(pixmap2)
    label2.move(350, 50)
    label2.setAlignment(Qt.AlignRight)

    label3 = QLabel(self)
    label3.setText(windowtitle)
    label3.move(200, 50)
    label3.setStyleSheet("color: #ffffff;background-color: #e68326;")
    label3.setAlignment(Qt.AlignCenter)
