import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, \
    QPushButton, QRadioButton
import csv
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR


class DeleteUserWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("Delete User")
        self.setGeometry(100, 100, 480, 800)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(25, 25)
        self.back_btn.setStyleSheet(BUTTON_STYLE)
        self.back_btn.clicked.connect(self.close)

        # Create vertical layout for the main window
        vbox = QVBoxLayout()

        # Create horizontal layout for the delete button and add it to the vertical layout
        hbox = QHBoxLayout()
        delete_btn = QPushButton("Delete")
        delete_btn.setStyleSheet(BUTTON_STYLE)
        delete_btn.clicked.connect(self.deleteRows)
        hbox.addStretch(1)
        hbox.addWidget(delete_btn)
        vbox.addLayout(hbox)

        # Create table widget and add it to the vertical layout
        self.table = QTableWidget()
        vbox.addWidget(self.table)

        # Read data from CSV file and populate table widget
        self.loadCSV()

        # Set the main layout for the window
        self.setLayout(vbox)

        # Show the window
        self.show()

    def loadCSV(self):
        # Open CSV file
        with open('users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        # Populate table widget with data from CSV file
        num_rows = len(data)
        num_cols = len(data[0])
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols + 1)
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(cell)
                self.table.setItem(i, j + 1, item)

            # Add radio button to the first column of each row
            radio_button = QRadioButton()
            radio_button.clicked.connect(self.selectRow)
            self.table.setCellWidget(i, 0, radio_button)

        # Set column headers
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("First Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Last Name"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Employee ID"))

    def selectRow(self):
        # Get selected radio button and select its row
        sender = self.sender()
        if sender.isChecked():
            row = self.table.indexAt(sender.pos()).row()
            self.table.selectRow(row)

    def deleteRows(self):
        # Get selected rows and delete them from the CSV file
        selected_rows = self.table.selectedItems()
        rows_to_delete = set()
        for item in selected_rows:
            row = item.row()
            rows_to_delete.add(row)
        rows_to_delete = sorted(rows_to_delete, reverse=True)
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i, row in enumerate(data):
                if i not in rows_to_delete:
                    writer.writerow(row)
        # Refresh table widget
        self.table.clearSelection()
        self.table.setRowCount(0)
        self.loadCSV()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeleteUserWindow()
    sys.exit(app.exec_())