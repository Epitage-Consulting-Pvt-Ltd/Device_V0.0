import sys
import csv
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from mfrc522 import SimpleMFRC522

class RFIDVerificationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RFID Verification")
        self.setGeometry(100, 100, 480, 800)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 380, 80)
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 16)
        self.label.setFont(font)

        self.button = QPushButton("Admin Scan", self)
        self.button.setGeometry(100, 200, 280, 80)
        self.button.setFont(font)
        self.button.clicked.connect(self.verify_rfid_card)

    def verify_rfid_card(self):
        self.label.setText("Please scan your card...")
        self.button.setEnabled(False)
        reader = SimpleMFRC522()
        
        try:
            id, text = reader.read()
            user_data = self.get_user_data()
            if text in user_data:
                self.label.setText("Access granted!")
                # Code to navigate to the next page or perform further actions
            else:
                self.label.setText("Invalid Admin Card")
        finally:
            self.button.setEnabled(True)
            reader.close()

    def get_user_data(self):
        user_data = []
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                user_data.append(row[0])
        return user_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RFIDVerificationWindow()
    window.show()
    sys.exit(app.exec_())
