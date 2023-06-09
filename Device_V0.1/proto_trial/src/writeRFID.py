import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
GPIO.setwarnings(False)
GPIO.setup(pin_rst, GPIO.OUT)
def write():
    try:
        text = input('Enter your roll no.: ')
        if text.isdigit():
            print("Now place your card.")
            reader.write(text)
            return text
        else:
            print("Roll no should be int.")
            return write()
    except Exception as e:
        return e
    finally:
        GPIO.cleanup()
