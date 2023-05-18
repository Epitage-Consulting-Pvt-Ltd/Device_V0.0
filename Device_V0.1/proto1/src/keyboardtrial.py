import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from mfrc522 import SimpleMFRC522
import csv
import RPi.GPIO as GPIO


class Keyboard(QWidget):
    def __init__(self, parent=None):
        super(Keyboard, self).__init__(parent)
        self.button_width = 40
        self.button_height = 40
        self.button_size = 24
        self.font_size = 12
        self.init_ui()

    def init_ui(self):
        self.resize(400, 300)
        self.setWindowTitle("Virtual Keyboard")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
        self.textbox = None
        self.create_buttons()

    def create_buttons(self):
        self.grid = QWidget(self)
        self.grid.setGeometry(0, 0, self.button_width * 10, self.button_height * 4)
        layout = [
            [
                ["`", "~"],
                ["1", "!"],
                ["2", "@"],
                ["3", "#"],
                ["4", "$"],
                ["5", "%"],
                ["6", "^"],
                ["7", "&"],
                ["8", "*"],
                ["9", "("],
                ["0", ")"],
                ["-", "_"],
                ["=", "+"],
                ["Backspace", "Backspace"],
            ],
            [
                ["q", "Q"],
                ["w", "W"],
                ["e", "E"],
                ["r", "R"],
                ["t", "T"],
                ["y", "Y"],
                ["u", "U"],
                ["i", "I"],
                ["o", "O"],
                ["p", "P"],
                ["[", "{"],
                ["]", "}"],
                ["\\", "|"],
            ],
            [
                ["a", "A"],
                ["s", "S"],
                ["d", "D"],
                ["f", "F"],
                ["g", "G"],
                ["h", "H"],
                ["j", "J"],
                ["k", "K"],
                ["l", "L"],
                [";", ":"],
                ["'", '"'],
                ["Enter", "Enter"],
            ],
            [
                ["Shift", "Shift"],
                ["z", "Z"],
                ["x", "X"],
                ["c", "C"],
                ["v", "V"],
                ["b", "B"],
                ["n", "N"],
                ["m", "M"],
                [",", "<"],
                [".", ">"],
                ["/", "?"],
                ["Clear", "Clear"],
            ],
        ]

        outer_layout = QVBoxLayout(self.grid)

        for row in layout:
            inner_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label[0], self.grid)
                button.setFont(QtGui.QFont("Arial", self.font_size))
                button.setMinimumSize(self.button_width, self.button_height)
                button.setMaximumSize(self.button_width, self.button_height)
                button.clicked.connect(lambda _, arg=label[0]: self.on_click(arg))
                inner_layout.addWidget(button)
            outer_layout.addLayout(inner_layout)

    def on_click(self, key):
        if key == "Enter":
            self.textbox.returnPressed.emit()
        elif key == "Backspace":
            self.textbox.backspace()
        elif key == "Clear":
            self.textbox.clear()
        # Show window
        self.show()


class RFIDWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize RFID reader
        self.rfid_reader = SimpleMFRC522()

        # Initialize user input fields
        self.id_label = QLabel("Employee ID:", self)
        self.id_input = QLineEdit(self)
        self.first_name_label = QLabel("First Name:", self)
        self.first_name_input = QLineEdit(self)
        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_input = QLineEdit(self)

        # Initialize button
        self.button = QPushButton("Register RFID Card", self)
        self.button.clicked.connect(self.register_rfid)

        # Set window size and title
        self.setGeometry(0, 0, 480, 800)
        self.setWindowTitle("RFID Registration")

        # Set widget positions
        self.id_label.move(50, 50)
        self.id_input.move(200, 50)
        self.first_name_label.move(50, 100)
        self.first_name_input.move(200, 100)
        self.last_name_label.move(50, 150)
        self.last_name_input.move(200, 150)
        self.button.move(200, 200)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rfid_window = RFIDWindow()
    sys.exit(app.exec_())
