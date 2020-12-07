from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt

from custom_items.file_item import FileItem
from custom_items.directory_item import DirectoryItem

from system_elements.file import File
from system_elements.directory import Directory


class FilesViewModel(QStandardItemModel):

    # CONSTANTS
    NAME = "Name"
    DATE_MODIFIED = "Date modified"
    SIZE = "Size"
    TYPE = "Type"

    FOLDER = "File folder"

    def __init__(self, widgetModel, parent = None):
        super(FilesViewModel, self).__init__(parent)
        
        self.setHorizontalHeaderItem(0, QStandardItem(self.NAME))
        self.setHorizontalHeaderItem(1, QStandardItem(self.DATE_MODIFIED))
        self.setHorizontalHeaderItem(2, QStandardItem(self.SIZE))
        self.setHorizontalHeaderItem(3, QStandardItem(self.TYPE))

        self._widgetModel = widgetModel
        self.populateList()

    def populateList(self):

        items = self._widgetModel.elements_list

        for index in range(len(items)):
            element = items[index]

            if isinstance(element, File):
                item = FileItem(element)
                self.__appendFileItem(index, item)

            else:
                item = DirectoryItem(element)
                self.__appendDirectoryItem(index, item)



    def __appendDirectoryItem(self, row, directoryItem):

        name = QStandardItem(directoryItem.getDirectoryName())
        name.setCheckable(True)
        name.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 0, name)

        creation_time = QStandardItem(directoryItem.getDirectoryCreationTime())
        creation_time.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 1, creation_time)

        size = QStandardItem(directoryItem.getDirectorySize())
        size.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 2, size)

        extension = QStandardItem(self.FOLDER)
        extension.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 3, extension)


    def __appendFileItem(self, row, fileItem):

        name = QStandardItem(fileItem.getFileName())
        name.setCheckable(True)
        name.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 0, name)

        creation_time = QStandardItem(fileItem.getFileCreationTime())
        creation_time.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 1, creation_time)

        size = QStandardItem(fileItem.getFileSize())
        size.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 2, size)

        extension = QStandardItem(fileItem.getFileExtension())
        extension.setTextAlignment(Qt.AlignCenter)
        self.setItem(row, 3, extension)


        



        