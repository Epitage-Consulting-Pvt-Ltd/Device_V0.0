import sys

from PyQt5.QtCore import Qt, QTimer, QDate, QTime
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton

from MenuGrid import MenuWindow
from theme import BUTTON_STYLE, WINDOW_BACKGROUND_COLOR, \
    WINDOW_FOREGROUND_COLOR
from topband import topband


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #topband(self, "test")

        # set window title
        self.setWindowTitle("Splash Screen")

        # set window size
        self.resize(480, 800)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QGridLayout(central_widget)
        central_widget.setLayout(layout)

        # add logos to the first row (central logo)
        logo1 = QLabel(self)
        pixmap1 = QPixmap("images/ethos.png").scaled(370, 370, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo1.setPixmap(pixmap1)
        layout.addWidget(logo1, 1, 0, 1, 3,alignment=Qt.AlignCenter)

        logo2 = QLabel(self)
        pixmap2 = QPixmap("images/gsk.jpg").scaled(80,80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo2.setPixmap(pixmap2)
        layout.addWidget(logo2, 0, 0, 1, 2,alignment=Qt.AlignLeft)

        logo3 = QLabel(self)
        pixmap3 = QPixmap("images/epitage.jpg").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo3.setPixmap(pixmap3)
        layout.addWidget(logo3, 0, 1, 1, 3,alignment=Qt.AlignRight)

        layout.setVerticalSpacing(10)
        # add system time to the second row
        time_label = QLabel(self)
        time_label.setObjectName("timeLabel")
        time_label.setAlignment(Qt.AlignCenter)
        time_label.setStyleSheet("font-size: 32px; color: black;")
        layout.addWidget(time_label, 3, 0, 1, 3)


        # add today's date to the third row
        date_label = QLabel(self)
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 32px;")
        layout.addWidget(date_label, 4, 0, 1, 3)



        # add menu button to the fourth row
        menu_button = QPushButton("Menu", self)
        menu_button.setFixedSize(120, 40)
        layout.addWidget(menu_button, 5, 0, 1, 3, alignment=Qt.AlignCenter)
        menu_button.setStyleSheet(BUTTON_STYLE)
        menu_button.clicked.connect(self.show_menu_grid_window)
        menu_button.clicked.connect(self.close)

        # update the time and date labels every second
        timer = QTimer(self)
        timer.timeout.connect(self.update_labels)
        timer.start(1000)

    def update_labels(self):
        # update the time label with the current system time
        time_label = self.centralWidget().findChild(QLabel, "timeLabel")
        if time_label is not None:
            current_time = QTime.currentTime().toString("hh:mm:ss")
            time_label.setText(current_time)

        # update the date label with today's date
        date_label = self.centralWidget().findChild(QLabel, "dateLabel")
        if date_label is not None:
            current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
            date_label.setText(current_date)

    def show_menu_grid_window(self):
        self.menu_grid_window = MenuWindow()
        self.menu_grid_window.show()


if __name__ == '__main__':
    # create the application
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # show the window
    window.show()
    # run the event loop
    sys.exit(app.exec_())
