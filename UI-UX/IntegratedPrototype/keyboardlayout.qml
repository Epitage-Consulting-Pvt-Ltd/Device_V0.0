import QtQuick 2.0
import QtQuick.VirtualKeyboard 2.2

Keyboard {
    id: keyboard
    
    
    Layout {
        id: layout
        Key {
            text: "A"
            keyCode: Qt.Key_A
            width: 50
            height: 50
            font.pixelSize: 20
            background: Rectangle {
                color: "red"
                radius: 5
            }
        }
        // add more keys here
    }
}

}
