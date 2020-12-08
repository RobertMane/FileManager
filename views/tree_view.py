from PySide2.QtWidgets import QTreeView, QFileIconProvider, QHeaderView
from PySide2.QtCore import QDir, Qt, Slot, QModelIndex

from custom_ui_items.empty_icon_provider import EmptyIconProvider
from model.tree_view_model import TreeViewModelItem
from utilities.system_manager import SystemManager

class TreeView(QTreeView):

    def __init__(self, widgetModel, widgetController, parent = None):
        super(TreeView, self).__init__(parent)
        self.model = TreeViewModelItem(self)
        self.setModel(self.model)              

        self.parent = parent

        self.__initialise()

        self._widgetModel = widgetModel
        self._widgetController = widgetController

        self.doubleClicked.connect(self._widgetController.change_tree_selected_item)
        self._widgetModel.tree_selection_changed.connect(self.on_tree_selection_changed)



    # PRIVATE METHODS

    def __initialise(self):
        self.setUniformRowHeights(True)
        self.setHeaderHidden(True)     

        columnCount = self.header().count()

        # Hiding every column excepting the first (name) 
        for index in range (1, columnCount):
            self.hideColumn(index)

    @Slot(QModelIndex)
    def on_tree_selection_changed(self, index):
        path = self.model.filePath(index)
        self.parent.setCurrentPath(path)





        

    

    
