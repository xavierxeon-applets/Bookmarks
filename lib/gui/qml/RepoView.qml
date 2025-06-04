import QtQuick 2.0

ListView {

    Component {
        id: repoDelegate
        Item {
            id: myItem
            height: 40

            Column {
                Text {
                    text: '<b>' + model.name + '</b>'
                }
                Text {
                    text: model.url
                }
            }
        }
    }

    model: repoModel
    delegate: repoDelegate
}
