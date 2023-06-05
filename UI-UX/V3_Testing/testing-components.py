from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

def create_button(text, parent, position, size, callback):
    button = QPushButton(text, parent)
    button.move(*position)
    button.setFixedSize(*size)
    button.clicked.connect(callback)
    return button

def create_labeled_textbox(label_text, parent, label_position, textbox_position, textbox_size):
    label = QLabel(label_text, parent)
    label.move(*label_position)

    textbox = QLineEdit(parent)
    textbox.move(*textbox_position)
    textbox.resize(*textbox_size)
    textbox.setEnabled(True)
    textbox.setParent(parent)

    return label, textbox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Window')
        self.setGeometry(100, 100, 400, 300)

        # Create 'Back' button
        self.back_btn = create_button('Back', self, (10, 60), (90, 40), self.show_menu_grid_window)

        # Create labeled textbox
        dob_label, dob_textbox = create_labeled_textbox('DOB:', self, (10, 100), (150, 100), (280, 25))



        self.show()

    def show_menu_grid_window(self):
        print("Back button clicked")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec_()
