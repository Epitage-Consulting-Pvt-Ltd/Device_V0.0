import csv
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QMainWindow

class VirtualKeyboard(QtWidgets.QDialog):
    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.target = target

        self.setWindowTitle("Virtual Keyboard")
        self.setGeometry(0, 0, 300, 200)

        layout = QtWidgets.QVBoxLayout(self)

        self.text_edit = QtWidgets.QTextEdit()
        layout.addWidget(self.text_edit)

        button_wrapper_layout = QtWidgets.QVBoxLayout()  # Added wrapper layout
        layout.addLayout(button_wrapper_layout)  # Added wrapper layout to main layout

        buttons = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M", "<-"],
            ["Enter"]  # Added row with "Enter" button
        ]

        for row_buttons in buttons:
            button_layout = QtWidgets.QHBoxLayout()
            button_wrapper_layout.addLayout(button_layout)

            for button_text in row_buttons:
                button = QtWidgets.QPushButton(button_text)
                button.clicked.connect(self.button_clicked)
                button_layout.addWidget(button)

    def button_clicked(self):
        button = self.sender()
        if button:
            button_text = button.text()
            if button_text == "<-":
                cursor = self.text_edit.textCursor()
                cursor.deletePreviousChar()
            elif button_text == "Enter":  # Close the keyboard on "Enter" button press
                self.accept()
            else:
                self.text_edit.insertPlainText(button_text)
                if self.target is not None:
                    self.target.setText(self.text_edit.toPlainText())

class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Management")
        self.setGeometry(100, 100, 480, 800)
        self.initUI()

    def initUI(self):
        # Set window background and foreground colors
        palette = self.palette()
        BACKGROUND_COLOR = QtGui.QColor(0, 0, 0)  # Replace with your desired background color
        FOREGROUND_COLOR = QtGui.QColor(255, 255, 255)  # Replace with your desired foreground color
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

        self.name_id = QLabel('ID:', self)
        self.name_id.move(10, 300)

        # Placeholder image path
        placeholder_image_path = 'img/userMainFace.jpg'

        # QLabel to display employee picture
        picture_label = QLabel(self)
        picture_label.setGeometry(170, 100, 150, 150)
        picture_label.setPixmap(QPixmap(placeholder_image_path))
        picture_label.setScaledContents(True)

        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        combo.installEventFilter(self)

        combo.setStyleSheet("QComboBox { height: 35px; }")
        combo.move(150, 300)
        combo.setFixedWidth(280)

    def eventFilter(self, obj, event):
        if obj == combo and event.type() == QEvent.MouseButtonPress:
            virtual_keyboard = VirtualKeyboard(combo)
            if virtual_keyboard.exec_() == QtWidgets.QDialog.Accepted:
                pass  # Optional code to handle the keyboard being closed
        return super().eventFilter(obj, event)

        def combo_text_changed():
            selected_employee_id = combo.currentText()
            if selected_employee_id:
                employee_info = get_employee_info(selected_employee_id)
                if employee_info is not None:
                    employee_name, dob = employee_info
                    self.text_id.setText(str(employee_name))  # Display EmployeeName
                    self.text_dob.setText(dob)
                    # Update employee picture based on the selected ID
                    image_path = f'img/{selected_employee_id}.jpg'  # Replace with your image path
                    picture_label.setPixmap(QPixmap(image_path))
                    return

            self.text_id.clear()
            self.text_dob.clear()
            picture_label.setPixmap(QPixmap(placeholder_image_path))  # Show placeholder image if no ID selected

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Employee ID:', self)
        label_id.move(10, 370)

        self.text_id = QLineEdit(self)
        self.text_id.setReadOnly(False)
        self.text_id.move(150, 370)
        self.text_id.resize(280, 35)

        label_dob = QLabel('Date of Birth:', self)
        label_dob.move(10, 440)

        self.text_dob = QLineEdit(self)
        self.text_dob.setReadOnly(False)
        self.text_dob.move(150, 440)
        self.text_dob.resize(280, 35)

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


if __name__ == '__main__':
    app = QApplication([])
    window = NewWindow()
    window.show()

