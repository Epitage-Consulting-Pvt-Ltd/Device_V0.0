from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title and size
        self.setWindowTitle("Text to Table")
        self.setGeometry(100, 100, 480, 800)

        # create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a grid layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # create text field
        self.text_field = QLineEdit()
        layout.addWidget(self.text_field, 0, 0)

        # create button
        button = QPushButton("Add to Table")
        layout.addWidget(button, 0, 1)

        # create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Text"])
        layout.addWidget(self.table, 1, 0, 1, 2)

        # connect button signal to slot
        button.clicked.connect(self.add_to_table)

    def add_to_table(self):
        # get text from text field
        text = self.text_field.text()

        # create table row
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # add text to table
        text_item = QTableWidgetItem(text)
        self.table.setItem(row_position, 0, text_item)

        # clear text field
        self.text_field.setText("")


if __name__ == '__main__':
    # create the application
    app = QApplication([])
    # create the main window
    window = MainWindow()
    # show the window
    window.show()
    # run the event loop
    app.exec_()
