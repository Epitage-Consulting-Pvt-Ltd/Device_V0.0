import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from mfrc522 import SimpleMFRC522
import csv
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
#from FingerPrintAddition import AddNewFingerPrint

from keyboard import MatchBoxLineEdit
from theme import BUTTON_STYLE

class AddUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize RFID reader
        self.rfid_reader = SimpleMFRC522()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add User")
        self.resize(480,800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 10)
        self.back_btn.clicked.connect(self.show_user_main_window)
        self.back_btn.clicked.connect(self.close)
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        
        # Initialize user input fields
        self.fn_label = QLabel('First Name:', self)
        self.fn_label.move(50,50)
        self.fn_textbox = MatchBoxLineEdit()
        self.fn_textbox.move(150, 50)
        self.fn_textbox.resize(200, 30)
        # Add Last Name
        self.ln_label = QLabel('Last Name:', self)
        self.ln_label.move(50,100)
        self.ln_textbox = MatchBoxLineEdit()
        self.ln_textbox.move(150, 100)
        self.ln_textbox.resize(200, 30)
        #Add Employee ID
        self.eid_label = QLabel('Employee ID:', self)
        self.eid_label.move(50, 150)
        self.eid_input = MatchBoxLineEdit()
        self.eid_textbox = MatchBoxLineEdit()
        self.eid_textbox.move(150, 150)
        self.eid_textbox.resize(200, 30)

        # Initialize button
        self.button = QPushButton('Scan your Card', self)
        #self.button_label.move(50,200)
        self.button.clicked.connect(self.register_rfid)
        #self.rfid_textbox.setStyleSheet(yellow_state)

        # Set window size and title
        #self.setGeometry(0, 0, 480, 800)
        #self.setWindowTitle('RFID Registration')

        # Add 'Save' button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(200, 250)
        self.save_btn.resize(100, 30)
        self.save_btn.clicked.connect(self.register_rfid)
        self.save_btn.setStyleSheet(BUTTON_STYLE)

        # Show window
        self.show()

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()

    def register_rfid(self):
        try:
            fn = self.fn_textbox.text()
            ln = self.ln_textbox.text()
            eid = self.eid_textbox.text()

            print("Place Card on reader.")
            rfid_id = self.rfid_reader.read_id()

            #with open("users.csv", "r") as file:
            #reader = csv.reader(file)
            #for row in reader:
            #    if rfid_id == row[3]:
            #        print("RFID Card is already registered.")
            #        return
            
            with open("users.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([fn, ln, eid, rfid_id])

            print("RFID Assignment Success.")

            self.fn_textbox.clear()
            self.ln_textbox.clear()
            self.eid_textbox.clear()

        except KeyboardInterrupt:
            print("User Manual Exit.")

        except Exception as e:
            print("Error:",e)

        finally:
            GPIO.cleanup()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddUserWindow()
    window.show()
    #rfid_window = RFIDWindow()
    sys.exit(app.exec_())
