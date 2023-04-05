from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QDate, QTime, QTimer
from PyQt5.QtGui import QIcon, QPixmap


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Splash Screen")

        # set window size
        self.setGeometry(100, 100, 480, 800)

        # create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a grid layout with 4 rows and 2 columns
        layout_g = QGridLayout()
        central_widget.setLayout(layout_g)

        # add logos to the first row
        logo1 = QLabel()
        pixmap1 = QPixmap("epitage_logo.jpg").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo1.setPixmap(pixmap1)
        layout_g.addWidget(logo1, 0, 0)

        logo2 = QLabel()
        pixmap2 = QPixmap("tata-motors.jpeg").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo2.setPixmap(pixmap2)
        layout_g.addWidget(logo2, 0, 1)

        # add system time to the second row
        time_label = QLabel()
        time_label.setAlignment(Qt.AlignCenter)
        layout_g.addWidget(time_label, 1, 0, 1, 2)

        # add today's date to the third row
        date_label = QLabel()
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 12px;")
        layout_g.addWidget(date_label, 2, 0, 1, 2)

        # create an instance of the object
        # obj = MenuWindow()

        # add menu button to the fourth row
        menu_button = QPushButton("Menu")
        menu_button.setStyleSheet("font-size: 18px;")
        menu_button.setFixedSize(200, 50)
        layout_g.addWidget(menu_button, 3, 0, 1, 2, Qt.AlignCenter)
        menu_button.clicked.connect(lambda: self.switch_window2(window2))

        # update the time and date labels every second
        timer = QTimer(self)
        timer.timeout.connect(self.update_labels)
        timer.start(1000)

    def update_labels(self):
        # update the time label with the current system time
        time_label = self.centralWidget().findChild(QLabel)
        current_time = QTime.currentTime().toString("hh:mm:ss")
        time_label.setText(current_time)

        # update the date label with today's date
        date_label = self.centralWidget().findChild(QLabel, "dateLabel")
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        date_label.setText(current_date)

    def switch_window2(self, window2):
        self.hide()
        window2.show()


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Main Window 2")

        # set window size
        self.setGeometry(100, 100, 480, 800)

        # create a button to switch to window 1
        switch_button = QPushButton("Switch to Window 1", self)
        switch_button.setGeometry(100, 100, 200, 50)
        switch_button.clicked.connect(self.switch_window1)

    def switch_window1(self):
        self.hide()
        window1.show()




if __name__ == '__main__':
    # create the application
    app = QApplication([])

    # create the main windows
    window1 = SplashScreen()
    window2 = MainWindow2()

    # show the first window
    window1.show()

    # run the event loop
    app.exec_()

