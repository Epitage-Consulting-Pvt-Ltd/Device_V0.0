from PyQt5 import QtWidgets, QtCore

class VirtualKeyboard(QtWidgets.QWidget):
    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.target = target

        self.setWindowTitle("Virtual Keyboard")

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.text_edit = QtWidgets.QTextEdit()
        layout.addWidget(self.text_edit)

        button_wrapper_layout = QtWidgets.QVBoxLayout()  # Added wrapper layout
        layout.addLayout(button_wrapper_layout)  # Added wrapper layout to main layout

        buttons = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M", "<-"]
        ]

        for row_buttons in buttons:
            button_layout = QtWidgets.QHBoxLayout()
            button_wrapper_layout.addLayout(button_layout)

            for button_text in row_buttons:
                button = QtWidgets.QPushButton(button_text)
                button.clicked.connect(lambda _, text=button_text: self.button_clicked(text))
                button_layout.addWidget(button)

    def button_clicked(self, button_text):
        if button_text == "<-":
            cursor = self.text_edit.textCursor()
            cursor.deletePreviousChar()
        else:
            self.text_edit.insertPlainText(button_text)
            self.target.setText(self.text_edit.toPlainText())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 480, 800)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        # Example name fields and labels
        self.name_field1 = QtWidgets.QLineEdit()
        self.name_field1.setPlaceholderText("Enter your name")
        self.name_field1.installEventFilter(self)

        self.name_label1 = QtWidgets.QLabel("Name:")
        self.name_label1.setCursor(QtCore.Qt.PointingHandCursor)
        self.name_label1.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
        self.name_label1.setLineWidth(1)
        self.name_label1.installEventFilter(self)

        self.name_field2 = QtWidgets.QLineEdit()
        self.name_field2.setPlaceholderText("Enter your name")
        self.name_field2.installEventFilter(self)

        self.name_label2 = QtWidgets.QLabel("Name:")
        self.name_label2.setCursor(QtCore.Qt.PointingHandCursor)
        self.name_label2.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
        self.name_label2.setLineWidth(1)
        self.name_label2.installEventFilter(self)

        layout.addWidget(self.name_label1)
        layout.addWidget(self.name_field1)
        layout.addWidget(self.name_label2)
        layout.addWidget(self.name_field2)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if obj in (self.name_field1, self.name_label1, self.name_field2, self.name_label2):
                self.show_virtual_keyboard(obj)
        return super().eventFilter(obj, event)

    def show_virtual_keyboard(self, target):
        virtual_keyboard = VirtualKeyboard(target)
        virtual_keyboard.show()

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
