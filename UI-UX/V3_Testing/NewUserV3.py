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

        self.back_btn = create_button('Back', self, (10, 80), btn_size_normal, self.show_menu_grid_window)
        self.back_btn.setStyleSheet(BUTTON_STYLE)

        # Function to get the employee info based on the selected employee ID
        def get_employee_info(employee_id):
            with open('EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == employee_id:
                        return row[1], row[2]  # Return empID and Date of Birth

        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store empID and Date of Birth mapping
        with open('EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                column_list.append(row[0])  # Append EmpID to column_list
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
            selected_employee_id = combo.currentText()
            if selected_employee_id:
                employee_info = get_employee_info(selected_employee_id)
                if employee_info is not None:
                    employee_id, dob = employee_info
                    text_id.setText(str(employee_id))
                    text_dob.setText(dob)
                    return
            text_id.clear()
            text_dob.clear()

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Employee Name:', self)
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

        face_id = QLabel("Card" , self)




        self.show()


    def show_menu_grid_window(self):
        print("Back button clicked")

if __name__ == '__main__':
    app = QApplication([])
    window = NewWindow("User Management")
    app.exec_()
