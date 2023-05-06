import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem
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

        # Initialize message label
        self.message_label = QLabel('', self)

        # Initialize user list section
        self.user_list_label = QLabel('Registered Users', self)
        self.user_table = QTableWidget(self)
        self.user_table.setColumnCount(4)
        self.user_table.setHorizontalHeaderLabels(['Employee ID', 'First Name', 'Last Name', 'RFID ID'])
        self.load_user_list()

        # Add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.button)
        layout.addWidget(self.message_label)
        layout.addWidget(self.user_list_label)
        layout.addWidget(self.user_table)
        self.setLayout(layout)

        # Set window size and title
        self.setGeometry(0, 0, 480, 800)
        self.setWindowTitle('RFID Registration')

        # Show window
        self.show()

    def register_rfid(self):
        try:
            # Get user information from user
            employee_id = self.id_input.text()
            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()

            # Prompt user to scan RFID card
            self.message_label.setText('Place RFID card on reader or press Ctrl+C to cancel.')
            rfid_id = self.rfid_reader.read_id()

            # Write user information to CSV file
            with open("users.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([employee_id, first_name, last_name, rfid_id])

            self.message_label.setText('RFID card associated with user successfully.')
            self.load_user_list()

        except KeyboardInterrupt:
            # User cancelled operation
            self.message_label.setText('Operation cancelled.')

        except Exception as e:
            # Error occurred
            self.message_label.setText('Error: ' + str(e))

        finally:
            # Close the connection to the RFID reader
            GPIO.cleanup()

    def load_user_list(self):
        # Clear existing data in table
        self.user_table.setRowCount(0)

        # Read user data from CSV file
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                employee_id = row[0]
                first_name = row[1]
                last_name = row[2]
                rfid_id = row[3]

                # Add row to table
                row_position = self.user_table.rowCount()
                self.user_table.insertRow(row_position)
                self.user_table.setItem
