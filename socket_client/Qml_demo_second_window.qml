import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 640
    height: 480
    property alias rectangle: rectangle
    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 640
        height: 480
        color: "#00508c"
        border.color: "#003969"

        Rectangle {
            id: rectangle1
            x: 50
            y: 100
            width: 540
            height: 300
            color: "#ffffff"

            Text {
                id: text2
                objectName: "textOS"
                x: 8
                y: 16
                text: qsTr("Text")
                font.pixelSize: 20
            }
        }
    }
    Button {
        id: button
        x: 50
        y: 430
        text: qsTr("<--")
        objectName: "mainButton"
        palette{
            buttonText: "black"
        }
    }

    Text {
        id: text1
        x: 140
        y: 50
        objectName: "textmain"
        width: 100
        height: 50
        text: qsTr("DEMO - Container Information")
        font.pixelSize: 30
    }
}
