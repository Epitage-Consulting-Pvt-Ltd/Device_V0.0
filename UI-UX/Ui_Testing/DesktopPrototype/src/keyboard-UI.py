import csv
import os
from PyQt5 import QtWidgets, QtCore


class KeyboardApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Keyboard App")
        self.setGeometry(100, 100, 480, 320)  # Set the window size to match the 5" display

        # Create the input fields
        self.first_name_edit = QtWidgets.QLineEdit()
        self.last_name_edit = QtWidgets.QLineEdit()
        self.employee_id_edit = QtWidgets.QLineEdit()

        # Connect the focus events of the input fields to show the keyboard
        self.first_name_edit.installEventFilter(self)
        self.last_name_edit.installEventFilter(self)
        self.employee_id_edit.installEventFilter(self)

        # Create a layout for the input fields
        layout = QtWidgets.QFormLayout()
        layout.addRow("First Name:", self.first_name_edit)
        layout.addRow("Last Name:", self.last_name_edit)
        layout.addRow("Employee ID:", self.employee_id_edit)

        # Create a save button
        self.save_button = QtWidgets.QPushButton("Save")
        self.save_button.clicked.connect(self.save_details)
        layout.addRow(self.save_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusIn:
            if obj == self.first_name_edit or obj == self.last_name_edit or obj == self.employee_id_edit:
                self.show_keyboard()
        return super().eventFilter(obj, event)

    def show_keyboard(self):
        # Launch the Matchbox keyboard process
        os.system("matchbox-keyboard --xres 480 --yres 320")  # Set the keyboard size to match the display

    def save_details(self):
        # Retrieve the entered details
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        employee_id = self.employee_id_edit.text()

        # Save the details to a CSV file
        with open("employee_details.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([first_name, last_name, employee_id])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = KeyboardApp()
    window.show()
    sys.exit(app.exec_())
