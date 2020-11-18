from shutil import copy2
from shutil import move
from shutil import rmtree
import os

class SystemElementsBasicOperations:

    # CONSTANTS
    READ_WRITE_MODE = "w+"

   
    # COPYING FILE / DIRECTORY METHODS
    @staticmethod
    def copyFile(source, destinationFolder, fileName):  

        destination = os.path.join(destinationFolder, fileName)
        copy2(source, destination)

    # MOVING FILE / DIRECTORY METHODS
    @staticmethod
    def moveFile(source, destinationFolder, fileName):

        destination = os.path.join(destinationFolder, fileName) 
        move(source, destination)


    # CHECK FILE / DIRECTORY EXISTENCE
    @staticmethod
    def existsSystemElement(path):
        if os.path.exists(path):
            return True
        else:
            return False

    
    # FILE / DIRECTORY CREATION METHODS
    @staticmethod
    def createFile(currentPath, fileName):

        path = os.path.join(currentPath, fileName)
        file = open(path, SystemElementsBasicOperations.READ_WRITE_MODE)
        file.close()


    @staticmethod
    def createDirectory(path, directoryName):

        directory = os.path.join(path, directoryName)
        os.mkdir(directory)


    # FILE / DIRECTORY REMOVING METHODS
    @staticmethod
    def removeFile(filePath):
        os.remove(filePath)

    @staticmethod
    def removeDirectory(directoryPath):
        rmtree(directoryPath)
    


