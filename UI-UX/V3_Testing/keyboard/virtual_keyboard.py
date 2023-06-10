from PyQt5 import QtWidgets

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


from PyQt5 import QtWidgets
import sys

# Create the main application window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setWindowTitle("Text Editor")
window.setGeometry(100, 100, 500, 500)

# Create the target text widget (QLineEdit or QTextEdit)
target_text = QtWidgets.QTextEdit()
window.setCentralWidget(target_text)

# Create the virtual keyboard widget
virtual_keyboard = VirtualKeyboard(target_text)

# Add the virtual keyboard widget to the main window
window.setCentralWidget(virtual_keyboard)

# Show the main window
window.show()

# Run the application event loop
sys.exit(app.exec_())
