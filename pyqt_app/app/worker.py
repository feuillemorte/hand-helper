# author: Oleg Sushchenko <fmorte@ya.ru>

import traceback

from PyQt5.QtCore import pyqtSignal, QObject
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, TimeoutException


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
            self.func(self.progress_bar, self.log, *self.func_args)
        except (AttributeError, TimeoutException, WebDriverException, NoSuchWindowException) as e:
            self.log.emit('Message: {}.\nPlease, try again'.format(e))
            self.log.emit('If you get this error again, please contact to developer and send this text:')
            self.log.emit('==========SEND THIS TO DEVELOPER==========')
            self.log.emit(traceback.format_exc())
            self.log.emit('=====================================')
        except (InterruptedError, Exception) as e:
            trace = traceback.format_exc()
            self.log.emit('Something went wrong. Please contact to developer and send this text:')
            self.log.emit('==========SEND THIS TO DEVELOPER==========')
            self.log.emit('Message: {}'.format(e))
            self.log.emit(trace)
            self.log.emit('=====================================')
        finally:
            self.finished.emit()
