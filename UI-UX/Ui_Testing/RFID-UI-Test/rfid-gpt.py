import sys
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QAction

from theme_test import WINDOW_BACKGROUND_COLOR, RFID_WINDOW_FOREGROUND_COLOR


class RFIDPromptDummy(QMainWindow):
    def __init__(self, company_pic, employee_name, employee_picture):
        super().__init__()

        # Set window size
        self.setFixedSize(200, 400)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, RFID_WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # Create QLabel for company picture
        company_pic_label = QLabel(self)
        pixmap = QPixmap(company_pic)
        company_pic_label.setPixmap(pixmap.scaledToWidth(150))

        # Create QLabel for employee picture
        employee_pic_label = QLabel(self)
        pixmap = QPixmap(employee_picture)
        employee_pic_label.setPixmap(pixmap.scaledToWidth(150))

        # Create QLabel for employee name
        employee_name_label = QLabel(employee_name, self)
        employee_name_label.setAlignment(Qt.AlignCenter)

        # Create QLabel for timestamp
        timestamp = QDateTime.currentDateTime().toString("MMM dd, yyyy hh:mm:ss AP")
        timestamp_label = QLabel(f"Timestamp: {timestamp}", self)
        timestamp_label.setWordWrap(True)

        # Create QVBoxLayout and add widgets to it
        vbox = QVBoxLayout()
        vbox.addWidget(employee_pic_label)
        vbox.addWidget(employee_name_label)
        vbox.addWidget(timestamp_label)

        # Create central widget and set layout
        central_widget = QWidget(self)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create menu bar and add menus and actions
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RFIDPromptDummy("sudarshanlogo.png", "Rajesh Peche", "Epitage.png")
    window.show()
    sys.exit(app.exec_())
