import csv
import sys
import os
import time
import signal
import RPi.GPIO as GPIO
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QInputDialog, QTextEdit
from mfrc522 import SimpleMFRC522

class AddUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Initialize window properties
    def initUI(self):
        self.setWindowTitle("Add User")
        self.resize(480, 800)
        
        # Initialize layout
        self.layout = QVBoxLayout()
        
        # Add user form fields
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.rfid_label = QLabel("RFID:")
        self.rfid_input = QLineEdit()
        self.rfid_button = QPushButton("Read RFID")
        self.rfid_button.clicked.connect(self.read_rfid)
        
        # Add on-screen keyboard
        self.keyboard = QTextEdit()
        self.keyboard.setReadOnly(True)
        self.keyboard.setFixedHeight(200)
        self.keyboard.setFixedWidth(400)
        self.keyboard.setStyleSheet("font-size: 20px;")
        self.keyboard.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        # Add form fields and keyboard to layout
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.rfid_label)
        self.layout.addWidget(self.rfid_input)
        self.layout.addWidget(self.rfid_button)
        self.layout.addWidget(self.keyboard)
        
        # Add submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        self.layout.addWidget(self.submit_button)
        
        # Set window layout
        self.setLayout(self.layout)
        
        # Initialize MFRC522 reader
        self.reader = SimpleMFRC522()
        
    def read_rfid(self):
        # Wait for card to be detected
        self.keyboard.setText("Please tap your RFID card on the reader.")
        try:
            id, rfid = self.reader.read()
            self.rfid_input.setText(str(id))
            self.keyboard.setText("RFID read successfully.")
        except Exception as e:
            self.keyboard.setText(f"Error reading RFID: {str(e)}")
    
    def submit_form(self):
        # Get form data
        name = self.name_input.text()
        rfid = self.rfid_input.text()
        
        # Validate form data
        if not name:
            self.show_error("Please enter a name.")
            return
        if not rfid:
            self.show_error("Please enter an RFID number.")
            return
        
        # Save user data to CSV file
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, rfid])
        
        # Clear form fields
        self.name_input.setText("")
        self.rfid_input.setText("")
        
        # Show success message
        self.show_success("User added successfully.")
    
    def show_error(self, message):
        # Show error message in on-screen keyboard
        self.keyboard.setText(f"Error: {message}")
    
    def show_success(self, message):
        # Show success message in on-screen keyboard
        self.keyboard.setText(f"Success: {message}")
    
    def cleanup(self, signal, frame):
        # Release MFRC522 resources
        GPIO.cleanup()
        sys.exit(0)
