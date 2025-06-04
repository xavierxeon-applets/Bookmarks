import QtQuick
import QtQuick.Layouts

Rectangle {
    color: palette.base

    GridLayout {
        id: grid
        anchors.fill: parent

        columns: 2
        columnSpacing: 0

        Header {
            text: "Folders"
            Layout.fillWidth: true
        }
        Header {
            text: "Repos"
            Layout.fillWidth: true
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
