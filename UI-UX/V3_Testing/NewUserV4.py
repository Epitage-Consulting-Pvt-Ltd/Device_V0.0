from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
from components import create_button, create_labeled_textbox, btn_size_normal
from topband_V3 import TopBandLayout
from src.foldertest import printcontents
from themeV3 import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE, WINDOW_BACKGROUND_COLOR, \
    WINDOW_FOREGROUND_COLOR, TRANSPARENT_BUTTON, EpitageLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QToolButton ,QProgressBar
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

        # Function to get the employee info based on the selected employee ID
        def get_employee_info(employee_id):
            with open('EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == employee_id:
                        return row[1], row[2]  # Return EmployeeName and Date of Birth

        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store EmployeeName and Date of Birth mapping
        with open('EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                column_list.append(row[0])  # Append EmpID to column_list
                dob_dict[row[0]] = row[2]  # Store empID and Date of Birth mapping

        name_id = QLabel('ID:', self)
        name_id.move(10, 300)

        # Placeholder image path
        placeholder_image_path = 'img/userMainFace.jpg'

        # QLabel to display employee picture
        picture_label = QLabel(self)
        picture_label.setGeometry(170, 100, 150, 150)
        #picture_label.setStylesheet()
        picture_label.setPixmap(QPixmap(placeholder_image_path))
        picture_label.setScaledContents(True)

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
                    employee_name, dob = employee_info
                    text_id.setText(str(employee_name))  # Display EmployeeName
                    text_dob.setText(dob)
                    # Update employee picture based on the selected ID
                    image_path = f'img/{selected_employee_id}.jpg'  # Replace with your image path
                    picture_label.setPixmap(QPixmap(image_path))
                    return
            text_id.clear()
            text_dob.clear()
            picture_label.setPixmap(QPixmap(placeholder_image_path))  # Show placeholder image if no ID selected

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

        label_face = QLabel('Face:', self)
        label_face.move(10, 510)

        text_face = QLineEdit(self)
        text_face.setReadOnly(False)
        text_face.move(150, 510)
        text_face.resize(280, 35)

        label_card = QLabel('Card:', self)
        label_card.move(10, 580)

        text_card = QLineEdit(self)
        text_card.setReadOnly(False)
        text_card.move(150, 580)
        text_card.resize(280, 35)

        label_thumb = QLabel('Thumb:', self)
        label_thumb.move(10, 650)

        text_thumb = QLineEdit(self)
        text_thumb.setReadOnly(False)
        text_thumb.move(150, 650)
        text_thumb.resize(280, 35)

        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(10, 720, 460, 20)
        progress_bar.setValue(0)

        save_label = QLabel('', self)
        save_label.move(10, 750)

        def update_progress_bar():
            progress_bar.setValue(progress_bar.value() + 33)
            if progress_bar.value() == 99:
                save_label.setText('User Successfully Saved')

        combo.currentTextChanged.connect(update_progress_bar)
        text_id.textChanged.connect(update_progress_bar)
        text_dob.textChanged.connect(update_progress_bar)
        text_face.textChanged.connect(update_progress_bar)
        text_card.textChanged.connect(update_progress_bar)
        text_thumb.textChanged.connect(update_progress_bar)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = NewWindow("User Management")
    app.exec_()
