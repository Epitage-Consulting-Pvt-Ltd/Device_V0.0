from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from theme import yellow_state , green_state

class AddNewFingerPrint(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle('Add New Fingerprint')
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # Create central box with text
        self.central_box = QLabel(self)
        self.central_box.setAlignment(Qt.AlignCenter)
        self.central_box.setText('Place index finger on the sensor')
        self.central_box.setWordWrap(True)
        self.central_box.setStyleSheet(yellow_state)
        self.central_box.setGeometry(20, 10, 160, 40)


        # Create label for status
        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setText('Recording fingerprint')
        self.status_label.setStyleSheet('color: gray; font-size: 12px;')
        self.status_label.setGeometry(20, 60, 160, 20)


        # Create close button
        self.close_btn = QPushButton('Close', self)
        self.close_btn.setStyleSheet(green_state)
        self.close_btn.setGeometry(75, 85, 50, 20)
        self.close_btn.clicked.connect(self.close)

        # Set timer to change color of central box
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(5000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRect(self.rect())

    def change_color(self):
        # Change color of central box to green and update status label
        self.central_box.setStyleSheet(
            'background-color: green; border: 2px solid black; border-radius: 5px; font-size: 14px;')
        self.status_label.setText('Fingerprint recorded')
        self.status_label.setStyleSheet('background-color: green; border: 2px solid black; border-radius: 5px; font-size: 14px;')
        self.timer.stop()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = AddNewFingerPrint()
    window.show()
    sys.exit(app.exec_())
