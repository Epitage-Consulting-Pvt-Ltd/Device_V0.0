from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from AddUser_Working import AddUserWindow
from ViewUser_Working import ViewUserWindow

class UserMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("User Management System")
        self.setGeometry(100, 100, 480, 800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(50, 50)
        self.back_btn.clicked.connect(self.close)


        # Add 'Add Users' button
        self.add_btn = QPushButton('Add Users', self)
        self.add_btn.move(100, 100)
        self.add_btn.clicked.connect(self.show_add_user_window)

        # Add 'View Users' button
        self.view_btn = QPushButton('View Users', self)
        self.view_btn.move(100, 200)
        self.view_btn.clicked.connect(self.show_view_user_window)


        self.show()

    def show_add_user_window(self):
        self.add_user_window = AddUserWindow()
        self.add_user_window.show()

    def show_view_user_window(self):
        self.view_user_window = ViewUserWindow()
        self.view_user_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = UserMainWindow()
    app.exec_()
