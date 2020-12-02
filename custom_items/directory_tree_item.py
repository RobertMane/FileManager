from PySide2.QtGui import QStandardItem

class DirectoryTreeItem(QStandardItem):
    def __init__(self, directory):
        super(DirectoryTreeItem, self).__init__()
        self._directory = directory
        self.setText(directory.name)
        self.setEditable(False)


    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self._directory = value