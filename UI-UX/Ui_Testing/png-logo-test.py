from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])

# Load the image file and scale it to the size of the button
pixmap = QPixmap('UserReg_test.png').scaled(149, 149)

# Create a QIcon object from the scaled pixmap
icon = QIcon(pixmap)

# Create a button and set its icon to the QIcon object
UserReg_button = QPushButton()
UserReg_button.setIcon(icon)
UserReg_button.setIconSize(UserReg_button.size())
# Set the fixed size of the button
UserReg_button.setFixedSize(169, 169)

# Show the button
UserReg_button.show()

app.exec_()
