from components import create_labeled_combobox
from PyQt5.QtCore import Qt

label_text = "Select Name:"
parent = self# Provide the appropriate parent widget
label_position = (10, 10)  # Specify the label position (x, y)
combobox_position = (120, 10)  # Specify the combobox position (x, y)
combobox_size = (150, 25)  # Specify the combobox size (width, height)
file_path = "sample.csv"  # Specify the CSV file path
column_name = "Name"  # Specify the desired column name

label, combobox = create_labeled_combobox(label_text, parent, label_position, combobox_position, combobox_size, file_path, column_name)
