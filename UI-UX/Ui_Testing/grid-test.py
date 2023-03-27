from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("UI_Testing")

        # set window size
        self.setGeometry(100, 100, 480, 800)

        # create a grid layout with 3 rows and 2 columns
        layout_g = QGridLayout()
        self.setLayout(layout_g)

        # create six buttons and add them to the layout
        """
        button1 = QPushButton()
        svg_image = QImage("user-plus.svg")
        svg_image_scaled = svg_image.scaled(50,50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        button1.setIcon(QIcon(QPixmap.fromImage(svg_image_scaled)))
        button1.setIconSize(button1.size())
        button1.setFixedSize(100,100)
        """
        pixmap = QPixmap('UserReg_test.png').scaled(149, 149)

        # Create a QIcon object from the scaled pixmap
        icon = QIcon(pixmap)

        # Create a button and set its icon to the QIcon object
        UserReg_button = QPushButton()
        UserReg_button.setIcon(icon)
        UserReg_button.setIconSize(UserReg_button.size())
        # Set the fixed size of the button
        UserReg_button.setFixedSize(169, 169)
        #button1.setText("User Registration")
        layout_g.addWidget( UserReg_button, 0, 0)

        button2 = QPushButton()
        button2.setIcon(QIcon("Diagnostic_test.png"))
        button2.setIconSize(button2.size())
        button2.setFixedSize(button2.sizeHint())
        button2.setFixedSize(button2.width(), button2.width())
        layout_g.addWidget(button2, 0, 1)

        button3 = QPushButton()
        button3.setIcon(QIcon("icon.svg"))
        button3.setIconSize(button3.size())
        button3.setFixedSize(button3.sizeHint())
        button3.setFixedSize(button3.width(), button3.width())
        layout_g.addWidget(button3, 1, 0)

        button4 = QPushButton()
        button4.setIcon(QIcon("icon.svg"))
        button4.setIconSize(button4.size())
        button4.setFixedSize(button4.sizeHint())
        button4.setFixedSize(button4.width(), button4.width())
        layout_g.addWidget(button4, 1, 1)

        button5 = QPushButton()
        button5.setIcon(QIcon("icon.svg"))
        button5.setIconSize(button5.size())
        button5.setFixedSize(button5.sizeHint())
        button5.setFixedSize(button5.width(), button5.width())
        layout_g.addWidget(button5, 2, 0)

        button6 = QPushButton()
        button6.setIcon(QIcon("icon.svg"))
        button6.setIconSize(button6.size())
        button6.setFixedSize(button6.sizeHint())
        button6.setFixedSize(button6.width(), button6.width())
        layout_g.addWidget(button6, 2, 1)

if __name__ == '__main__':
    # create the application
    app = QApplication(sys.argv)

    # create the main window
    window = Window()

    # show the window
    window.show()

    # run the event loop
    sys.exit(app.exec_())
