# author: Oleg Sushchenko <fmorte@ya.ru>

import selenium
from PyQt5.QtCore import pyqtSignal, QObject


class Worker(QObject):
    finished = pyqtSignal()
    log = pyqtSignal(str)
    progress_bar = pyqtSignal(int)

    def __init__(self, progressBar, func, *func_args):
        super().__init__()
        self.progressBar = progressBar
        self.func = func
        self.func_args = func_args

    def work(self):
        try:
            self.func(self.progress_bar, *self.func_args)
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.WebDriverException) as e:
            self.log.emit('Message: {}.\nPlease, try again or contact to developer'.format(e))

        self.finished.emit()
