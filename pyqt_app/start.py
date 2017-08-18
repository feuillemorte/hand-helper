# author: Oleg Sushchenko <fmorte@ya.ru>

import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets as Widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from app.main_window import MainWindow
from init import Setup, resource_path

# import for pyinstaller
import queue

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = Widgets.QSplashScreen(QtGui.QPixmap(resource_path('splash_img.png')))

    splash.showMessage('Starting browser and waiting for page load... ', Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
    splash.show()
    app.processEvents()

    app.processEvents()
    window = MainWindow()
    splash.showMessage('Starting application... ', Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
    app.processEvents()
    window.show()
    Setup().start_browser()
    splash.finish(window)
    sys.exit(app.exec_())
