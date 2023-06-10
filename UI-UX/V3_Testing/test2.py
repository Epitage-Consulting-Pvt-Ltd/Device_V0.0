from PyQt5 import QtWidgets
from components import load_combobox_with_autofill

app = QtWidgets.QApplication([])

# Create the combo box and text box
combo = QtWidgets.QComboBox()
autofill_textbox = QtWidgets.QLineEdit()

# Load the combo box with data from the CSV file
load_combobox_with_autofill(combo, 'EmpMaster-Epitage.csv', 'EmployeeName', autofill_textbox)

# Create a layout and add the combo box and text box to it
layout = QtWidgets.QVBoxLayout()
layout.addWidget(combo)
layout.addWidget(autofill_textbox)

# Create a main window and set the layout
window = QtWidgets.QWidget()
window.setLayout(layout)
window.show()

app.exec()
