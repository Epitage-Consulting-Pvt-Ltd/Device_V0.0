from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from AddUser_Working import AddUserWindow
from EditUser import DeleteUserWindow
#<<<<<<< HEAD
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE, WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR
#=======
from ViewUser_Working import ViewUserWindow
from theme import BUTTON_STYLE
from topband import topband

#>>>>>>> 11378a4aab6e23c4f7c4b5dcb9a4f71da46b4997

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
#<<<<<<< HEAD
        self.back_btn.move(50, 50)
#	self.back_btn.setStyleSheet(BUTTON_STYLE)
#=======
        self.back_btn.move(50, 150)
        self.back_btn.clicked.connect(self.show_menu_grid_window)
#>>>>>>> 11378a4aab6e23c4f7c4b5dcb9a4f71da46b4997
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)


        # Add 'Add Users' button
        self.add_btn = QPushButton('Add Users', self)
        self.add_btn.move(130, 200)
        self.add_btn.resize(200, 50)
        self.add_btn.clicked.connect(self.show_add_user_window)
        self.add_btn.clicked.connect(self.close)
        self.add_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'View Users' button
        self.view_btn = QPushButton('View Users', self)
        self.view_btn.move(130, 300)
        self.view_btn.resize(200, 50)
        self.view_btn.clicked.connect(self.show_view_user_window)
        self.view_btn.clicked.connect(self.close)
        self.view_btn.setStyleSheet(BUTTON_STYLE)

        # Add 'Delete Users' button
        self.delete_btn = QPushButton('Edit Users', self)
        self.delete_btn.move(130, 400)
        self.delete_btn.resize(200, 50)
        self.delete_btn.clicked.connect(self.show_delete_user_window)
        self.delete_btn.clicked.connect(self.close)
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

    def show_menu_grid_window(self):
        from MenuGrid import MenuWindow
        self.menu_grid_window = MenuWindow()
        self.menu_grid_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = UserMainWindow()
    app.exec_()
