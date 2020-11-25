import os
import sys
import psutil

class SystemManager:

    @staticmethod
    def get_system_tree_structure():
        
        return SystemManager.get_drives()



    @staticmethod
    def get_drives():
        diskPartitions = psutil.disk_partitions()
        drives = list()

        for partition in diskPartitions:
            drives.append(partition.device)

        return drives

    @staticmethod
    def get_user_directories():
        DOT ='.'

        home = os.path.expanduser('~')
        homeDirectoryContents = os.listdir(home)

        # Add only directories from user folder
        directories = list()

        # Filtering the files so only the ones without dot as first character will be added
        for item in homeDirectoryContents:
            if(item[0] != DOT):
                path = os.path.join(home, item)

        # Adding only directories
                if os.path.isdir(path):
                    directories.append(item)

        return directories
        
