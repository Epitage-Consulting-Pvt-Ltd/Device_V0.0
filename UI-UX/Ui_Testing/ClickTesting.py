from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MenuPage1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Page 1")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Go to Menu Page 2", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.go_to_menu_page2)

    def go_to_menu_page2(self):
        self.menu_page2 = MenuPage2()
        self.menu_page2.show()
        self.hide()

class MenuPage2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Page 2")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Go back to Menu Page 1", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.go_to_menu_page1)

    def go_to_menu_page1(self):
        self.menu_page1 = MenuPage1()
        self.menu_page1.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    menu_page1 = MenuPage1()
    menu_page1.show()
    app.exec_()
