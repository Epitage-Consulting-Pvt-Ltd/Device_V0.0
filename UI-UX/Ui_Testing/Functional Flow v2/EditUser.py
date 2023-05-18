import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, \
    QPushButton, QRadioButton
import csv
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR
from topband import topband

class DeleteUserWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI
        self.initUI()
        # Defining a Table Widget


    def initUI(self):
        # Set window title and size
        self.setWindowTitle("Delete User")
        self.resize(480, 800)

        topband(self)

        back_btn = QPushButton('Back', self)
        back_btn.setStyleSheet(BUTTON_STYLE)
        back_btn.clicked.connect(self.show_user_main_window)
        back_btn.clicked.connect(self.close)

        delete_btn = QPushButton("Delete")
        delete_btn.setStyleSheet(BUTTON_STYLE)
        delete_btn.clicked.connect(self.deleteRows)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # Add 'Back' button

        # Create vertical layout for the main window
        vbox = QVBoxLayout()



        # Create horizontal layout for the delete button and add it to the vertical layout
        hbox = QHBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(delete_btn)
        hbox.addWidget(back_btn)
        vbox.addLayout(hbox)
        self.table = QTableWidget(self)

        # Create a container widget for the table widget and add it to the vertical layout
        table_container = QWidget()
        table_container.setLayout(QVBoxLayout())

        table_container.layout().addWidget(self.table)
        vbox.addWidget(table_container)

        # Read data from CSV file and populate table widget
        self.loadCSV()

        # Set the position of the table container widget
        table_container.move(200, 200)

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

    def show_user_main_window(self):
        from UserMain_Working import UserMainWindow
        self.user_main_window = UserMainWindow()
        self.user_main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeleteUserWindow()
    sys.exit(app.exec_())
