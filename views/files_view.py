from PySide2.QtWidgets import QTableView, QHeaderView, QAbstractItemView
from PySide2.QtCore import Qt, Slot, QModelIndex
from PySide2.QtGui import QStandardItem
import os

from model.files_view_model import FilesViewModel



class FilesListView(QTableView):

    def __init__(self, width, height, widgetModel, widgetController, parent = None):
        super(FilesListView, self).__init__(parent)

        self.setFixedSize(width, height)

        self._parent = parent

        self._widgetModel = widgetModel
        self._widgetController = widgetController
        
        model = FilesViewModel(widgetModel, widgetController, parent, self)
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

        self.doubleClicked.connect(self._widgetController.change_pressed_files_item)

        self._widgetModel.files_selection_changed.connect(self.on_pressed_item_changed)

    
    @Slot(QModelIndex)
    def on_pressed_item_changed(self, index):
        name = index.data()
        currentPath = self._parent.currentPathLineEdit.text()
        path = os.path.join(currentPath, name)

        if os.path.isfile(path):
            os.startfile(path)
        else:
            self._parent.setCurrentPath(path)


