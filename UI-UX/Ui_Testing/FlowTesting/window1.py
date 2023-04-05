from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QDate, QTime



class Screen1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screen 1')
        self.setGeometry(0, 0, 480, 800)

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

        # add today's date to the third row
        date_label = QLabel()
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("font-size: 12px;")
        layout_g.addWidget(date_label, 2, 0, 1, 2)

        button = QPushButton('Go to Screen 2', self)
        button.setGeometry(160, 700, 160, 80)
        button.clicked.connect(self.go_to_screen2)

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
        # date_label = self.centralWidget().findChild(QLabel, "dateLabel")
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        date_label.setText(current_date)

    def go_to_screen2(self):
        from window2 import Screen2
        self.screen2 = Screen2()
        self.screen2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    screen1 = Screen1()
    screen1.show()
    app.exec_()
