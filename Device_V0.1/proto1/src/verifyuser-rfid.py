import csv
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
# Initialize RFID reader
rfid_reader = SimpleMFRC522()

try:
    # Prompt user to scan RFID card
    print("Place RFID card on reader or press Ctrl+C to cancel.")
    rfid_id = rfid_reader.read_id()

    # Check if RFID card is associated with a user in the CSV file
    with open("users1.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == str(rfid_id):
                # User found
                print("Verified user with ID:", row[1], row[2])
                break
        else:
            # User not found
            print("Access denied.")
    
except KeyboardInterrupt:
    # User cancelled operation
    print("Operation cancelled.")
    
except Exception as e:
    # Error occurred
    print("Error:", e)

finally:
    # Close the connection to the RFID reader
    GPIO.cleanup()
#rfid_reader.close()
