from PyQt5.QtCore import pyqtSignal, QObject


class Worker(QObject):
    finished = pyqtSignal()
    log = pyqtSignal(str)
    progress_bar = pyqtSignal(int)

    def __init__(self, pbar, func, *func_args):
        super().__init__()
        self.pbar = pbar
        self.func = func
        self.func_args = func_args

    def work(self):
        self.func(self.progress_bar, self.log, *self.func_args)
        self.finished.emit()
