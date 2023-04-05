import csv
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Data Entry")

        # set window size
        self.setGeometry(100, 100, 480, 800)

        # create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a grid layout with 4 rows and 2 columns
        layout_g = QGridLayout()
        central_widget.setLayout(layout_g)

        # add name label and text field to the first row
        name_label = QLabel("Name:")
        layout_g.addWidget(name_label, 0, 0)

        self.name_field = QLineEdit()
        layout_g.addWidget(self.name_field, 0, 1)

        # add employee ID label and text field to the second row
        employee_id_label = QLabel("Employee ID:")
        layout_g.addWidget(employee_id_label, 1, 0)

        self.employee_id_field = QLineEdit()
        layout_g.addWidget(self.employee_id_field, 1, 1)

        # add submit button to the third row
        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("font-size: 18px;")
        submit_button.setFixedSize(200, 50)
        layout_g.addWidget(submit_button, 2, 0, 1, 2, Qt.AlignCenter)
        submit_button.clicked.connect(self.submit_data)

        # add table widget to the fourth row
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Name", "Employee ID"])
        self.table.setFixedSize(400, 400)
        layout_g.addWidget(self.table, 3, 0, 1, 2)

        # load existing data from CSV file, if any
        self.load_data()

    def submit_data(self):
        # get name and employee ID values from text fields
        name = self.name_field.text()
        employee_id = self.employee_id_field.text()

        # ensure both fields are non-empty
        if not name or not employee_id:
            QMessageBox.warning(self, "Error", "Both Name and Employee ID are required.")
            return

        # add data to the table widget
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(name))
        self.table.setItem(row_count, 1, QTableWidgetItem(employee_id))

        # save data to CSV file
        with open("data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, employee_id])

        # clear text fields
        self.name_field.clear()
        self.employee_id_field.clear()

    def load_data(self):
        # try to open CSV file and load data into the table widget
        try:
            with open("data.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    name = row[0]
                    employee_id = row[1]
                    row_count = self.table.rowCount()
                    self.table.insertRow(row_count)
                    self.table.setItem(row_count, 0, QTableWidgetItem(name))
                    self.table.setItem(row_count, 1, QTableWidgetItem(employee_id))
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    # create the application
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # show the window
    window.show()
    # run the event loop
    sys.exit(app.exec_())

