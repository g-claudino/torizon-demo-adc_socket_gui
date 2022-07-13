import QtQuick 2.15
import QtQuick.Controls 2.15
import QtCharts 2.15

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

        Button {
            id: button
            objectName: "mainButton"
            x: 520
            y: 430
            text: qsTr("-->")
            palette{
                buttonText: "black"
            }
        }

        Text {
            id: text1
            objectName: "title"
            x: 220
            y: 50
            width: 100
            height: 50
            text: qsTr("DEMO - Toradex")
            font.pixelSize: 30
        }

        Text {
            id: text2
            objectName: "sideText"
            x: 480
            y: 320
            text: qsTr("This demo application uses:\n - ADC \n - GPIO's \n - SOCKETS \n \n Please click bellow \n to change page")
            font.pixelSize: 12
            lineHeightMode: Text.ProportionalHeight
            fontSizeMode: Text.HorizontalFit
        }

        Text {
            id: text3
            objectName: "Temp"
            x: 8
            y: 200
            text: qsTr("Current Temperature [°C]: \n")
            font.pixelSize: 20
            lineHeightMode: Text.ProportionalHeight
            fontSizeMode: Text.HorizontalFit
        }
        Image {
            id: image
            objectName: "tordy"
            width: 130; height: 150
            fillMode: Image.PreserveAspectFit
            source: "Tordy_Hey.png"
            x: 480
            y: 150
        }
    }
}
