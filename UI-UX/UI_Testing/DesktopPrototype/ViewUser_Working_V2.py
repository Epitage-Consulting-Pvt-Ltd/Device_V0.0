import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from theme import BUTTON_STYLE
from topband_V2 import topband
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton ,QLineEdit
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt ,QCoreApplication
from PyQt5.QtWidgets import QLabel, QHBoxLayout ,QLayout
import sys
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , TRANSPARENT_BUTTON
from PyQt5.QtSvg import QSvgWidget
from UserMain_Working import UserMainWindow
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

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        #self.showMaximized()
        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(20, 100)
        self.back_btn.setFixedSize(90,40)
        self.back_btn.clicked.connect(self.show_user_main_window)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)

        # Add table to display user data
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 160, 440, 620)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['EmpID', 'Employee Name', 'Date of Birth'])

        # Set alternating row colors
        self.table.setAlternatingRowColors(True)

        # Populate the table with data from the CSV file
        with open("users.csv") as file:
            reader = csv.reader(file)
            data = list(reader)
            row_count = len(data)
            self.table.setRowCount(row_count)
            for i in range(row_count):
                for j in range(3):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

        header = self.table.horizontalHeader()
        header.setStyleSheet("background-color: #e68326;")
        # Apply style sheet to color alternate rows
        self.table.setStyleSheet("alternate-background-color: #c4c4c4; background-color: white;")
        self.show()

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()




if __name__ == '__main__':
    app = QApplication([])
    window = ViewUserWindow()
    app.exec_()
