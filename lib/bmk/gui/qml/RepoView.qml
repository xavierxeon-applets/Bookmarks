import QtQuick

Rectangle
{
   color: palette.base
   
   ListView {
      anchors.fill: parent
    
      model: repoModel
      delegate: ModelDelegate {}
   }
}
