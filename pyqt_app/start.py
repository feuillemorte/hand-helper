import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets as Widgets
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = Widgets.QSplashScreen(QtGui.QPixmap('splash_img.png'))

    splash.showMessage('Starting browser and application... ', Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
    splash.show()
    app.processEvents()

    from app.main_window import MainWindow

    app.processEvents()
    window = MainWindow()
    app.processEvents()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
