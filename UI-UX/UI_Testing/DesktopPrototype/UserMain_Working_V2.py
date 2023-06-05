from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap

class UserMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Management System")
        self.resize(480, 800)

        # Create 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 60)
        self.back_btn.setFixedSize(90, 40)
        self.back_btn.clicked.connect(self.show_menu_grid_window)

        # Create 'Add Users' button
        self.add_btn = QPushButton('Add Users', self)
        self.add_btn.move(10, 115)
        self.add_btn.setFixedSize(110, 40)
        self.add_btn.clicked.connect(self.enable_label_fields)
        self.add_btn.clicked.connect(self.highlight_button)

        # Create 'View Users' button
        self.view_btn = QPushButton('View Users', self)
        self.view_btn.move(130, 115)
        self.view_btn.setFixedSize(110, 40)
        self.view_btn.clicked.connect(self.enable_label_fields)
        self.view_btn.clicked.connect(self.highlight_button)

        # Create 'Delete Users' button
        self.delete_btn = QPushButton('Edit Users', self)
        self.delete_btn.move(250, 115)
        self.delete_btn.resize(110, 40)
        self.delete_btn.clicked.connect(self.enable_label_fields)
        self.delete_btn.clicked.connect(self.highlight_button)

        # Create label fields
        self.eid_label = QLabel('ID:', self)
        self.eid_label.move(10, 300)
        self.eid_textbox = QLineEdit()
        self.eid_textbox.move(150, 300)
        self.eid_textbox.resize(280, 45)
        self.eid_textbox.setEnabled(False)
        self.eid_textbox.show()
        self.eid_textbox.setParent(self)

        self.fn_label = QLabel('First Name:', self)
        self.fn_label.move(10, 370)
        self.fn_textbox = QLineEdit()
        self.fn_textbox.move(150, 370)
        self.fn_textbox.resize(280, 45)
        self.fn_textbox.setEnabled(False)
        self.fn_textbox.show()

        self.ln_label = QLabel('Last Name:', self)
        self.ln_label.move(10, 440)
        self.ln_textbox = QLineEdit()
        self.ln_textbox.move(150, 440)
        self.ln_textbox.resize(280, 45)
        self.ln_textbox.setEnabled(False)

        self.dob_label = QLabel('DOB:', self)
        self.dob_label.move(10, 520)
        self.dob_textbox = QLineEdit()
        self.dob_textbox.move(150, 520)
        self.dob_textbox.resize(280, 45)
        self.dob_textbox.setEnabled(False)

        self.show()

    def enable_label_fields(self):
        self.eid_textbox.setEnabled(True)
        self.fn_textbox.setEnabled(True)
        self.ln_textbox.setEnabled(True)
        self.dob_textbox.setEnabled(True)

    def highlight_button(self):
        sender = self.sender()
        all_buttons = [self.add_btn, self.view_btn, self.delete_btn]
        for button in all_buttons:
            if button == sender:
                button.setStyleSheet("background-color: yellow")
            else:
                button.setStyleSheet("")

    def show_menu_grid_window(self):
        from MenuGrid import MenuWindow
        self.menu_grid_window = MenuWindow()
        self.menu_grid_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = UserMainWindow()
    app.exec_()
