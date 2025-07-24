import QtQuick

Rectangle {
    id: header

    property string text
    width: parent.width
    height: 40
    color: palette.window

    Text {
        anchors.fill: parent

        padding: 10
        color: "black"
        text: header.text

        font.bold: true
        font.pixelSize: 20
        font.capitalization: Font.AllUppercase
    }
}
