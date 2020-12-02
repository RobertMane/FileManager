from utilities.system_elements_basic_operations import SystemElementsBasicOperations
from system_elements.directory import Directory
import os

class Node:

    def __init__(self, directory):
        self._directory = directory
        self._children = list()

    def add_child(self, child):
        self._children.append(child)

    def add_all_subelements(self):
        subdirectories = Directory.get_all_subdirectories(self._directory.path)
        for subdirectory in subdirectories:
            child = Node(subdirectory)
            self.add_child(child)
    
    def add_all_subelements_rec(self, root):
        for root, dirs, files in os.walk(root):
            for path in dirs:
                if os.path.isdir(path) == True :
                    directory  = Directory(path, path)
                    child = Node(directory)
                    self.add_child(child)
                    self.add_all_subelements_rec(child.directory.path)
        
            

        



    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, value):
        self._directory = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value