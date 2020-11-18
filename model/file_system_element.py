
class FileSystemElement:

    def __init__(self, name, path):
        self._name = name
        self._path = path

    # NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # PATH
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = path

    # CREATION DATE
    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter(self, value)
    def creation_date(self, value):
        self._creation_date = value

    # SIZE
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size

    # SIZE AS STRING
    @property
    def size_as_string(self):
        return self._size_as_string

    @size_as_string.setter
    def size_as_string(self, value):
        self._size_as_string

    # IS FILE
    @property
    def is_file(self):
        return self._is_file
    
    @is_file.setter:
    def is_file(self, value):
        self._is_file = value
