import csv
import os
import time
import signal
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
#from FingerPrintAddition import AddNewFingerPrint
from theme import BUTTON_STYLE
from theme import yellow_state
from mfrc522 import SimpleMFRC522
# Calling a file from a different folder
import sys
#sys.path.append('Device_Firmware/GT521F52-working/')

#import fps


class AddUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rfid_reader=SimpleMFRC522()
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
        self.rfid_label = QLabel('RFID:', self)
        self.rfid_label.move(50, 200)
        self.rfid_textbox = QPushButton(self)
        self.rfid_textbox.move(150, 200)
        self.rfid_textbox.resize(200, 30)
        self.rfid_textbox.setText("Scan your card:")  # TODO adding the str of the card
        self.rfid_textbox.clicked.connect(self.read_rfid)
        #self.submit_textbox.setText("Submit")
        #self.submit_textbox.clicked.connect(self.submit)
#        self.delete_textbox.setText("delete")
        self.rfid_textbox.setStyleSheet(yellow_state)

        # Add 'Save' button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(200, 250)
        self.save_btn.resize(100, 30)
        self.save_btn.clicked.connect(self.save_user)
        self.save_btn.setStyleSheet(BUTTON_STYLE)

        #self.rfid_reader=SimpleMFRC522()


    def read_rfid(self):
        try:
            id,text=self.rfid_reader.read()
            #self.rfid_input.setText("RFID read successful.")
            self.rfid.setText(str(id))
        except Exception as e:
            self.rfid_textbox.setText(str(e))


#self.fingerprint = AddNewFingerPrint()
 #       self.fingerprint.show()

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()
'''
    def save_user(self):
        # Get data from text boxes
        fn = self.fn_textbox.text()
        ln = self.ln_textbox.text()
        eid = self.eid_textbox.text()
        rfid = self.rfid_textbox.text().strip()
        #fp = self.efingerprint_textbox.text()
        if not id or not first_name or not last_name or not rfid:
            self.show_error("All fields are required")
            return

        # Check if the RFID value is already registered
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == rfid:
                    self.show_error("RFID already registered")
                    return

        # Write data to CSV file
        with open('users.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([fn, ln, eid, rfid])

        # Clear text boxes
        self.fn_textbox.clear()
        self.ln_textbox.clear()
        self.rfid_entry.clear()
        self.eid_textbox.clear()
'''
    def save_user(self):
        try:
            # Get user information from user
            #employee_id = self.id_input.text()
            #first_name = self.first_name_input.text()
            #last_name = self.last_name_input.text()
            fn = self.fn_textbox.text()
            ln = self.ln_textbox.text()
            eid = self.eid_textbox.text()


            # Prompt user to scan RFID card
            print("Place RFID card on reader or press Ctrl+C to c>
            rfid_id = self.rfid_reader.read_id()

            # Write user information to CSV file
            with open("users1.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([employee_id, first_name, last_na>

            print("RFID card associated with user successfully.")

        except KeyboardInterrupt:
            # User cancelled operation
            print("Operation cancelled.")

        except Exception as e:
            # Error occurred
            print("Error:", e)

        finally:
            # Close the connection to the RFID reader
            GPIO.cleanup()


if __name__ == '__main__':
    app = QApplication([])
    window = AddUserWindow()
    window.show()
    app.exec_()
