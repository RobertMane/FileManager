from PySide2.QtWidgets import QTreeView
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import QItemSelectionModel

from custom_items.tree_view_model import TreeViewModelItem
from custom_items.directory_tree_item import DirectoryTreeItem
from utilities.system_manager import SystemManager

class TreeView(QTreeView):

    def __init__(self,parent = None):
        super(TreeView, self).__init__(parent)
        self.model = TreeViewModelItem(self)
        self.setModel(self.model)
        self.setUniformRowHeights(True)
        self.setHeaderHidden(True)
                
        # Populate data
        self.__populateData()

    # PRIVATE METHODS

    def __populateData(self):
        directoriesList = SystemManager.get_system_tree_structure()
        length = len(directoriesList)
        for index in range(length):
            parent = DirectoryTreeItem(directoriesList[index])
            self.model.appendRow(parent)


        

    

    
