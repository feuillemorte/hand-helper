from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QInputDialog, QLabel, QTextEdit

from app.search_dialog import SearchDialog
from app.worker import Worker
from init import Setup
from scenarios.search_google import search, search_with_query

driver = Setup().driver


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(140, 50, 210, 25)

        self.logOutput = QTextEdit(self)
        self.logOutput.setReadOnly(True)
        self.log_with_html('<b>Log:</b>')

        self.initUI()

        self.t_finished = True

        self.thread = QThread()
        self.w = None

    def closeEvent(self, event):
        driver.quit()
        event.accept()

    @pyqtSlot()
    def onFinished(self):
        self.thread.quit()
        self.t_finished = True
        self.pbar.setValue(100)

        self.raise_()

    def initUI(self):
        QApplication.processEvents()
        lbl1 = QLabel('Progress:', self)
        lbl1.move(50, 52.5)

        self.logOutput.move(400, 50)
        self.logOutput.setMaximumHeight(500)
        self.logOutput.resize(400, 300)

        self.add_button('Search with google', 'Search with google', search, move_y=150)
        self.add_button(
            'Search with google (dialog)',
            'Search with google (dialog)',
            self.search_dialog,
            move_y=200,
            dialog=True
        )
        self.add_button(
            'Search with google (dialog 2)',
            'Search with google (dialog 2)',
            self.search_select_dialog,
            move_y=250,
            dialog=True
        )

        self.setGeometry(100, 100, 850, 400)
        self.setWindowTitle('Hand Helpers')
        self.show()

    def add_button(self, name, tip, func, move_x=50, move_y=100, btn_size=(300, 50), dialog=False):
        btn = QPushButton(name, self)
        btn.setToolTip(tip)
        btn.resize(btn_size[0], btn_size[1])
        btn.move(move_x, move_y)
        if not dialog:
            btn.clicked.connect(self.make_on_click(func))
        else:
            btn.clicked.connect(func)

    def search_dialog(self):
        text, ok = QInputDialog.getText(self, 'Search Dialog', 'Enter query:')

        if ok:
            self.start_thread(search_with_query, [text])

    def search_select_dialog(self):
        inputter = SearchDialog(self)
        if inputter.exec_():
            query = inputter.query_text.text()

            self.start_thread(search_with_query, [query])

    @pyqtSlot(str)
    def log_with_html(self, html):
        self.logOutput.append(html)

    @pyqtSlot(int)
    def fill_bar(self, i):
        self.pbar.setValue(i)

    def start_thread(self, func, *func_args):
        if self.t_finished:
            self.t_finished = False

            self.w = Worker(self.pbar, func, *func_args)
            self.w.finished.connect(self.onFinished)
            self.w.log[str].connect(self.log_with_html)
            self.w.progress_bar[int].connect(self.fill_bar)
            self.w.moveToThread(self.thread)
            self.thread.started.connect(self.w.work)
            self.thread.start()
        else:
            self.log_with_html('Process still working, please wait for ending')

    def make_on_click(self, func):
        def on_click():
            self.start_thread(func)

        return on_click
