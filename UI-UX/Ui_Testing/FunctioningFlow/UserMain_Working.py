from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton

from AddUser_Working import AddUserWindow
from EditUser import DeleteUserWindow
from ViewUser_Working import ViewUserWindow
from theme import BUTTON_STYLE
from topband import topband


class UserMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Create top band using a function call.

        topband(self)


        self.setWindowTitle("User Management System")
        self.setGeometry(100, 100, 480, 800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(50, 150)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)


        # Add 'Add Users' button
        self.add_btn = QPushButton('Add Users', self)
        self.add_btn.move(130, 200)
        self.add_btn.resize(200, 50)
        self.add_btn.clicked.connect(self.show_add_user_window)
        self.add_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'View Users' button
        self.view_btn = QPushButton('View Users', self)
        self.view_btn.move(130, 300)
        self.view_btn.resize(200, 50)
        self.view_btn.clicked.connect(self.show_view_user_window)
        self.view_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'Delete Users' button
        self.delete_btn = QPushButton('Edit Users', self)
        self.delete_btn.move(130, 400)
        self.delete_btn.resize(200, 50)
        self.delete_btn.clicked.connect(self.show_delete_user_window)
        self.delete_btn.setStyleSheet(BUTTON_STYLE)


        self.show()

    def show_add_user_window(self):
        self.add_user_window = AddUserWindow()
        self.add_user_window.show()

    def show_view_user_window(self):
        self.view_user_window = ViewUserWindow()
        self.view_user_window.show()

    def show_delete_user_window(self):
        self.delete_user_window = DeleteUserWindow()
        self.delete_user_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = UserMainWindow()
    app.exec_()
