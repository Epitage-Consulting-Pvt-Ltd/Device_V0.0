from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
import sys
sys.path.append('src')
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR
from PyQt5.QtSvg import QSvgWidget
from UserMain_Working import UserMainWindow
from cardverification import CardVerificationApp
class MenuWindow(QWidget):
    def __init__(self):

        super().__init__()

        # set window title and size
        self.setWindowTitle("Device Menu")
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
            # create a QSvgWidget object from the image path
            svg_widget = QSvgWidget(image_path)
            svg_widget.setFixedSize(100,100)

            # create a QIcon object from the svg_widget
            icon = QIcon(svg_widget.renderer())

            # create a button and set its icon and size
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setFixedSize(169, 169)

            # add the button to the layout
            layout_g.addWidget(button, row, col)

            return button
        # add buttons to the layout using the reusable function
        user_reg = add_button("svgfiles/adduser.svg", 0, 0)
        user_reg.clicked.connect(self.show_user_main_window)
        user_reg.clicked.connect(self.close)
        user_reg.setStyleSheet(BUTTON_STYLE)

        card_verify = add_button("svgfiles/cardverify.svg", 0, 1)
        card_verify.clicked.connect(self.show_verify_card_window)
        card_verify.clicked.connect(self.close)
        card_verify.setStyleSheet(BUTTON_STYLE)
    def show_user_main_window(self):
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()

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

