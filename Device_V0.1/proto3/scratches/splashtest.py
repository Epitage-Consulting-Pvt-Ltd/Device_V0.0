import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime

class DisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("../images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(3, 3, 160, 20)

        # Set font for date and time label
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)

        # Set font for date and time label
        font_big = QFont("inika", 20, QFont.Normal)

        self.logoImage = QLabel(self)
        self.logoImage.setPixmap(QPixmap("../images/img.png"))
        self.logoImage.setGeometry(50,154,381,277)



        # Create label for additional date
        self.additional_date_label = QLabel(self)
        self.additional_date_label.setGeometry(137, 509, 300,26)
        self.additional_date_label.setFont(font_big)
        self.additional_date_label.setAlignment(Qt.AlignVCenter)

        # Create label for time
        self.time_label = QLabel(self)
        self.time_label.setGeometry(207, 547, 300, 30)
        self.time_label.setFont(font_big)

        # Update date and time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        # Initial date and time display
        self.update_date_time()

    def update_date_time(self):
        # Get current date and time
        current_datetime = datetime.now()

        # Format the date as "14th June 2023"
        formatted_date = current_datetime.strftime("%d{} %B %Y").format(
            "th" if 10 <= current_datetime.day <= 19 else
            {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
        )

        # Get the current day
        current_day = current_datetime.strftime("%A")

        # Format the time as "hh:mm:ss"
        formatted_time = current_datetime.strftime("%H:%M:%S")

        # Update date and time labels
        current_datetime_str = f"{formatted_date} - {formatted_time}"
        self.date_time_label.setText(current_datetime_str)
        self.additional_date_label.setText(f"{current_day} , {formatted_date}")
        self.time_label.setText(formatted_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())
