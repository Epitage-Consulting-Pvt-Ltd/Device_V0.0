from time import sleep
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from splashscreen import MainWindow

import MFRC522

from RFIDDummyWindow import RFIDPromptDummy

# Enter the RFID number that you want to match
#rfid_number = reader.read()

reader = SimpleMFRC522()

#app = QApplication(sys.argv)
#widget = RFIDPromptDummy("sudarshanlogo.png","Rajesh Peche", "Epitage.png")
#widget.show()

def show_splashscreen_window(self):
	self.splashscreen_window=MenuWindow()
	self.splashscreen_window.show()

try:
    while True:
        print("Hold a tag near the reader")
        #id, text = reader.read()
        id,text = reader.read() # Just for bench testing
        print("ID: %s\nText: %s" % (id,text))
#        if str(id) == id:
        print("RFID number matched!")
        self.show_splashscreen_window()
	#widget.show()
        sleep(6)
        #widget.hide()
        #sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

sys.exit(app.exec_())
