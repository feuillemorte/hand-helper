from PyQt5 import QtWidgets as Widgets
from PyQt5 import uic


class SearchDialog(Widgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/ui/search_select_dialog.ui', self)
        self.show()

        self.chooseFromList.clicked.connect(self.get_query)

    def get_query(self):
        query, ok = Widgets.QInputDialog.getItem(
            self,
            'Select input dialog',
            'List of queries',
            ['Funny cats', 'Funny dogs', 'Funny birds'],
            0,
            False
        )

        if ok and query:
            self.queryText.setText(query)
