#from fps import fps
import settings
import codecs
import logging

logging.basicConfig(format="[%(name)s][%(asctime)s] %(message)s")
logger = logging.getLogger("Fingerprint")
logger.setLevel(logging.INFO)

class Fingerprint():

    COMMENDS = {
        'None': 0x00,  # Default value for enum. Scanner will return error if sent this.
        'Open': 0x01,  # Open Initialization
        'Close': 0x02,  # Close Termination
        'UsbInternalCheck': 0x03,  # UsbInternalCheck Check if the connected USB device is valid
        'ChangeBaudrate': 0x04,  # ChangeBaudrate Change UART baud rate
        'SetIAPMode': 0x05,  # SetIAPMode Enter IAP Mode In this mode, FW Upgrade is available
        'CmosLed': 0x12,  # CmosLed Control CMOS LED
        'GetEnrollCount': 0x20,  # Get enrolled fingerprint count
        'CheckEnrolled': 0x21,  # Check whether the specified ID is already enrolled
        'EnrollStart': 0x22,  # Start an enrollment
        'Enroll1': 0x23,  # Make 1st template for an enrollment
        'Enroll2': 0x24,  # Make 2nd template for an enrollment
        'Enroll3': 0x25,
        # Make 3rd template for an enrollment, merge three templates into one template, save merged template to the database
        'IsPressFinger': 0x26,  # Check if a finger is placed on the sensor
        'DeleteID': 0x40,  # Delete the fingerprint with the specified ID
        'DeleteAll': 0x41,  # Delete all fingerprints from the database
        'Verify1_1': 0x50,  # Verification of the capture fingerprint image with the specified ID
        'Identify1_N': 0x51,  # Identification of the capture fingerprint image with the database
        'VerifyTemplate1_1': 0x52,  # Verification of a fingerprint template with the specified ID
        'IdentifyTemplate1_N': 0x53,  # Identification of a fingerprint template with the database
        'CaptureFinger': 0x60,  # Capture a fingerprint image(256x256) from the sensor
        'MakeTemplate': 0x61,  # Make template for transmission
        'GetImage': 0x62,  # Download the captured fingerprint image(256x256)
        'GetRawImage': 0x63,  # Capture & Download raw fingerprint image(320x240)
        'GetTemplate': 0x70,  # Download the template of the specified ID
        'SetTemplate': 0x71,  # Upload the template of the specified ID
        'GetDatabaseStart': 0x72,  # Start database download, obsolete
        'GetDatabaseEnd': 0x73,  # End database download, obsolete
        'UpgradeFirmware': 0x80,  # Not supported
        'UpgradeISOCDImage': 0x81,  # Not supported
        'Ack': 0x30,  # Acknowledge.
        'Nack': 0x31  # Non-acknowledge
    }

    PACKET_RES_0 = 0x55
    PACKET_RES_1 = 0xAA
    PACKET_DATA_0 = 0x5A
    PACKET_DATA_1 = 0xA5

    ACK = 0x30
    NACK = 0x31



if __name__ == '__main__':

    f = Fingerprint(settings.PORT_FINGERPRINTSCANNER, 115200)
   # f = Fingerprint(settings.ser, 9600)

    def signal_handler(signum, frame):
        f.close_serial()
    signal.signal(signal.SIGINT, signal_handler)

    if f.init():
        print("Open: %s" % str(f.open()))

        #f.delete()
        count = f.get_enrolled_cnt()

        ch = 0
        while ch != 4:
            print("no : of enrolled : %s" % str(count))
            print("1.Enroll")
            print("2.Delete")
            print("3.Verify")
            print("4.Exit")
            f1 = 0
            ch = input("Your Choice:  ")
            if ch == '1':
                while f.get_enrolled_cnt() != count + 1:
                    time.sleep(0.5)
                    idtemp = str(f.identify())
                    #idtemp = -1
                    if idtemp > "-1" and idtemp != "None":
                        print("You are an already existing User with ID : %s" %str(idtemp+1))
                        break
                    else:
                        if f.capture_finger():                      #capture_finger function
                            f.enroll()
                            time.sleep(0.5)
                            count = count + 1
                            print(" Successfully Enrolled!!!!")
                            break
                        else:
                            if f1 == 0:
                                print("e Place your finger")
                                f1 = 1
#                               break

            if ch == '2':
                did = input("Enter ID number to delete : ")
                print("Delete : %s" % str(did))
                count = 0

            if ch == '3':
                print("Place your Finger")
                #print(f.capture_finger())                      #capture_finger function

                #time.sleep(2)

                idtemp = f.identify()
                if f.capture_finger():                      #capture_finger function
                    if idtemp == -1:
                        GPIO.output(11,GPIO.HIGH)
                        print("You are not a valid user ")
                        time.sleep(1)
                        GPIO.output(11,GPIO.LOW)
                    elif idtemp >= 0:
                        GPIO.output(12,GPIO.HIGH)
                        print("You are an already existing User with ID : %s" %str(idtemp+1))
                        time.sleep(1)
                        GPIO.output(12,GPIO.LOW)
                else:
                    print("did not place finger")

            if ch == '4':
                print("Close: %s" % str(f.close()))
                f.ser.close()
                break

