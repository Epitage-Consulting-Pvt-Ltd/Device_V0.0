from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QDate, QTime

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Text Entry")

        # set window size
        self.setGeometry(100, 100, 480, 800)

        # create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a grid layout with 4 rows and 2 columns
        layout_g = QGridLayout()
        central_widget.setLayout(layout_g)

        # add a label and text field to the first row
        label1 = QLabel("Name:")
        layout_g.addWidget(label1, 0, 0)

        self.name_field = QLineEdit()
        layout_g.addWidget(self.name_field, 0, 1)

        # add a label and text field to the second row
        label2 = QLabel("EmployeeID:")
        layout_g.addWidget(label2, 1, 0)

        self.address_field = QLineEdit()
        layout_g.addWidget(self.address_field, 1, 1)


        # add a save button to the fourth row
        save_button = QPushButton("Save")
        save_button.setStyleSheet("font-size: 18px;")
        save_button.setFixedSize(200, 50)
        layout_g.addWidget(save_button, 3, 0, 1, 2, Qt.AlignCenter)
        save_button.clicked.connect(self.save_data)

    def save_data(self):
        # get the text entries from the fields
        name = self.name_field.text()
        address = self.address_field.text()
        comments = self.comments_field.toPlainText()

        # open the file in append mode and write the data
        with open("saved_data.txt", "a") as f:
            f.write(f"Name: {name}\n")
            f.write(f"EmployeeID: {address}\n")


        # clear the fields after saving the data
        self.name_field.clear()
        self.address_field.clear()
        self.comments_field.clear()

if __name__ == '__main__':
    # create the application
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # show the window
    window.show()
    # run the event loop
    sys.exit(app.exec_())
