import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget to hold everything
        widget = QWidget()

        # Create a vertical layout to add widgets to
        layout = QVBoxLayout()

        # Add the layout to the widget
        widget.setLayout(layout)

        # Create the top band
        top_band = QWidget()
        top_band.setMaximumSize(480, 200)
        top_band.setStyleSheet("background-color: #000000")

        # Add logos and screen name to the top band
        logo1 = QLabel(top_band)
        logo1.setPixmap(QPixmap("tata-motors.jpeg"))
        logo2 = QLabel(top_band)
        logo2.setPixmap(QPixmap("e"))
        screen_name = QLabel("Screen Name", top_band)
        screen_name.setStyleSheet("color: #FFFFFF; font-size: 24px; font-weight: bold;")
        hlayout = QHBoxLayout()
        hlayout.addWidget(logo1)
        hlayout.addWidget(screen_name)
        hlayout.addWidget(logo2)
        hlayout.setAlignment(Qt.AlignCenter)

        # Set the layout for the top band
        top_band.setLayout(hlayout)
        top_band.setAlignment(Qt.AlignTop)

        # Add the top band to the main layout
        layout.addWidget(top_band)

        # Set the main widget
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
