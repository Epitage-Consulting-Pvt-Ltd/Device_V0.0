from GT521F52.fps import fps
import settings

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
