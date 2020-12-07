from PySide2.QtWidgets import QTableView, QHeaderView, QAbstractItemView
from PySide2.QtCore import Qt

from custom_items.files_view_model import FilesViewModel



class FilesListView(QTableView):

    def __init__(self, width, height, widgetModel, parent = None):
        super(FilesListView, self).__init__(parent)

        self.setFixedSize(width, height)
        
        model = FilesViewModel(widgetModel, self)
        self.setModel(model)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        for column in range(self.horizontalHeader().count()):
            self.setColumnWidth(column, width/self.horizontalHeader().count())

        self.verticalHeader().setVisible(False)

        self.setShowGrid(False)

        self.horizontalHeader().setSortIndicatorShown(True)

        self.horizontalHeader().setHighlightSections(False)

        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setFocusPolicy(Qt.NoFocus)


