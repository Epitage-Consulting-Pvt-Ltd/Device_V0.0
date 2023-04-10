from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QDate, QTime
from Me


import sys

class MainWindow(QMainWindow):
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

        '''
        # add system time to the second row
        time_label = QLabel()
        time_label.setAlignment(Qt.AlignCenter)
        layout_g.addWidget(time_label, 2, 1, 1, 2)

        '''

        # add today's date to the third row
        date_label = QLabel()
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 12px;")
        layout_g.addWidget(date_label, 2, 0, 1, 2)



        # add menu button to the fourth row
        menu_button = QPushButton("Menu")
        menu_button.setStyleSheet("font-size: 18px;")
        menu_button.setFixedSize(200, 50)
        layout_g.addWidget(menu_button, 3, 0, 1, 2, Qt.AlignCenter)
        #menu_button.clicked.connect(obj.__init__())

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



if __name__ == '__main__':
    # create the application
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # show the window
    window.show()
    # run the event loop
    sys.exit(app.exec_())