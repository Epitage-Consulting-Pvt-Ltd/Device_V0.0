from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
import sys
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR

from UserMain_Working import UserMainWindow

class MenuWindow(QWidget):
    def __init__(self):

        super().__init__()

        # set window title and size
        self.setWindowTitle("UI_Testing")
        self.resize(480, 800)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # create a grid layout with 3 rows and 2 columns
        layout_g = QGridLayout(self)
        self.setLayout(layout_g)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(20, 25)
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        self.back_btn.clicked.connect(self.show_splashS)
        self.back_btn.clicked.connect(self.close)

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
        user_reg = add_button("UserReg.png", 0, 0)
        user_reg.clicked.connect(self.show_user_main_window)
        user_reg.clicked.connect(self.close)
        user_reg.setStyleSheet(BUTTON_STYLE)

        user_mang = add_button("Diagnostic_test.png", 0, 1)



        add_button("Diagnostic_test.png", 1, 0)



        add_button("Diagnostic_test.png", 1, 1)
        add_button("Diagnostic_test.png", 2, 0)
        add_button("Diagnostic_test.png", 2, 1)

    def show_user_main_window(self):
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()

    def show_splashS(self):
        from splashscreen import MainWindow
        self.splashS = MainWindow()
        self.splashS.show()


if __name__ == '__main__':
    # create the application and main window
    app = QApplication(sys.argv)
    window = MenuWindow()
    # show the window and run the event loop
    window.show()
    sys.exit(app.exec_())

