from PyQt5 import QtWidgets


class InputWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Name:")
        self.text_input = QtWidgets.QLineEdit()

        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
