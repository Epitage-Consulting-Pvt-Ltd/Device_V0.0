from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class TopBandLayout(QWidget):
    def __init__(self, windowtitle, parent=None):
        super(TopBandLayout, self).__init__(parent)

        layout = QGridLayout(self)

        label1 = QLabel(self)
        pixmap1 = QPixmap('img/epitage.jpg').scaled(150, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label1.setPixmap(pixmap1)
        label1.setAlignment(Qt.AlignLeft)  # Align label1 to the center
        label1.setFixedSize(pixmap1.width(), pixmap1.height())  # Set fixed size for label1
        layout.addWidget(label1, 0, 0 ,alignment=Qt.AlignLeft)


        label3 = QLabel(self)
        label3.setText(windowtitle)
        label3.setStyleSheet("color: #ffffff;background-color: #e68326;")
        label3.setAlignment(Qt.AlignCenter)
        layout.addWidget(label3, 0, 1, alignment= Qt.AlignCenter)


        label2 = QLabel(self)
        pixmap2 = QPixmap('img/gsk.jpg').scaled(150, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        label2.setPixmap(pixmap2)
        label2.setAlignment(Qt.AlignLeft)  # Align label2 to the center
        label2.setFixedSize(pixmap2.width(), pixmap2.height())  # Set fixed size for label2
        layout.addWidget(label2, 0, 2, alignment=Qt.AlignRight)

        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)


        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
