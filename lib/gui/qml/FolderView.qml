import QtQuick 2.0

ListView {

    Component {
        id: folderDelegate
        Item {
            id: myItem
            height: 40

            Column {
                Text {
                    text: '<b>' + model.name + '</b>'
                }
                Text {
                    text: model.path
                }
            }
        }
    }

    model: folderModel
    delegate: folderDelegate
}
