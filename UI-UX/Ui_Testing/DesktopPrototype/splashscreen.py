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

        topband(self, "test")

        # set window title
        self.setWindowTitle("Splash Screen")

        # set window size
        self.resize(480, 800)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)


        # add logos to the first row (central logo )
        logo1 = QLabel()
        pixmap1 = QPixmap("images/ethos.jpg").scaled(370, 370, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo1.setPixmap(pixmap1)
        logo1.move(240,400)

        logo2 = QLabel()
        pixmap2 = QPixmap("images/gsk.jpg").scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo2.setPixmap(pixmap2)
        logo2.move(18, 10)

        logo3 = QLabel()
        pixmap3 = QPixmap("images/epitage.jpg").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo3.setPixmap(pixmap3)
        logo3.move(370, 10)

        # add system time to the second row
        time_label = QLabel()
        time_label.setObjectName("timeLabel")
        time_label.setAlignment(Qt.AlignCenter)
        time_label.setStyleSheet("font-size: 32px; color: black;")
        time_label.move(240,600)

        # add today's date to the third row
        date_label = QLabel()
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 32px;")
        date_label.move(240,700)

        # add menu button to the fourth row
        menu_button = QPushButton("Menu")
        menu_button.setFixedSize(120, 40)
        menu_button.move(240,750)
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
        current_time = QTime.currentTime().toString("hh:mm:ss")
        time_label.setText(current_time)

        # update the date label with today's date
        date_label = self.centralWidget().findChild(QLabel, "dateLabel")
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
