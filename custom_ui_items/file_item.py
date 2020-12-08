from PySide2.QtGui import QStandardItem
from PySide2.QtCore import Qt


class FileItem(QStandardItem):
    def __init__(self, file):
        super(FileItem, self).__init__(file.name)

        self.setFlags(self.flags() & ~ Qt.ItemIsEditable)

        self._file = file

    @property
    def file(self):
        return self._file
    
    @file.setter
    def file(self, value):
        self._file = value

    def getFileName(self):
        return self._file.name

    def getFilePath(self):
        return self._file.path

    def getFileCreationTime(self):
        return self._file.creation_time

    def getFileSize(self):
        return self._file.size_as_string

    def getFileExtension(self):
        return self._file.extension