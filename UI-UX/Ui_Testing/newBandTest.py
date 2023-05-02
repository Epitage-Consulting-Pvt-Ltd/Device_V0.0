import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 480, 800)

        label1 = QLabel(self)
        pixmap1 = QPixmap('epitage_logo.jpg')
        label1.setPixmap(pixmap1.scaled(100,150))
        label1.move(50, 50)

        label2 = QLabel(self)
        pixmap2 = QPixmap('tata-motors.jpeg')
        label2.setPixmap(pixmap2.scaled(100,150))
        label2.move(300, 50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
