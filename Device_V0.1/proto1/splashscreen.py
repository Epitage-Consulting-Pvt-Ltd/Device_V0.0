from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPalette, QFont
from PyQt5.QtCore import Qt, QTimer, QDate, QTime
from MenuGrid import MenuWindow
from topband import topband
from theme import BACKGROUND_COLOR, FOREGROUND_COLOR, ACCENT_COLOR, BUTTON_STYLE, TABLE_STYLE , WINDOW_BACKGROUND_COLOR, WINDOW_FOREGROUND_COLOR
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #topband(self ,"test")

        # set window title
        self.setWindowTitle("Splash Screen")

        # set window size
        self.resize(480, 800)

        # Set window background and foreground colors
        palette = self.palette()
        palette.setColor(QPalette.Window, WINDOW_BACKGROUND_COLOR)
        palette.setColor(QPalette.WindowText, WINDOW_FOREGROUND_COLOR)
        self.setPalette(palette)

        # create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a grid layout with 4 rows and 2 columns
        layout_g = QGridLayout()
        central_widget.setLayout(layout_g)

        # add logos to the first row
        logo1 = QLabel()
        pixmap1 = QPixmap("image/ethos.jpg").scaled(370, 370, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo1.setPixmap(pixmap1)
        layout_g.addWidget(logo1, 1, 0, 3, 0, Qt.AlignCenter)

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
        time_label.setStyleSheet("fint-size: 32px;")
        layout_g.addWidget(time_label, 3, 1, 1, 2)


        # add today's date to the third row
        date_label = QLabel()
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 32px;")
        layout_g.addWidget(date_label, 3, 0, 2, 4)



        # add menu button to the fourth row
        menu_button = QPushButton("Menu")
        menu_button.setFixedSize(120, 40)
        layout_g.addWidget(menu_button, 4, 0, 1, 4, Qt.AlignCenter)
        menu_button.setStyleSheet(BUTTON_STYLE)
        menu_button.clicked.connect(self.show_menu_grid_window)
        menu_button.clicked.connect(self.close)


        # update the time and date labels every second
        timer = QTimer(self)
        timer.timeout.connect(self.update_labels)
        timer.start(1000)

    def update_labels(self):

        '''
        # update the time label with the current system time
        time_label = self.centralWidget().findChild(QLabel)
        current_time = QTime.currentTime().toString("hh:mm:ss")
        time_label.setText(current_time)
        '''

        # update the date label with today's date
        date_label = self.centralWidget().findChild(QLabel, "dateLabel")
        #date_label = self.centralWidget().findChild(QLabel, "dateLabel")
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
