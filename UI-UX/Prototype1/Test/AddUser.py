import csv
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class AddUserWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # create labels and text fields
        self.lbl_first_name = QLabel("First Name:")
        self.txt_first_name = QLineEdit()
        self.lbl_last_name = QLabel("Last Name:")
        self.txt_last_name = QLineEdit()
        self.lbl_employee_id = QLabel("Employee ID:")
        self.txt_employee_id = QLineEdit()

        # create save button
        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self.save_user)

        # create layout for labels and text fields
        layout_fields = QVBoxLayout()
        layout_fields.addWidget(self.lbl_first_name)
        layout_fields.addWidget(self.txt_first_name)
        layout_fields.addWidget(self.lbl_last_name)
        layout_fields.addWidget(self.txt_last_name)
        layout_fields.addWidget(self.lbl_employee_id)
        layout_fields.addWidget(self.txt_employee_id)

        # create layout for save button
        layout_button = QHBoxLayout()
        layout_button.addStretch()
        layout_button.addWidget(self.btn_save)
        layout_button.addStretch()

        # create layout for window
        layout = QVBoxLayout()
        layout.addLayout(layout_fields)
        layout.addLayout(layout_button)

        # set layout for the window
        self.setLayout(layout)

    def save_user(self):
        # get values from text fields
        first_name = self.txt_first_name.text()
        last_name = self.txt_last_name.text()
        employee_id = self.txt_employee_id.text()

        # clear text fields
        self.txt_first_name.setText("")
        self.txt_last_name.setText("")
        self.txt_employee_id.setText("")

        # write data to CSV file
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, employee_id])

        # show popup
        msg_box = QMessageBox()
        msg_box.setText("New user added!")
        msg_box.exec_()
