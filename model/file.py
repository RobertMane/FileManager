from file_system_element import FileSystemElement

class File(FileSystemElement):
    def __init__(self, extension):
        self._extension = extension

    # THE EXTENSION OF THE FILE
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value