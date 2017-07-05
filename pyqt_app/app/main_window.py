import PyQt5.QtWidgets as Widgets
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSlot

from app.search_dialog import SearchDialog
from app.worker import Worker
from init import Setup
from scenarios.search_google import search, search_with_query

driver = Setup().driver
config = Setup().config


class MainWindow(Widgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/ui/main_window.ui', self)

        self.log_with_html('<b>Log:</b>')
        self.configView.append('<br>'.join('<b>{}:</b> {}'.format(key, val) for key, val in config['common'].items()))
        self.t_finished = True
        self.thread = QThread()
        self.w = None

        self.search.clicked.connect(lambda: self.start_thread(search))
        self.searchDialog.clicked.connect(self.search_select_dialog)
        self.searchDialog2.clicked.connect(self.search_dialog)

    def search_select_dialog(self):
        inputter = SearchDialog()
        if inputter.exec_():
            query = inputter.queryText.text()

            self.start_thread(search_with_query, query)

    def search_dialog(self):
        text, ok = Widgets.QInputDialog.getText(self, 'Search Dialog', 'Enter query:')

        if ok:
            self.start_thread(search_with_query, [text])

    def closeEvent(self, event):
        driver.quit()
        event.accept()

    def start_thread(self, func, *func_args):
        if self.t_finished:
            self.t_finished = False

            self.w = Worker(self.progressBar, func, *func_args)
            self.w.finished.connect(self.on_finished)
            self.w.log[str].connect(self.log_with_html)
            self.w.progress_bar[int].connect(self.fill_bar)
            self.w.moveToThread(self.thread)
            self.thread.started.connect(self.w.work)
            self.thread.start()
        else:
            self.log_with_html('Process still working, please wait for ending')

    @pyqtSlot(str)
    def log_with_html(self, html):
        self.logView.append(html)

    @pyqtSlot(int)
    def fill_bar(self, i):
        self.progressBar.setValue(i)

    @pyqtSlot()
    def on_finished(self):
        self.thread.quit()
        self.t_finished = True
        self.progressBar.setValue(100)

        self.raise_()
