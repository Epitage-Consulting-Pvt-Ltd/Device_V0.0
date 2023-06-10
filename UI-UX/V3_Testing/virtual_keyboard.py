from PyQt5 import QtWidgets
from keyboardPyQT import AlphaNeumericVirtualKeyboard

class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        self.virtual_keyboard = AlphaNeumericVirtualKeyboard(source=self)

    def mousePressEvent(self, event):
        # Call the virtual keyboard when the line edit is clicked
        self.virtual_keyboard.display()
        super(CustomLineEdit, self).mousePressEvent(event)
