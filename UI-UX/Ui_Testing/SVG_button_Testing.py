from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout
from pyqt_svg_button.svgButton import SvgButton

class SvgButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()
        self.setWindowTitle("SVG_Testing")
        # set window size
        self.setGeometry(100, 100, 480, 800)

    def __initUi(self):
        newButton = SvgButton()
        newButton.setIcon('user-plus.svg')
        openButton = SvgButton()
        openButton.setIcon('open.svg')
        saveButton = SvgButton()
        saveButton.setIcon('save.svg')
        lay = QHBoxLayout()
        lay.addWidget(newButton)
        lay.addWidget(openButton)
        lay.addWidget(saveButton)
        self.setLayout(lay)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = SvgButtonExample()
    ex.show()
    sys.exit(app.exec_())