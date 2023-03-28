from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt
import sys


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set window title and size
        self.setWindowTitle("UI_Testing")
        self.setGeometry(100, 100, 480, 800)

        # create a grid layout with 3 rows and 2 columns
        layout_g = QGridLayout(self)
        self.setLayout(layout_g)

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
        user_reg.clicked.connect(MenuWindow.close) # Checking signal functionality.
        add_button("Diagnostic_test.png", 0, 1)
        add_button("icon.svg", 1, 0)
        add_button("icon.svg", 1, 1)
        add_button("icon.svg", 2, 0)
        add_button("icon.svg", 2, 1)


if __name__ == '__main__':
    # create the application and main window
    app = QApplication(sys.argv)
    MenuWindow = MenuWindow()
    # show the window and run the event loop
    MenuWindow.show()
    sys.exit(app.exec_())

