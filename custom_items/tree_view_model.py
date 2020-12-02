from PySide2.QtWidgets import QFileSystemModel
from PySide2.QtCore import QDir

from custom_items.empty_icon_provider import EmptyIconProvider

class TreeViewModelItem(QFileSystemModel):

    def __init__(self, tree):
        super(TreeViewModelItem, self).__init__()
        self.__tree = tree
        self.__current = tree
        self.__view = None

        self.setRootPath(QDir.currentPath())
        self.setIconProvider(EmptyIconProvider())
        self.setFilter(QDir.NoDotAndDotDot | QDir.Dirs)
      
   