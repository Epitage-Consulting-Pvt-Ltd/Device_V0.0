from PyQt5 import QtWidgets
from virtual_keyboard import VirtualKeyboard
from input_widget import InputWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    input_widget = InputWidget()
    virtual_keyboard = VirtualKeyboard(input_widget.text_input)

    window.setCentralWidget(input_widget)
    window.setWindowTitle("Virtual Keyboard Example")
    window.show()

    virtual_keyboard.show()

    app.exec_()
