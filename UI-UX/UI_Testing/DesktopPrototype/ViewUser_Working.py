import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from theme import BUTTON_STYLE
from topband_V2 import topband


class ViewUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        windowtitle = "View Users"
        self.setWindowTitle(windowtitle)
        self.resize(480, 800)
        topband(self , windowtitle)

        #self.showMaximized()
        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(50, 50)
        self.back_btn.clicked.connect(self.show_user_main_window)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)

        # Add table to display user data
        self.table = QTableWidget(self)
        self.table.setGeometry(50, 100, 400, 500)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['First Name', 'Last Name', 'Employee ID', 'RFID_ID'])

        # Populate the table with data from the CSV file
        with open("users.csv") as file:
            reader = csv.reader(file)
            data = list(reader)
            row_count = len(data)
            self.table.setRowCount(row_count)
            for i in range(row_count):
                for j in range(4):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

        self.show()

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()




if __name__ == '__main__':
    app = QApplication([])
    window = ViewUserWindow()
    app.exec_()
