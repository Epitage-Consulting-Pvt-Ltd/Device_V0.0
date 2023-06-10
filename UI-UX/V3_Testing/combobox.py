from PyQt5 import QtWidgets
import csv

def create_combobox_widget(file_path, name_column, id_column):
    app = QtWidgets.QApplication([])

    def parse_csv_file(file_path):
        data = []

        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        data.append(row)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

        return data

    # Parse the specified columns from the provided CSV file
    data = parse_csv_file(file_path)
    name_column_index = None
    id_column_index = None
    names = []
    ids = []

    if len(data) > 0:
        header = data[0]
        if name_column in header and id_column in header:
            name_column_index = header.index(name_column)
            id_column_index = header.index(id_column)
            names = [row[name_column_index] for row in data[1:]]
            ids = [row[id_column_index] for row in data[1:]]

    name_combo = QtWidgets.QComboBox()
    name_combo.addItems(names)

    id_combo = QtWidgets.QComboBox()

    def name_selected(index):
        selected_name = name_combo.itemText(index)
        selected_index = names.index(selected_name)
        selected_id = ids[selected_index]
        id_combo.setCurrentText(selected_id)

    name_combo.currentIndexChanged.connect(name_selected)

    # completers only work for editable combo boxes. QComboBox.NoInsert prevents insertion of the search text
    name_combo.setEditable(True)
    name_combo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

    # change completion mode of the default completer from InlineCompletion to PopupCompletion
    name_combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

    # Disable editing for the ID combo
    id_combo.setEditable(False)

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(name_combo)
    layout.addWidget(id_combo)

    widget = QtWidgets.QWidget()
    widget.setLayout(layout)

    widget.show()
    app.exec()
