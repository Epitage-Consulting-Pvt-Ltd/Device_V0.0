from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
from components import create_button, create_labeled_textbox, btn_size_normal
from topband_V3 import TopBandLayout
from src.foldertest import printcontents
from themeV3 import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , TRANSPARENT_BUTTON ,EpitageLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
#from EditUser import DeleteUserWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QToolButton
from PyQt5.QtGui import QIcon, QPixmap

class MyWindow(TopBandLayout):
    def __init__(self, windowtitle, parent=None):
        super(MyWindow, self).__init__(windowtitle, parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Management")
        self.setGeometry(100, 100, 480, 800)
        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, FOREGROUND_COLOR)
        self.setPalette(palette)


        self.back_btn = create_button('Back', self, (10, 60), btn_size_normal, self.show_menu_grid_window)
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        self.add_btn = create_button('New Users', self, (10, 115), btn_size_normal, self.show_menu_grid_window)
        self.add_btn.setStyleSheet(BUTTON_STYLE)
        self.view_btn = create_button('Edit Users', self, (130, 115), btn_size_normal, self.show_menu_grid_window)
        self.view_btn.setStyleSheet(BUTTON_STYLE)
        self.delete_btn = create_button('Delete', self, (250, 115), btn_size_normal, self.show_menu_grid_window)
        self.delete_btn.setStyleSheet(BUTTON_STYLE)

        # Function to get the employee ID based on the selected employee name
        def get_employee_info(employee_name):
            with open('EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == employee_name:
                        return row[0], row[2]  # Return empID and Date of Birth

        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store empID and Date of Birth mapping
        with open('EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                column_list.append(row[1])
                dob_dict[row[0]] = row[2]  # Store empID and Date of Birth mapping

        name_id = QLabel('Employee Name:', self)
        name_id.move(10, 300)

        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        combo.setStyleSheet("QComboBox { height: 35px; }")
        combo.move(150, 300)
        combo.setFixedWidth(280)


        def combo_text_changed():
            selected_employee_name = combo.currentText()
            if selected_employee_name:
                employee_info = get_employee_info(selected_employee_name)
                if employee_info is not None:
                    employee_id, dob = employee_info
                    text_id.setText(str(employee_id))
                    text_dob.setText(dob)
                    return
            text_id.clear()
            text_dob.clear()

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Employee ID:', self)
        label_id.move(10, 370)


        text_id = QLineEdit(self)
        text_id.setReadOnly(False)
        text_id.move(150, 370)
        text_id.resize(280, 35)

        label_dob = QLabel('Date of Birth:', self)
        label_dob.move(10, 440)

        text_dob = QLineEdit(self)
        text_dob.setReadOnly(False)
        text_dob.move(150, 440)
        text_dob.resize(280, 35)

        # Card Button
        self.card_btn = QPushButton(self)
        pixmap = QPixmap('img/userMainCrd.jpg')
        self.card_btn.setIcon(QIcon(pixmap))
        self.card_btn.setIconSize(self.card_btn.size())
        self.card_btn.move(30, 500)
        self.card_btn.setFixedSize(120, 120)
        self.card_btn.clicked.connect(self.close)

        # Face Button
        self.face_btn = QPushButton(self)
        pixmap = QPixmap('img/userMainFace.jpg')
        self.face_btn.setIcon(QIcon(pixmap))
        self.face_btn.setIconSize(self.face_btn.size())
        self.face_btn.move(180, 500)
        self.face_btn.setFixedSize(120, 120)
        self.face_btn.clicked.connect(self.close)

        self.thumb_btn = QPushButton(self)
        pixmap = QPixmap('img/userMainThumb.jpg')
        scaled_pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
        icon = QIcon(scaled_pixmap)
        self.thumb_btn.setIcon(icon)
        self.thumb_btn.setIconSize(scaled_pixmap.size())
        self.thumb_btn.move(330, 500)
        self.thumb_btn.setFixedSize(120, 120)
        self.thumb_btn.clicked.connect(self.close)

        self.show()


    def show_menu_grid_window(self):
        print("Back button clicked")

    def printanotherfolder(self):
        printcontents("test")User
In this code instead of parsing the employee name in this code , I want to parse the EmpID and fill all the details accordingly:
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
from components import create_button, create_labeled_textbox, btn_size_normal
from topband_V3 import TopBandLayout
from src.foldertest import printcontents
from themeV3 import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , TRANSPARENT_BUTTON ,EpitageLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
#from EditUser import DeleteUserWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QToolButton
from PyQt5.QtGui import QIcon, QPixmap

class NewWindow(TopBandLayout):
    def __init__(self, windowtitle, parent=None):
        super(NewWindow, self).__init__(windowtitle, parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Management")
        self.setGeometry(100, 100, 480, 800)
        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, FOREGROUND_COLOR)
        self.setPalette(palette)


        # Function to get the employee ID based on the selected employee name
        def get_employee_info(employee_name):
            with open('EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == employee_id:
                        return row[0], row[2]  # Return empID and Date of Birt
        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store empID and Date of Birth mapping
        with open('EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                column_list.append(row[0])
                dob_dict[row[0]] = row[2]  # Store empID and Date of Birth mapping

        name_id = QLabel('ID:', self)
        name_id.move(10, 300)

        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        combo.setStyleSheet("QComboBox { height: 35px; }")
        combo.move(150, 300)
        combo.setFixedWidth(280)

        def combo_text_changed():
            selected_employee_name = combo.currentText()
            if selected_employee_name:
                employee_info = get_employee_info(selected_employee_name)
                if employee_info is not None:
                    employee_id, dob = employee_info
                    text_id.setText(str(employee_id))
                    text_dob.setText(dob)
                    return
            text_id.clear()
            text_dob.clear()

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Employee ID:', self)
        label_id.move(10, 370)


        text_id = QLineEdit(self)
        text_id.setReadOnly(False)
        text_id.move(150, 370)
        text_id.resize(280, 35)

        label_dob = QLabel('Date of Birth:', self)
        label_dob.move(10, 440)

        text_dob = QLineEdit(self)
        text_dob.setReadOnly(False)
        text_dob.move(150, 440)
        text_dob.resize(280, 35)


        self.show()

    def show_menu_grid_window(self):
        print("Back button clicked")

    def printanotherfolder(self)
        printcontents("test")

if __name__ == '__main__':
    app = QApplication([])
    window = NewWindow("User Management")
    app.exec_()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow("User Management")
    app.exec_()
