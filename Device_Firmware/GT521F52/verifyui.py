import csv
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

# Function to verify fingerprint
def verify_fingerprint(fingerprint):
    with open('fingerprint_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_fingerprint = row[0]
            if fingerprint == stored_fingerprint:
                return True
    return False

# PyQt5 button click event
def button_clicked():
    fingerprint = hashlib.md5("Fingerprint").hexdigest()  # Replace with actual fingerprint reading logic
    if verify_fingerprint(fingerprint):
        QMessageBox.information(window, 'Verification', 'Fingerprint verified!')
    else:
        QMessageBox.warning(window, 'Verification', 'Fingerprint not recognized.')

# Create the PyQt5 application
app = QApplication([])
window = QMainWindow()
button = QPushButton('Verify', window)
button.clicked.connect(button_clicked)
window.setCentralWidget(button)
window.show()
app.exec()
