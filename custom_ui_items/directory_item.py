from PySide2.QtGui import QStandardItem
from PySide2.QtCore import Qt


class DirectoryItem(QStandardItem):
    def __init__(self, directory):
        super(DirectoryItem, self).__init__(directory.name)

        self.setFlags(self.flags() & ~ Qt.ItemIsEditable)

        self._directory = directory

    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, value):
        self._directory = value

    def getDirectoryName(self):
        return self._directory.name

    def getDirectoryPath(self):
        return self._directory.path

    def getDirectoryCreationTime(self):
        return self._directory.creation_time

    def getDirectorySize(self):
        return self._directory.size