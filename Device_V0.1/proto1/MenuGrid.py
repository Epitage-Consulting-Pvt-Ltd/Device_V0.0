from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

import sys
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , Transparent_BUTTON_STYLE
from PyQt5.QtSvg import QSvgWidget

#Layout New
#from UserMain_Final import UserMainWindow
#Layout Old
from AddUser_Working import AddUserWindow

from topband import topband
from cardverification import CardVerificationApp
class MenuWindow(QWidget):
    def __init__(self):

        super().__init__()

        # set window title and size
        self.setWindowTitle("Device Menu")
        self.resize(480, 800)
        topband(self)

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

        def add_button(image_path, text, row, col):
            # create a QVBoxLayout to stack the QSvgWidget and QLabel
            layout = QVBoxLayout()

            # create a QSvgWidget object from the image path
            svg_widget = QSvgWidget(image_path)
            svg_widget.setFixedSize(100, 100)

            # set the background color of the QSvgWidget to transparent
            svg_widget.setStyleSheet(Transparent_BUTTON_STYLE)

            # create a QPixmap from the QSvgWidget with a white background
            pixmap = QPixmap(svg_widget.size())
            pixmap.fill(Qt.white)
            painter = QPainter(pixmap)
            svg_widget.render(painter)
            painter.end()

            # create a QIcon object from the pixmap
            icon = QIcon(pixmap)

            # create a button and set its icon and size
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setFixedSize(169, 169)

            # set the button's style sheet to have a transparent background
            button.setStyleSheet(Transparent_BUTTON_STYLE)

            # create a QLabel for the text
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)

            # add the QSvgWidget and QLabel to the layout
            layout.addWidget(svg_widget)
            layout.addWidget(label)

            # create a QWidget to hold the layout
            widget = QWidget()
            widget.setLayout(layout)

            # create a QIcon object from the QWidget
            icon = QIcon(widget.grab())

            # create a button and set its icon and size
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setFixedSize(169, 169)

            # set the button's style sheet to have a transparent background
            button.setStyleSheet(Transparent_BUTTON_STYLE)

            # add the button to the layout
            layout_g.addWidget(button, row, col)

            return button

        # add buttons to the layout using the reusable function
        user_reg = add_button("svgfiles/user.svg", "User Registeration", 0, 0)
        user_reg.clicked.connect(self.show_user_main_windowB)
        user_reg.clicked.connect(self.close)
        user_reg.setStyleSheet(Transparent_BUTTON_STYLE)

        card_verify = add_button("svgfiles/cardverify.svg","Card Verification", 0, 1)
        card_verify.clicked.connect(self.show_verify_card_window)
        card_verify.clicked.connect(self.close)
        card_verify.setStyleSheet(Transparent_BUTTON_STYLE)


    def show_user_main_windowA(self):
        self.user_main_windowA = UserMainWindow()
        self.user_main_windowA.show()
        
    def show_user_main_windowB(self):
        self.user_main_windowB = AddUserWindow()
        self.user_main_windowB.show()


    def show_splashS(self):
        from splashscreen import MainWindow
        self.splashS = MainWindow()
        self.splashS.show()

    def show_verify_card_window(self):

        self.show_verify_card_window = CardVerificationApp()
        self.show_verify_card_window.show()


if __name__ == '__main__':
    # create the application and main window
    app = QApplication(sys.argv)
    window = MenuWindow()
    # show the window and run the event loop
    window.show()
    sys.exit(app.exec_())
