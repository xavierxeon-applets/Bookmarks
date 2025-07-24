import QtQuick

Rectangle {
    id: modelDelegate

    height: 40
    width: parent ? parent.width : 0

    color: model.bgcolor

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
            color: model.textcolor
        }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            model.interaction = 'clicked';
            modelDelegate.color = model.bgcolor; // Change color on click
        }
        onDoubleClicked: {
            model.interaction = 'doubleClicked';
            modelDelegate.color = model.bgcolor; // Change color on click
        }
    }
}
