import os
import sys
import psutil

from utilities.node import Node
from utilities.directories_tree import DirectoriesTree
from system_elements.directory import Directory

class SystemManager:


    # CONSTANTS
    DOT_SIGN = '.'
    DOLLAR_SIGN = '$'


    @staticmethod
    def get_system_tree_structure():
        
        tree = DirectoriesTree()
        roots = list()
        
        # Getting the system drives
        drives = SystemManager.get_drives()

        # Creating nodes for roots of system tree structure
        # by adding the drives
        for drive in drives:
            # The name is the same as the path in case of drives
            directory = Directory(drive, drive)
            # Creating new node from the directory and adding it to the roots list
            node = Node(directory)
            roots.append(node)

        # Generating the underlying directory hierarchy of the roots
        for root in roots:
            root.add_all_subelements()
        
        # Adding roots with their underlying folder hierarchy to the tree
        for root in roots:
            tree.roots.append(root)
        

        return tree



    @staticmethod
    def get_drives():
        diskPartitions = psutil.disk_partitions()
        drives = list()

        for partition in diskPartitions:
            drives.append(partition.device)

        return drives

    @staticmethod
    def get_user_directories():
        

        home = os.path.expanduser('~')
        homeDirectoryContents = os.listdir(home)

        # Add only directories from user folder
        directories = list()

        # Filtering the files so only the ones without dot as first character will be added
        for item in homeDirectoryContents:
            if((item[0] != SystemManager.DOT_SIGN) and (item[0] != SystemManager.DOLLAR_SIGN)):
                path = os.path.join(home, item)

        # Adding only directories
                if os.path.isdir(path):
                    directories.append(item)

        return directories

    

        
