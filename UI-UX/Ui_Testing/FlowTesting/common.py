from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Common(QWidget):
    def __init__(self):
        super().__init__()

        # create a label
        label = QLabel("This is a common label")

        # create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(label)

        # set the layout for the widget
        self.setLayout(layout)
