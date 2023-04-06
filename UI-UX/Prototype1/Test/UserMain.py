import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from AddUser import AddUserWindow
#from ViewUsers import ViewUsersWindow
#from EditUsers import EditUsersWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a stack widget to hold the different windows
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # create buttons for each window
        self.btn_add_user = QPushButton("Add User", self)
        self.btn_add_user.clicked.connect(self.show_add_user_window)

        self.btn_view_users = QPushButton("View Users", self)
        self.btn_view_users.clicked.connect(self.show_view_users_window)

        self.btn_edit_users = QPushButton("Edit Users", self)
        self.btn_edit_users.clicked.connect(self.show_edit_users_window)

        # add the buttons to the main window
        self.toolbar = self.addToolBar("Main Toolbar")
        self.toolbar.addWidget(self.btn_add_user)
        self.toolbar.addWidget(self.btn_view_users)
        self.toolbar.addWidget(self.btn_edit_users)

        # create the different windows
        self.add_user_window = AddUserWindow()
        self.view_users_window = ViewUsersWindow()
        self.edit_users_window = EditUsersWindow()

        # add the windows to the stack widget
        self.stack.addWidget(self.add_user_window)
        self.stack.addWidget(self.view_users_window)
        self.stack.addWidget(self.edit_users_window)

    def show_add_user_window(self):
        self.stack.setCurrentWidget(self.add_user_window)

    def show_view_users_window(self):
        self.stack.setCurrentWidget(self.view_users_window)

    def show_edit_users_window(self):
        self.stack.setCurrentWidget(self.edit_users_window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
