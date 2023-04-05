from PyQt5.QtWidgets import QApplication
from window1 import Window1
from window2 import Window2

if __name__ == '__main__':
    # create the application
    app = QApplication([])

    # create the main windows
    window1 = Window1()
    window2 = Window2()

    # set references to the other windows
    window1.window2 = window2
    window2.window1 = window1

    # show the first window
    window1.show()

    # run the event loop
    app.exec_()
