import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class AddUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add User")
        self.setGeometry(100, 100, 480, 800)

        # Add 'Back' button
        self.back_btn = QPushButton('Back', self)
        self.back_btn.move(10, 10)
        self.back_btn.clicked.connect(self.close)

        # Add First Name label and text box
        self.fn_label = QLabel('First Name:', self)
        self.fn_label.move(50, 50)
        self.fn_textbox = QLineEdit(self)
        self.fn_textbox.move(150, 50)
        self.fn_textbox.resize(200, 30)

        # Add Last Name label and text box
        self.ln_label = QLabel('Last Name:', self)
        self.ln_label.move(50, 100)
        self.ln_textbox = QLineEdit(self)
        self.ln_textbox.move(150, 100)
        self.ln_textbox.resize(200, 30)

        # Add Employee ID label and text box
        self.eid_label = QLabel('Employee ID:', self)
        self.eid_label.move(50, 150)
        self.eid_textbox = QLineEdit(self)
        self.eid_textbox.move(150, 150)
        self.eid_textbox.resize(200, 30)

        # Add 'Save' button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(150, 200)
        self.save_btn.resize(100, 30)
        self.save_btn.clicked.connect(self.save_user)

    def save_user(self):
        # Get data from text boxes
        fn = self.fn_textbox.text()
        ln = self.ln_textbox.text()
        eid = self.eid_textbox.text()

        # Write data to CSV file
        with open('users.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([fn, ln, eid])

        # Clear text boxes
        self.fn_textbox.clear()
        self.ln_textbox.clear()
        self.eid_textbox.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = AddUserWindow()
    window.show()
    app.exec_()
