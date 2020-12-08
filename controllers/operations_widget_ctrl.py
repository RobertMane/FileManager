from PySide2.QtCore import QObject, Slot, Qt, QModelIndex
from PySide2.QtGui import QStandardItem

class OperationsWidgetController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(str)
    def change_combo_box_selection(self, index):
        self._model.combo_box_selection = index

    @Slot(QStandardItem)
    def change_files_list_selections(self, item):
        if item.checkState() == Qt.Checked:
            self._model.selected_items_append(item)
        else:
            self._model.selected_items_remove(item)

    @Slot(QModelIndex)
    def change_tree_selected_item(self, value):
        self._model.tree_selected_item = value

    @Slot(str)
    def change_current_path_text(self, value):
        self._model.current_path = value

    @Slot(str)
    def change_search_text(self, value):
        self._model.current_search = value

    @Slot(QModelIndex)
    def change_pressed_files_item(self, value):
        self._model.files_selected_item = value