from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from components import create_button ,create_labeled_textbox ,btn_size_normal
from topband_V3 import TopBandLayout

class MyWindow(TopBandLayout):
    def __init__(self, windowtitle, parent=None):
        super(MyWindow, self).__init__(windowtitle, parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("User Mangement")
        self.setGeometry(100, 100, 480, 800)

        self.back_btn = create_button('Back', self, (10, 60), btn_size_normal, self.show_menu_grid_window)
        self.add_btn = create_button('New Users', self, (10, 115), btn_size_normal, self.show_menu_grid_window)
        self.view_btn = create_button('Edit Users', self, (20, 100), btn_size_normal, self.show_menu_grid_window)
        self.delete_btn = create_button('Delete', self, (20, 60), btn_size_normal, self.show_menu_grid_window)

        ID_label, ID_textbox = create_labeled_textbox('ID:', self, (10, 100), (150, 100), (280, 25))
        Name_label, Name_textbox = create_labeled_textbox('Name:', self, (20, 100), (150, 120), (280, 25))

        self.show()

    def show_menu_grid_window(self):
        print("Back button clicked")




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow("User Mangement")
    app.exec_()