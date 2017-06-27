from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog, QLabel, QGridLayout, QDialog, QVBoxLayout, QLineEdit,\
    QDialogButtonBox


class SearchDialog(QDialog):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        main_layout = QVBoxLayout()

        layout = QGridLayout()
        self.query = QLabel()
        self.query.setText('Enter query:')
        layout.addWidget(self.query, 1, 0)

        self.btn = QPushButton("Choose from list")
        self.btn.clicked.connect(self.getQuery)
        layout.addWidget(self.btn, 1, 3)

        self.query_text = QLineEdit()
        layout.addWidget(self.query_text, 1, 1)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons, 3, 0)

        main_layout.addLayout(layout)
        self.setLayout(main_layout)

        self.resize(500, 100)
        self.setWindowTitle('Search Dialog')

    def getQuery(self):
        query, ok = QInputDialog.getItem(
            self,
            'Select input dialog',
            'List of queries',
            ['Funny cats', 'Funny dogs', 'Funny birds'],
            0,
            False
        )

        if ok and query:
            self.query_text.setText(query)
