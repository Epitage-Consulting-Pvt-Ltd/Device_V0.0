import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from utilities.components import create_img_button
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from utilities.components import create_img_button , create_labeled_textbox , imgbutton
from utilities.themeV3 import BUTTON_STYLE


class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(3, 3, 160, 20)

        # Set font for date and time label
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)

        self.backbtnv2 = imgbutton(self, "images/icons/BackIcon.png", 30,30, (5, 44), self.close)

        self.deviceMenu = create_img_button(self,"images/icons/NewUserIcon.png", 55, 100, (18, 142), self.close, "New", "#D9D9D9")
        self.deviceMenu.setEnabled(True)

        self.UserMenu = create_img_button(self, "images/icons/EditUserIcon.png", 55, 100, (133, 142), self.close,"Edit", "#D9D9D9")
        self.UserMenu.setEnabled(True)

        self.CommMenu = create_img_button(self, "images/icons/CopyUserIcon.png", 55, 100, (248, 142), self.close,"Copy", "#D9D9D9")
        self.CommMenu.setEnabled(True)

        self.LogMenu = create_img_button(self, "images/icons/DeleteUserIcon.png", 55, 100, (363, 142), self.close,"Delete","#D9D9D9")
        self.LogMenu.setEnabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserWindow()
    window.show()
    sys.exit(app.exec_())






