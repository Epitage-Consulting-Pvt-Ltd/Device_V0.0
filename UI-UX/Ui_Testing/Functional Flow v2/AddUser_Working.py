import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from FingerPrintAddition import AddNewFingerPrint
from theme import BUTTON_STYLE
from theme import yellow_state

# Calling a file from a different folder
import sys
sys.path.append('Device_Firmware/GT521F52-working/')

#import fps


class AddUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add User")
        self.resize(480, 800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 10)
        self.back_btn.clicked.connect(self.show_user_main_window)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)

        # Add First Name label and text box
        self.fn_label = QLabel('First Name:', self)
        self.fn_label.move(50, 50)
        self.fn_textbox = QLineEdit(self)
        self.fn_textbox.move(150, 50)
        self.fn_textbox.resize(200, 30)

        # Add Last Name label and text box
        self.ln_label = QLabel('Last Name:', self)
        self.ln_label.move(50, 100)
        self.ln_textbox = QLineEdit(self)
        self.ln_textbox.move(150, 100)
        self.ln_textbox.resize(200, 30)

        # Add Employee ID label and text box
        self.eid_label = QLabel('Employee ID:', self)
        self.eid_label.move(50, 150)
        self.eid_textbox = QLineEdit(self)
        self.eid_textbox.move(150, 150)
        self.eid_textbox.resize(200, 30)

        # Add fingerprint label and text box
        self.efingerprint_label = QLabel('Fingerprint ID:', self)
        self.efingerprint_label.move(50, 200)
        self.efingerprint_textbox = QPushButton(self)
        self.efingerprint_textbox.move(150, 200)
        self.efingerprint_textbox.resize(200, 30)
        self.efingerprint_textbox.setText("Click here to Register")  # TODO
        self.efingerprint_textbox.clicked.connect(self.show_fingerprint_window)
        self.efingerprint_textbox.setStyleSheet(yellow_state)

        # Add 'Save' button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(200, 250)
        self.save_btn.resize(100, 30)
        self.save_btn.clicked.connect(self.save_user)
        self.save_btn.setStyleSheet(BUTTON_STYLE)

    def show_fingerprint_window(self):
        self.fingerprint = AddNewFingerPrint()
        self.fingerprint.show()

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()

    def save_user(self):
        # Get data from text boxes
        fn = self.fn_textbox.text()
        ln = self.ln_textbox.text()
        eid = self.eid_textbox.text()
        fp = self.efingerprint_textbox.text()

        # Write data to CSV file
        with open('users.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([fn, ln, eid,fp])

        # Clear text boxes
        self.fn_textbox.clear()
        self.ln_textbox.clear()
        self.eid_textbox.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = AddUserWindow()
    window.show()
    app.exec_()
