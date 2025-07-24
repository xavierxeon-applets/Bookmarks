import QtQuick

Rectangle
{
   color: palette.base
   
   ListView {
      anchors.fill: parent
    
      model: syncModel
      delegate: ModelDelegate {}
   }
}

