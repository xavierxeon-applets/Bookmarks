import QtQuick

Rectangle {
    height: 40
    width: parent.width

    color: "red"

    Column {
        Item {
            height: 5
            width: 100
        }
        Text {
            text: '  ' + model.name
            font.bold: true
        }
        Text {
            text: '  ' + model.value
        }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            model.mouse = 'clicked';
        }
        onDoubleClicked: {
            model.mouse = 'doubleClicked';
        }
    }
}
