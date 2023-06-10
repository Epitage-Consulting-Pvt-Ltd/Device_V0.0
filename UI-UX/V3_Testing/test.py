from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from components import LabeledComboBox

if __name__ == '__main__':
    app = QApplication([])

    window = QMainWindow()
    window.setWindowTitle("Labeled ComboBox Example")
    window.setGeometry(100, 100, 480, 800)

    widget = QWidget(window)
    layout = QVBoxLayout(widget)
    window.setCentralWidget(widget)

    labeled_combobox1 = LabeledComboBox("Select Name:", widget, (10, 10), (120, 10), (150, 25), "sample.csv", "name")
    labeled_combobox2 = LabeledComboBox("Employee ID", widget, (10, 10), (120, 10), (150, 25), "sample.csv", "name")

    labeled_combobox1.move(10,100)

    window.show()
    app.exec_()
