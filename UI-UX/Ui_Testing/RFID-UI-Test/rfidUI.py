from time import sleep
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

import mrfc522

from RFIDDummyWindow import RFIDPromptDummy

# Enter the RFID number that you want to match
rfid_number = "1234567890"

reader = SimpleMFRC522()

app = QApplication(sys.argv)
widget = RFIDPromptDummy("sudarshanlogo.png","Rajesh Peche", "Epitage.png")
widget.show()

try:
    while True:
        print("Hold a tag near the reader")
        #id, text = reader.read()
        id,text = rfid_number # Just for bench testing
        print("ID: %s\nText: %s" % (id,text))
        if str(id) == rfid_number:
            print("RFID number matched!")
            widget.show()
            sleep(6)
            widget.hide()
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

sys.exit(app.exec_())
