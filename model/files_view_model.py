from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2.QtCore import Qt, Slot

from custom_ui_items.file_item import FileItem
from custom_ui_items.directory_item import DirectoryItem

from system_elements.file import File
from system_elements.directory import Directory


class FilesViewModel(QStandardItemModel):

    # CONSTANTS
    NAME = "Name"
    DATE_MODIFIED = "Date modified"
    SIZE = "Size"
    TYPE = "Type"

    FOLDER = "File folder"

    FILE_ICON_PATH = "resources/file_icon.png"
    FOLDER_ICON_PATH = "resources/folder_icon.png"

    ZIP_ICON_PATH = "resources/zip_icon.png"
    ZIP_EXTENSION = ".zip"
    RAR_EXTENSION = ".rar"

    def __init__(self, widgetModel, widgetController, mainWidget, parent = None):
        super(FilesViewModel, self).__init__(parent)
        
        self.setHorizontalHeaderItem(0, QStandardItem(self.NAME))
        self.setHorizontalHeaderItem(1, QStandardItem(self.DATE_MODIFIED))
        self.setHorizontalHeaderItem(2, QStandardItem(self.SIZE))
        self.setHorizontalHeaderItem(3, QStandardItem(self.TYPE))

        self._parent = parent

        self._mainWidget = mainWidget
        
        self._widgetModel = widgetModel
        self._widgetController = widgetController

        self.itemChanged.connect(self._widgetController.change_files_list_selections)

        self._widgetModel.selected_items_added.connect(self.on_files_list_check_add)
        self._widgetModel.selected_items_removed.connect(self.on_files_list_check_removal)


        self.populateList()

    
    @Slot(QStandardItem)
    def on_files_list_check_add(self, item):
        if item.checkState() == Qt.Checked:
            self._mainWidget.appendToSelectedItems(item)

    @Slot(QStandardItem)
    def on_files_list_check_removal(self, item):
        if item.checkState() == Qt.Unchecked:
            self._mainWidget.removeFromSelectedItems(item)


    def populateList(self):

        items = self._widgetModel.elements_list
        self.setRowCount(0)

        for index in range(len(items)):
            element = items[index]

            if isinstance(element, File):
                item = FileItem(element)
                self.__appendFileItem(index, item)

            else:
                item = DirectoryItem(element)
                self.__appendDirectoryItem(index, item)


    def __appendDirectoryItem(self, row, directoryItem):

        name = directoryItem
        name.setIcon(QIcon(self.FOLDER_ICON_PATH))
        name.setCheckable(True)
        name.setTextAlignment(Qt.AlignCenter)
        name.setFlags(name.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 0, name)

        creation_time = QStandardItem(directoryItem.getDirectoryCreationTime())
        creation_time.setTextAlignment(Qt.AlignCenter)
        creation_time.setFlags(creation_time.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 1, creation_time)

        size = QStandardItem(directoryItem.getDirectorySize())
        size.setTextAlignment(Qt.AlignCenter)
        size.setFlags(size.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 2, size)

        extension = QStandardItem(self.FOLDER)
        extension.setTextAlignment(Qt.AlignCenter)
        extension.setFlags(extension.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 3, extension)


    def __appendFileItem(self, row, fileItem):

        name = fileItem

        if fileItem.getFileExtension() == self.ZIP_EXTENSION or fileItem.getFileExtension() == self.RAR_EXTENSION :

            fileItem.setIcon(QIcon(self.ZIP_ICON_PATH))
            name.setCheckable(True)
            name.setTextAlignment(Qt.AlignCenter)
            name.setFlags(name.flags() &  ~Qt.ItemIsEditable)
            self.setItem(row, 0, name)

        else:

            fileItem.setIcon(QIcon(self.FILE_ICON_PATH))
            name.setCheckable(True)
            name.setTextAlignment(Qt.AlignCenter)
            name.setFlags(name.flags() &  ~Qt.ItemIsEditable)
            self.setItem(row, 0, name)

        creation_time = QStandardItem(fileItem.getFileCreationTime())
        creation_time.setTextAlignment(Qt.AlignCenter)
        creation_time.setFlags(creation_time.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 1, creation_time)

        size = QStandardItem(fileItem.getFileSize())
        size.setTextAlignment(Qt.AlignCenter)
        size.setFlags(size.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 2, size)

        extension = QStandardItem(fileItem.getFileExtension())
        extension.setTextAlignment(Qt.AlignCenter)
        extension.setFlags(extension.flags() &  ~Qt.ItemIsEditable)
        self.setItem(row, 3, extension)


        



        