from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QLayout
import sys
from theme import (
    BACKGROUND_COLOR,
    FOREGROUND_COLOR,
    ACCENT_COLOR,
    BUTTON_STYLE,
    TABLE_STYLE,
    WINDOW_BACKGROUND_COLOR,
    WINDOW_FOREGROUND_COLOR,
    TRANSPARENT_BUTTON,
)
from PyQt5.QtSvg import QSvgWidget
from UserMain_Final import UserMainWindow
from topband_V2 import topband
from mfrc522 import SimpleMFRC522

# from cardverification import CardVerificationApp
class MenuWindow(QWidget):
    def __init__(self):

        super().__init__()

        windowtitle = "Device Menu"

        # set window title and size
        self.setWindowTitle(windowtitle)
        self.resize(480, 800)
        topband(self, windowtitle)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # create a grid layout with 3 rows and 2 columns
        layout_g = QGridLayout(self)
        self.setLayout(layout_g)

        # Add 'Back' button
        self.back_btn = QPushButton("Back", self)
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        self.back_btn.clicked.connect(self.show_splashS)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.move(20, 100)
        self.back_btn.setFixedSize(90, 40)

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
            # create a QVBoxLayout to stack the QSvgWidget and QLabel
            layout = QVBoxLayout()

            # create a QSvgWidget object from the image path
            svg_widget = QSvgWidget(image_path)
            svg_widget.setFixedSize(100, 100)

            # set the background color of the QSvgWidget to transparent
            svg_widget.setStyleSheet(TRANSPARENT_BUTTON)

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
            button.setStyleSheet(TRANSPARENT_BUTTON)

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
            button.setStyleSheet(TRANSPARENT_BUTTON)

            # add the button to the layout
            layout_g.addWidget(button, row, col)

            return button

        # add buttons to the layout using the reusable function
        self.user_reg = add_button("svgfiles/user.svg", "User Registeration", 1, 0)
        self.user_reg.clicked.connect(self.show_user_main_window)
        self.user_reg.clicked.connect(self.close)
        self.user_reg.setEnabled(False)
        self.user_reg.setStyleSheet(TRANSPARENT_BUTTON)

        self.card_verify = add_button(
            "svgfiles/cardverify.svg", "Card Verification", 1, 1
        )
        self.card_verify.clicked.connect(self.show_verify_card_window)
        self.card_verify.clicked.connect(self.close)
        self.card_verify.setEnabled(False)
        self.card_verify.setStyleSheet(TRANSPARENT_BUTTON)

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

    """def verify_password(self):
        password = self.password_field.text()
        print("Entered Password:", password)

        # Perform password verification logic here
        # For example, check if the password matches a predefined value
        expected_password = "admin"
        is_password_matched = (password == expected_password)
        print("Password Matched:", is_password_matched)

        # Enable or disable buttons based on password verification result
        self.user_reg.setEnabled(is_password_matched)
        self.card_verify.setEnabled(is_password_matched)"""

    def read_user_data(self):
        user_data = {}
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                fn = int(row[0])
                ln = int(row[1])
                eid = row[2]
                user_data[card_id] = (Chetan, 1)
        return user_data

    def verify_password(self):
        reader = SimpleMFRC522()

        try:
            card_id = reader.read_id()
            print("RFID Card ID:", card_id)

            user_data = read_user_data()

            if card_id in user_data:
                user_id, username = user_data[card_id]
                print("Card Matched - User ID:", user_id)
                print("Username:", username)

                # Enable or disable buttons based on card verification result
                self.user_reg.setEnabled(True)
                self.card_verify.setEnabled(True)
            else:
                print("Card not found in user data")

        finally:
            reader.cleanup()


if __name__ == "__main__":
    # create the application and main window
    app = QApplication(sys.argv)
    window = MenuWindow()
    # show the window and run the event loop
    window.show()
    sys.exit(app.exec_())
