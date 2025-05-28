#

import signal
import sys


from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from .mainwidget import MainWidget


def signit_handler(*args):

   QApplication.quit()


def main_gui(manager):

   app = QApplication([])

   signal.signal(signal.SIGINT, signit_handler)
   timer = QTimer()
   timer.start(500)
   timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.

   mw = MainWidget(manager)
   mw.show()

   sys.exit(app.exec())
