from system_elements.file_system_element import FileSystemElement
from utilities.system_elements_basic_operations import SystemElementsBasicOperations

class File(FileSystemElement):
    def __init__(self, name, path):
        super(File, self).__init__(name, path)
        self._extension = SystemElementsBasicOperations.getElementExtension(self._path)
        self._is_file = True

    # THE EXTENSION OF THE FILE
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value