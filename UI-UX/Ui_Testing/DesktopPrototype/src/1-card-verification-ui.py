import sys
import csv
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class CardVerificationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize RFID reader
        self.rfid_reader = SimpleMFRC522()

        # Set window size
        self.window_width = 480
        self.window_height = 800
        self.setGeometry(0, 0, self.window_width, self.window_height)

        # Set window title
        self.setWindowTitle("Card Verification")

        # Create label to display user details
        self.user_label = QLabel("Scan an RFID card", self)
        self.user_label.setGeometry(0, 0, self.window_width, self.window_height)
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setFont(QFont("Arial", 24))

        # Create verify button
        self.verify_button = QPushButton("Verify Card", self)
        self.verify_button.setGeometry(100, 200, 280, 60)
        self.verify_button.clicked.connect(self.verify_card)

        # Create timer for resetting the verify button
        self.reset_timer = QTimer()
        self.reset_timer.timeout.connect(self.reset_button)

    def verify_card(self):
        try:
            # Prompt user to scan RFID card
            self.user_label.setText("Place RFID card on reader or press Ctrl+C to cancel.")
            rfid_id = self.rfid_reader.read_id()

            # Check if RFID card is associated with a user in the CSV file
            with open("users1.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[3] == str(rfid_id):
                        # User found
                        self.user_label.setText("Verified user with ID: " + row[1])
                        break
                else:
                    # User not found
                    self.user_label.setText("Access denied.")

            # Start the timer for button reset
            self.reset_timer.start(5000)  # 30 seconds

        except KeyboardInterrupt:
            # User cancelled operation
            self.user_label.setText("Operation cancelled.")

        except Exception as e:
            # Error occurred
            self.user_label.setText("Error: " + str(e))

    def reset_button(self):
        # Reset the verify button and label
        self.user_label.setText("Scan an RFID card")
        self.verify_button.setEnabled(True)

    def closeEvent(self, event):
        # Close the connection to the RFID reader
        GPIO.cleanup()
        event.accept()


if __name__ == "__main__":
    # Initialize the PyQt application
    app = QApplication(sys.argv)

    # Create the main window
    window = CardVerificationApp()
    window.show()

    # Run the application event loop
    sys.exit(app.exec_())
