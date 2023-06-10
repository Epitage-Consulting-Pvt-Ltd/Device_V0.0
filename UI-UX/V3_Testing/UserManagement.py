from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
import csv
from PyQt5 import QtWidgets , Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
from components import create_button, create_labeled_textbox, btn_size_normal
from topband_V3 import TopBandLayout
from src.foldertest import printcontents
from themeV3 import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR , TRANSPARENT_BUTTON ,EpitageLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
import csv


class MyWindow(QMainWindow):
    def __init__(self, windowtitle, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle(windowtitle)
        self.setGeometry(100, 100, 480, 800)
        self.initUI()

    def initUI(self):
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 60)

        self.add_btn = QPushButton('New Users', self)
        self.add_btn.move(10, 115)

        self.view_btn = QPushButton('Edit Users', self)
        self.view_btn.move(130, 115)

        self.delete_btn = QPushButton('Delete', self)
        self.delete_btn.move(250, 115)

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

        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        combo.move(20, 20)

        def combo_text_changed():
            selected_employee_name = combo.currentText()
            if selected_employee_name:
                employee_info = get_employee_info(selected_employee_name)
                if employee_info is not Non
                    employee_id, dob = employee_info
                    text_id.setText(str(employee_id))
                    text_dob.setText(dob)
                    return
            text_id.clear()
            text_dob.clear()

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Employee ID:', self)
        label_id.move(20, 60)

        text_id = QLineEdit(self)
        text_id.setReadOnly(True)
        text_id.move(120, 60)

        label_dob = QLabel('Date of Birth:', self)
        label_dob.move(20, 90)

        text_dob = QLineEdit(self)
        text_dob.setReadOnly(True)
        text_dob.move(120, 90)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow("User Management")
    app.exec_()
