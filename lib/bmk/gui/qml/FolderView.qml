import QtQuick

Rectangle
{
   color: palette.base
   
   ListView {
      anchors.fill: parent
    
      model: folderModel
      delegate: ModelDelegate {}
   }
}

