from system_elements.file_system_element import FileSystemElement
import os, stat
from system_elements.file import File

class Directory(FileSystemElement):
    
    # CONSTANTS
    DOT_SIGN = '.'
    DOLLAR_SIGN = '$'

    def __init__(self, name, path):
        super(Directory, self).__init__(name, path)
        self._is_file = False

    @staticmethod
    def get_all_subdirectories(directoryPath):
        directoryContents = os.listdir(directoryPath)
        subdirectories = list()

        for name in directoryContents:
            if (name[0] != Directory.DOT_SIGN and name[0]!= Directory.DOLLAR_SIGN):
                path = os.path.join(directoryPath, name)

                if os.path.isdir(path):
                    directory = Directory(name, path)
                    subdirectories.append(directory)
        
        return subdirectories

    @staticmethod
    def get_all_subfiles(directoryPath):
        directoryContents = os.listdir(directoryPath)
        subfiles = list()

        for name in directoryContents:
            if (name[0] != Directory.DOT_SIGN and name[0]!= Directory.DOLLAR_SIGN):
                path = os.path.join(directoryPath, name)

                if os.path.isfile(path):
                    file = File(name, path)
                    subfiles.append(file)
        
        return subfiles