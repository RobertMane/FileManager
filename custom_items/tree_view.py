from PySide2.QtWidgets import QTreeView, QFileIconProvider
from PySide2.QtCore import QDir

from custom_items.empty_icon_provider import EmptyIconProvider
from custom_items.tree_view_model import TreeViewModelItem
from custom_items.directory_tree_item import DirectoryTreeItem
from utilities.system_manager import SystemManager

class TreeView(QTreeView):

    def __init__(self,parent = None):
        super(TreeView, self).__init__(parent)
        self.model = TreeViewModelItem(self)
        self.setModel(self.model)              

        self.__initialise()

        # Populate data
        #self.__populateData()


    # PRIVATE METHODS

    def __initialise(self):
        self.setUniformRowHeights(True)
        self.setHeaderHidden(True)     

        columnCount = self.header().count()

        # Hiding every column excepting the first (name) 
        for index in range (1, columnCount):
            self.hideColumn(index)


    def __populateData(self):
        tree = SystemManager.get_system_tree_structure()
        length = len(tree.roots)

        for index in range(length):
            root = tree.roots[index]
            parent = DirectoryTreeItem(root.directory)
            size = len(root.children)

            for index in range(size):
                child = DirectoryTreeItem(root.children[index].directory)
                parent.appendRow(child)

            self.model.appendRow(parent)


        

    

    
