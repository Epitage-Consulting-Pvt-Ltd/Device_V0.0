from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt
import sys

class Screen2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screen 2')
        self.setGeometry(0, 0, 480, 800)
        # create a grid layout with 3 rows and 2 columns
        if self.layout() is not None:
            # delete the existing layout
            self.layout().deleteLater()

            # create a new grid layout
        layout_g = QGridLayout(self)

        # create a reusable function to add buttons to the layout
        def add_button(image_path, row, col):
            # create a QPixmap object from the image path and scale it
            pixmap = QPixmap(image_path).scaled(149, 149)

            # create a QIcon object from the scaled pixmap
            icon = QIcon(pixmap)

            # create a button and set its icon and size
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setFixedSize(169, 169)

            # add the button to the layout
            layout_g.addWidget(button, row, col)

            return button

        # add buttons to the layout using the reusable function
        user_reg = add_button("UserReg_test.png", 0, 0)
        #user_reg.clicked.connect(MainWindow.open)  # Checking signal functionality.
        add_button("Diagnostic_test.png", 0, 1)
        add_button("Diagnostic_test.png", 1, 0)
        add_button("Diagnostic_test.png", 1, 1)
        add_button("Diagnostic_test.png", 2, 0)
        add_button("Diagnostic_test.png", 2, 1)

        self.setLayout(layout_g)



    def go_to_screen1(self):
        from window1 import Screen1
        self.screen1 = Screen1()
        self.screen1.show()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    screen2 = Screen2()
    screen2.show()
    app.exec_()
