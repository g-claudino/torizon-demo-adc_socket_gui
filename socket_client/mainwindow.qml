import QtQuick 2.0
import QtQuick.Controls 2.0

Rectangle {
    width: 200
    height: 200
    color: "green"

    Text {
        id: mytext2
        objectName: "mytext2"
        text: "Hello World"
        anchors.centerIn: parent
    }

    Button {
        id: mybutton2
        objectName: "secondButton"
        text: "Hello"
    }
}
