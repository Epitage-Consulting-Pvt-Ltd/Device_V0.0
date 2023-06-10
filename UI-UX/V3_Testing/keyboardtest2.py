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
                button.clicked.connect(self.button_clicked)
                button_layout.addWidget(button)

    def button_clicked(self):
        button = self.sender()
        if button:
            button_text = button.text()
            if button_text == "<-":
                cursor = self.text_edit.textCursor()
                cursor.deletePreviousChar()
            else:
                self.text_edit.insertPlainText(button_text)
                self.target.setText(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    label = QtWidgets.QLabel("Text Input:")
    text_input = QtWidgets.QLineEdit()
    virtual_keyboard = VirtualKeyboard(text_input)

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(text_input)

    central_widget = QtWidgets.QWidget()
    central_widget.setLayout(layout)

    window.setCentralWidget(central_widget)
    window.setWindowTitle("Virtual Keyboard Example")
    window.show()

    virtual_keyboard.show()

    app.exec_()
