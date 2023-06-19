from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton ,QLineEdit
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt ,QCoreApplication
from PyQt5.QtWidgets import QLabel, QHBoxLayout ,QLayout
import sys
from themeV3 import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , TRANSPARENT_BUTTON
from PyQt5.QtSvg import QSvgWidget
#from UserMain_Working import UserMainWindow
from topband_V3 import TopBandLayout
#from cardverification import CardVerificationApp
from PyQt5.QtSvg import QSvgRenderer

class MenuWindow(QMa):
    def __init__(self, windowtitle, parent=None):
            super(MenuWindow, self).__init__(windowtitle, parent)
            self.initUI()

    def initUI(self):



        # set window title and size
        self.setWindowTitle("Menu")
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
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        self.back_btn.clicked.connect(self.show_splashS)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.move(20, 100)
        self.back_btn.setFixedSize(90,40)

        # Create the label
        label = QLabel("Enter Password", self)
        label.setStyleSheet("color: #808080")
        label.move(60, 160)

        # Create the password field
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("here")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.textChanged.connect(self.verify_password)
        self.password_field.setFixedSize(250, 30)
        self.password_field.move(200, 160)

        # create a reusable function to add buttons to the layout

        def add_button(image_path, text, row, col):
            # Create a QVBoxLayout to stack the QLabel and button
            layout = QVBoxLayout()

            # Create a QLabel for the text
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)

            # Create a QSvgRenderer object from the image path
            renderer = QSvgRenderer(image_path)

            # Create a QPixmap to hold the rendered SVG
            pixmap = QPixmap(100, 100)
            pixmap.fill(Qt.white)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()

            # Create a QIcon object from the pixmap
            icon = QIcon(pixmap)

            # Create a button and set its icon and size
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setFixedSize(169, 169)

            # Set the button's style sheet to have a transparent background
            button.setStyleSheet(TRANSPARENT_BUTTON)

            # Add the QLabel and button to the layout
            layout.addWidget(label)
            layout.addWidget(button)

            # Check if the widget already has a layout
            if isinstance(layout_g, QLayout):
                # Retrieve the existing layout from the widget
                existing_layout = layout_g
                # Create a QWidget to hold the layout
                widget = QWidget()
                widget.setLayout(existing_layout)

                # Add the new widget to the existing layout
                existing_layout.addWidget(widget)
            else:
                # Create a QWidget to hold the layout
                widget = QWidget()
                widget.setLayout(layout)

                # Add the widget to the layout_g
                layout_g.addWidget(widget, row, col)

            return button

        # add buttons to the layout using the reusable function
        self.user_reg = add_button("adduserv3.svg", "User Registeration", 1, 0)
        self.user_reg.clicked.connect(self.show_user_main_window)
        self.user_reg.clicked.connect(self.close)
        self.user_reg.setEnabled(False)
        self.user_reg.setStyleSheet(TRANSPARENT_BUTTON)

        self.card_verify = add_button("svgfiles/cardverify.svg","Card Verification", 1, 1)
        self.card_verify.clicked.connect(self.show_verify_card_window)
        self.card_verify.clicked.connect(self.close)
        self.card_verify.setEnabled(False)
        self.card_verify.setStyleSheet(TRANSPARENT_BUTTON)

        self.printerbutton = add_button("svgfiles/printer.svg","Printer Demo" ,2,0)
        #self.printerbutton.clicked.connect(self.show_printerdemo)
        self.printerbutton.clicked.connect(self.close)
        self.printerbutton.setEnabled(False)


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

    def verify_password(self):
        password = self.password_field.text()
        print("Entered Password:", password)

        # Perform password verification logic here
        # For example, check if the password matches a predefined value
        expected_password = "admin"
        is_password_matched = (password == expected_password)
        print("Password Matched:", is_password_matched)

        # Enable or disable buttons based on password verification result
        self.user_reg.setEnabled(is_password_matched)
        self.card_verify.setEnabled(is_password_matched)




if __name__ == '__main__':
    # create the application and main window
    app = QApplication(sys.argv)
    window = MenuWindow("Menu")
    # show the window and run the event loop
    window.show()
    sys.exit(app.exec_())
