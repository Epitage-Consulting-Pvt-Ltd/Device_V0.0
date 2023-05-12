from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

# Define theme variables
BACKGROUND_COLOR = '#F5F5F5'  # dark grey colour
FOREGROUND_COLOR = '#ffffff'  # white
ACCENT_COLOR = '#F29916'  # orange

BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {ACCENT_COLOR};
        color: {FOREGROUND_COLOR};
        font-size: 18px;
        font-family: Calibri, Arial, sans-serif;
        border-radius: 5px;
    }}
    QPushButton:hover {{
        background-color: #ff8c00;
    }}
"""


TABLE_STYLE = f"""
    QTableWidget {{
        background-color: {BACKGROUND_COLOR};
        color: {FOREGROUND_COLOR};
        border-radius: 5px;
    }}
    QHeaderView::section {{
        background-color: #2c3e50;
        color: {FOREGROUND_COLOR};
        font-weight: bold;
    }}
    QTableCornerButton::section {{
        background-color: #2c3e50;
        border: none;
    }}
"""
# Set window background and foreground colors
WINDOW_BACKGROUND_COLOR = QColor(245, 245, 245)  # gray
WINDOW_FOREGROUND_COLOR = Qt.white
RFID_WINDOW_FOREGROUND_COLOR = Qt.black

yellow_state ='background-color: yellow; border: 2px solid black; border-radius: 5px; font-size: 14px;'
green_state = 'background-color: red;border: 2px solid black; color: white; font-size: 12px; border-radius: 5px;'

FP_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {ACCENT_COLOR};
        color: {FOREGROUND_COLOR};
        border-radius: 5px;
    }}
    QPushButton:hover {{
        background-color: #ff8c00;
    }}
"""