from PySide2.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide2.QtGui import QStandardItemModel

class TreeViewModelItem(QStandardItemModel):

    def __init__(self, tree):
        super(TreeViewModelItem, self).__init__()
        self.__tree = tree
        self.__current = tree
        self.__view = None
      
    """
    def  flags(self, index):
        flag = Qt.ItemIsEnabled
        if index.isValid():
            flag |= Qt.ItemIsSelectable

        return flag

    def index(self, row, column, parent=QModelIndex()):
        node = QModelIndex()
        if parent.isValid():
            parentPointer = parent.internalPointer()
            childPointer = parentPointer.child[row]
            node = self.__createIndex(row, column, childPointer)
        else:
            node = self.__createIndex(row, column, self.__tree)
        return node   

    def parent(self, index):
        node = QModelIndex()
        if index.isValid():
            internalPointer = index.internalPointer()
            parent = internalPointer.parent
            if parent is not None:
                node = self.__createIndex(parent.position(), 0, parent)
        return node

    def rowCount(self, index = QModelIndex()):
        count = 1
        node = index.internalPointer()
        if node is not None:
            count = len(node.child)
        return count

    def columnCount(self, index = QModelIndex()):
        return 1

    def data(self, index, role = Qt.DisplayRole):
        data = None
        return data

    def setView(self, view):
        self.__view = view

    def __createIndex(self, row, column, node):
        if node.index == None:
            index = self.createIndex(row, column, node)
            node.index = index
        if node.widget is None:
            node.widget = FileSystemWidget(node)
            self.__view.setIndexWidget(index, node.widget) 

        return node.index   
        """