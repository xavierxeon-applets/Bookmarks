#

from PySide6.QtCore import QSettings

from pathlib import Path


class Settings(QSettings):

   def __init__(self):

      _settingsPath = str(Path.home()) + '/.bookmarks/'
      QSettings.__init__(self, _settingsPath + 'gui_settings.ini', QSettings.IniFormat)
