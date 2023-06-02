from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit

# Declarations
btn_size_normal = (90,40)


def create_button(text, parent, position, size, clicked_slot):
    button = QPushButton(text, parent)
    button.move(*position)
    button.setFixedSize(*size)
    button.clicked.connect(clicked_slot)
    return button

def create_labeled_textbox(label_text, parent, label_position, textbox_position, textbox_size):
    label = QLabel(label_text, parent)
    label.move(*label_position)
    label.setParent(parent)

    textbox = QLineEdit(parent)
    textbox.move(*textbox_position)
    textbox.resize(*textbox_size)
    textbox.setEnabled(True)
    textbox.setParent(parent)

    label.show()
    textbox.show()

    return label, textbox
