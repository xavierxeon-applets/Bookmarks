import QtQuick
import QtQuick.Layouts

Rectangle {

    color: palette.window

    GridLayout {
        id: grid
        anchors.fill: parent

        columns: 3
        columnSpacing: 5

        Header {
            text: "Folders"
            Layout.fillWidth: true
        }
        Header {
            text: "Repos"
            Layout.fillWidth: true
        }
        Header {
            text: "Sync"
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
        SyncView {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}
