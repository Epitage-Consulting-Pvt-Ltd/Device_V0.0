import csv
# import
# Calling a file from a different folder
import sys

# import fps
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit

from theme import BUTTON_STYLE
from theme import yellow_state


# sys.path.append('Device_Firmware/GT521F52-working/')


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
        # Add RFID Label and text box
        # self.name_label = QLabel("Name:")
        # self.name_label =QLineEdit()
        self.rfid_label = QLabel("RFID:", self)
        self.rfid_input = QLineEdit()
        self.rfid_textbox = QPushButton(self)
        self.rfid_textbox.move(150, 200)
        self.rfid_textbox.resize(200, 30)
        self.rfid_textbox.setText("Click here to Register")
        self.rfid_textbox.clicked.connect(self.read_rfid)
        self.rfid_textbox.setStyleSheet(yellow_state)
        # Add 'Save' button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(200, 250)
        self.save_btn.resize(100, 30)
        self.save_btn.clicked.connect(self.save_user)
        self.save_btn.setStyleSheet(BUTTON_STYLE)

        # Add on screen keyboard
        self.keyboard = QTextEdit()
        self.keyboard.setReadOnly(True)
        self.keyboard.setFixedHeight(100)
        self.keyboard.setFixedWidth(200)
        self.keyboard.setStyleSheet("font-size: 20px;")
        self.keyboard.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard.setAlignment(Qt.AlignLeft | Qt.AlignTop)


def read_rfid(self):
    self.keyboard.setText("Tap your Card on the Reader")
    try:
        id, rfid = self.reader.read()
        self.rfid_input.setText(str(id))
        self.keyboard.setText("Card read successful. ")
    except:
        self.keyboard.setText(f"Error Reading card: {str(e)}")


def show_user_main_window(self):
    from UserMain_Working import UserMainWindow
    self.user_main_window = UserMainWindow()
    self.user_main_window.show()


def save_user(self):
    # Get data from text boxes
    fn = self.fn_textbox.text()
    ln = self.ln_textbox.text()
    eid = self.eid_textbox.text()
    # fp = self.efingerprint_textbox.text()
    rfid = self.rfid_input.text()

    # Write data to CSV file
    with open('users.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([fn, ln, eid, rfid])

    # Clear text boxes
    self.fn_textbox.clear()
    self.ln_textbox.clear()
    self.eid_textbox.clear()
    self.rfid_input.clear()


def cleanup(self, signal, frame):
    # Release MFRC522 resources
    GPIO.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    app = QApplication([])
    window = AddUserWindow()
    window.show()
    app.exec_()
