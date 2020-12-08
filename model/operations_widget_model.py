from PySide2.QtCore import QObject, Signal, QModelIndex
from PySide2.QtGui import QStandardItem

from utilities.system_manager import SystemManager
from system_elements.directory import Directory

class OperationsWidgetModel(QObject):
    combo_box_selection_changed = Signal(str)

    selected_items_added = Signal(QStandardItem)
    selected_items_removed = Signal(QStandardItem)

    tree_selection_changed = Signal(QModelIndex)

    current_path_changed = Signal(str)

    current_search_changed = Signal(str)

    files_selection_changed = Signal(QModelIndex)


    # COMBO BOX CURRENT SELECTION
    @property
    def combo_box_selection(self):
        return self._combo_box_selection

    @combo_box_selection.setter
    def combo_box_selection(self, value):
        self._combo_box_selection = value
        self.combo_box_selection_changed.emit(value)

    # COMBO BOX LIST REPRESENTED BY SYSTEM DRIVES
    @property
    def combo_box_list(self):
        return self._combo_box_list

    @combo_box_list.setter
    def combo_box_selection(self, value):
        self._combo_box_list = value

    # ELEMENTS LIST
    @property
    def elements_list(self):
        return self._elements_list
    @elements_list.setter
    def elements_list(self, value):
        self._elements_list = value

    # SELECTED ITEMS
    @property
    def selected_items(self):
        return self._selected_items
    
    @selected_items.setter
    def selected_items(self, value):
        self._selected_items = value

    def selected_items_append(self, value):
        self._selected_items.append(value)
        self.selected_items_added.emit(value)

    def selected_items_remove(self, value):
        if (value in self._selected_items):
            self._selected_items.remove(value)
            self.selected_items_removed.emit(value)

    # DOUBLE CLICKED TREE VIEW ITEM
    @property
    def tree_selected_item(self):
        return self._tree_selected_item

    @tree_selected_item.setter
    def tree_selected_item(self, value):
        self._tree_selected_item = value
        self.tree_selection_changed.emit(value)

    @property
    def current_path(self):
        return self._currentPath

    @current_path.setter
    def current_path(self, value):
        self._currentPath = value
        self.current_path_changed.emit(value)

    @property
    def current_search(self):
        return self._currentSearch

    @current_search.setter
    def current_search(self, value):
        self._currentSearch = value
        self.current_search_changed.emit(value)

    # DOUBLE CLICKED TREE VIEW ITEM
    @property 
    def files_selected_item(self):
        return self._files_selected_item

    @files_selected_item.setter
    def files_selected_item(self, value):
        self._files_selected_item = value
        self.files_selection_changed.emit(value)



    def __init__(self):
        super().__init__()

        self._combo_box_list = SystemManager.get_drives()

        self._elements_list = Directory.get_all_subelements(self._combo_box_list[0])
        self._currentPath = self._combo_box_list[0]
        self._selected_items = list()

        

    