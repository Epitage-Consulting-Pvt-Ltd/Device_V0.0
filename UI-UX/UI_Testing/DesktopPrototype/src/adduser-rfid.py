import csv
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
# Initialize RFID reader
rfid_reader = SimpleMFRC522()

try:
    # Get user information from user
    employee_id = input("Enter employee ID: ")
    first_name = input("Enter user's first name: ")
    last_name = input("Enter user's last name: ")
    
    # Prompt user to scan RFID card
    print("Place RFID card on reader or press Ctrl+C to cancel.")
    rfid_id = rfid_reader.read_id()

    # Write user information to CSV file
    with open("users1.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, first_name, last_name, rfid_id])

    print("RFID card associated with user successfully.")
    
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

