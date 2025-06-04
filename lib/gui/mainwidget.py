#
import os
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QVBoxLayout, QCommandLinkButton, QStatusBar, QSizePolicy
from PySide6.QtQuickWidgets import QQuickWidget

from .model_folder import ModelFolder
from .model_repo import ModelRepo
from .settings import Settings
from ..manager_jump import ManagerJump


class MainWidget(QWidget):

   def __init__(self, manager):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      # view
      self.quickView = QQuickWidget()
      self.quickView.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
      self.quickView.setResizeMode(QQuickWidget.SizeRootObjectToView)

      # models
      self.modelFolder = ModelFolder()
      self.quickView.rootContext().setContextProperty('folderModel', self.modelFolder)

      self.modelRepo = ModelRepo()
      self.quickView.rootContext().setContextProperty('repoModel', self.modelRepo)

      # load
      localPath = os.path.dirname(__file__)
      self.quickView.setSource(QUrl.fromLocalFile(localPath + '/qml/MainItem.qml'))

      # other
      self.removeButton = QCommandLinkButton('REMOVE', 'remove selected entries')
      self.statusBar = QStatusBar()  # without status bar, the window is not resizable in WSL

      # layout
      self.masterLayout = QVBoxLayout()
      self.setLayout(self.masterLayout)

      self.masterLayout.addWidget(self.quickView)
      self.masterLayout.addWidget(self.removeButton)
      self.masterLayout.addWidget(self.statusBar)

      # settings
      settings = Settings()
      print('settings @ ', settings.fileName())

      self.restoreGeometry(settings.value('geometry', b''))

   def closeEvent(self, event):

      settings = Settings()
      settings.setValue('geometry', self.saveGeometry())

      event.accept()

   def _jump(self, nameList):

      if not nameList:
         return

      name = nameList[0]
      jumpManager = ManagerJump(None, name)
      return jumpManager.execute()
