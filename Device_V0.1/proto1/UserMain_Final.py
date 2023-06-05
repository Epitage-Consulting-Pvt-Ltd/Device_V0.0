from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from EditUser import DeleteUserWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QToolButton
from PyQt5.QtGui import QIcon, QPixmap
from ViewUser_Working import ViewUserWindow
from theme import BUTTON_STYLE , EpitageLabel
from topband import topband
from keyboard import MatchBoxLineEdit
from AddUser_Working import AddUserWindow


class UserMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Create top band using a function call.
        topband(self)


        self.setWindowTitle("User Management System")
        self.resize(480, 800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 60)
        self.back_btn.setFixedSize(90, 40)
        self.back_btn.clicked.connect(self.show_menu_grid_window)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)


        # Add 'Add Users' button
        self.add_btn = QPushButton('Add Users', self)
        self.add_btn.move(10, 115)
        self.add_btn.setFixedSize(110, 40)
        self.add_btn.clicked.connect(self.show_add_user_window)
        self.add_btn.clicked.connect(self.close)
        self.add_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'View Users' button
        self.view_btn = QPushButton('View Users', self)
        self.view_btn.move(130, 115)
        self.view_btn.setFixedSize(110, 40)
        self.view_btn.clicked.connect(self.show_view_user_window)
        self.view_btn.clicked.connect(self.close)
        self.view_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'Delete Users' button
        self.delete_btn = QPushButton('Edit Users', self)
        self.delete_btn.move(250, 115)
        self.delete_btn.resize(110, 40)
        self.delete_btn.clicked.connect(self.show_delete_user_window)
        self.delete_btn.clicked.connect(self.close)
        self.delete_btn.setStyleSheet(BUTTON_STYLE)

        self.datalog_btn = QPushButton('Data Log', self)
        self.datalog_btn.move(10, 200)
        self.datalog_btn.resize(110, 40)
        self.datalog_btn.clicked.connect(self.close)
        self.datalog_btn.setStyleSheet(BUTTON_STYLE)

        self.userlog_btn = QPushButton('User Log', self)
        self.userlog_btn.move(180, 200)
        self.userlog_btn.resize(110, 40)
        self.userlog_btn.clicked.connect(self.close)
        self.userlog_btn.setStyleSheet(BUTTON_STYLE)

        self.eid_label = QLabel('ID:', self)
        self.eid_label.setStyleSheet("font-size: 20px; font-weight: light;")
        self.eid_label.move(10, 300)
        self.eid_textbox = QLineEdit()
        self.eid_textbox = MatchBoxLineEdit()
        self.eid_textbox.move(150, 300)
        self.eid_textbox.resize(280, 45)
        self.eid_textbox.setParent(self)

        self.fn_label = QLabel('First Name:', self)
        self.fn_label.setStyleSheet("font-size: 20px; font-weight: light;")
        self.fn_label.move(10, 370)
        self.fn_textbox= QLineEdit()
        self.fn_textbox = MatchBoxLineEdit()
        self.fn_textbox.move(150, 370)
        self.fn_textbox.resize(280, 45)
        self.fn_textbox.setParent(self)

        self.ln_label = QLabel('Last Name:', self)
        self.ln_label.setStyleSheet("font-size: 20px; font-weight: light;")
        self.ln_label.move(10, 440)
        self.ln_textbox = QLineEdit()
        self.ln_textbox.move(150, 440)
        self.ln_textbox.resize(280, 45)
        self.ln_textbox.setParent(self)

        self.dob_label = QLabel('DOB:', self)
        self.dob_label.setStyleSheet("font-size: 20px; font-weight: light;")
        self.dob_label.move(10, 520)
        self.dob_textbox = QLineEdit()
        self.dob_textbox = MatchBoxLineEdit()
        self.dob_textbox.move(150, 520)
        self.dob_textbox.resize(280, 45)
        self.dob_textbox.setParent(self)

        #Card Button
        self.card_btn = QPushButton(self)
        pixmap = QPixmap('images/userMainCrd.jpg')
        self.card_btn.setIcon(QIcon(pixmap))
        self.card_btn.setIconSize(self.card_btn.size())
        self.card_btn.move(30, 600)
        self.card_btn.setFixedSize(120, 120)
        self.card_btn.clicked.connect(self.close)

        #Face Button
        self.face_btn = QPushButton(self)
        pixmap = QPixmap('images/userMainFace.jpg')
        self.face_btn.setIcon(QIcon(pixmap))
        self.face_btn.setIconSize(self.face_btn.size())
        self.face_btn.move(180, 600)
        self.face_btn.setFixedSize(120, 120)
        self.face_btn.clicked.connect(self.close)

        # Thumb Button
        self.thumb_btn = QPushButton(self)
        pixmap = QPixmap('images/userMainThumb.jpg')
        icon = QIcon(pixmap)
        self.thumb_btn.setIcon(icon)
        self.thumb_btn.setIconSize(self.thumb_btn.size())  # Set the icon size to match the button size
        self.thumb_btn.move(330, 600)
        self.thumb_btn.setFixedSize(120, 120)
        self.thumb_btn.clicked.connect(self.close)
        self.show()

    def show_add_user_window(self):
        from AddUser_Working import AddUserWindow
        self.add_user_window = AddUserWindow()
        self.add_user_window.show()

    def show_view_user_window(self):
        self.view_user_window = ViewUserWindow()
        self.view_user_window.show()

    def show_delete_user_window(self):
        self.delete_user_window = DeleteUserWindow()
        self.delete_user_window.show()

    def show_menu_grid_window(self):
        from MenuGrid import MenuWindow
        self.menu_grid_window = MenuWindow()
        self.menu_grid_window.show()


if __name__ == '__main__':
    app = QApplication([])
    window = UserMainWindow()
    app.exec_()
