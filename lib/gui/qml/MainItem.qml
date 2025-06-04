import QtQuick 2.0
import QtQuick.Layouts

Item {
    GridLayout {
        id: grid
        columns: 2
        anchors.fill: parent

        Text {
            text: "Folders"
            font.bold: true
        }
        Text {
            text: "Repos"
            font.bold: true
        }
        FolderView {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
        RepoView {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}
