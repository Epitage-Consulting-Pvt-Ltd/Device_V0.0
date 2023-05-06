import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from mfrc522 import SimpleMFRC522
import csv
import RPi.GPIO as GPIO

class RFIDWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize RFID reader
        self.rfid_reader = SimpleMFRC522()

        # Initialize user input fields
        self.id_label = QLabel('Employee ID:', self)
        self.id_input = QLineEdit(self)
        self.first_name_label = QLabel('First Name:', self)
        self.first_name_input = QLineEdit(self)
        self.last_name_label = QLabel('Last Name:', self)
        self.last_name_input = QLineEdit(self)

        # Initialize button
        self.button = QPushButton('Register RFID Card', self)
        self.button.clicked.connect(self.register_rfid)

        # Set window size and title
        self.setGeometry(0, 0, 480, 800)
        self.setWindowTitle('RFID Registration')

        # Set widget positions
        self.id_label.move(50, 50)
        self.id_input.move(200, 50)
        self.first_name_label.move(50, 100)
        self.first_name_input.move(200, 100)
        self.last_name_label.move(50, 150)
        self.last_name_input.move(200, 150)
        self.button.move(200, 200)

        # Show window
        self.show()

    def register_rfid(self):
        try:
            # Get user information from user
            employee_id = self.id_input.text()
            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()

            # Prompt user to scan RFID card
            print("Place RFID card on reader or press Ctrl+C to cancel.")
            rfid_id = self.rfid_reader.read_id()

            # Write user information to CSV file
            with open("users1.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([employee_id, first_name, last_name, rfid_id])

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
    app = QApplication(sys.argv)
    rfid_window = RFIDWindow()
    sys.exit(app.exec_())
