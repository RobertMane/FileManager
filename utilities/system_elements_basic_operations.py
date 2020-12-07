from shutil import copy2
from shutil import move
from shutil import rmtree
import os
from datetime import datetime

class SystemElementsBasicOperations:

    # CONSTANTS

    # Read mode
    READ_WRITE_MODE = "w+"

    # Empty space
    EMPTY_SPACE = " "

    # Creation date format
    CREATION_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    # Memory measurement units
    SCALE_COEFFICIENT = 1024
    BYTE = "B"
    KILOBYTE = "kB"
    MEGABYTE = "MB"
    GIGABYTE = "GB"

    # Directory extension
    DIRECTORY_EXTENSION = ""

   
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


    # METHOD TO GET THE CREATION TIME OF THE FILE WITH SPECIFIED PATH
    @staticmethod
    def getElementCreationTime(path):
        creationDate = os.path.getctime(path)
        creationDateAsString = datetime.fromtimestamp(creationDate).strftime(SystemElementsBasicOperations.CREATION_DATE_FORMAT)

        return creationDateAsString

    # METHOD TO GET THE SIZE OF THE FILE WITH SPECIFIED PATH, MEASURED IN BYTES
    @staticmethod
    def getElementSize(path):
        return os.path.getsize(path)

    # METHOD TO GET THE SIZE OF THE FILE WITH SPECIFIED PATH AS A STRING, MEASURED IN BYTES
    # THE METHOD WILL CONVERT THE SIZE TO A HIGHER SCALE, IF IT IS THE CASE
    @staticmethod
    def getElementSizeAsString(path):

        size = os.path.getsize(path)

        scale_coefficient = SystemElementsBasicOperations.SCALE_COEFFICIENT

        byte_kilobyte_difference = scale_coefficient
        byte_megabyte_difference = scale_coefficient * scale_coefficient
        byte_gigabyte_difference = scale_coefficient * scale_coefficient * scale_coefficient

        # Case of kilobytes
        if ((size > byte_kilobyte_difference) and (size < byte_megabyte_difference)):
            size = size / byte_kilobyte_difference
            sizeAsString = str(size) + SystemElementsBasicOperations.EMPTY_SPACE + SystemElementsBasicOperations.KILOBYTE
            return sizeAsString

        # Case of megabytes
        elif ((size > byte_megabyte_difference) and (size < byte_gigabyte_difference)):
            size = size / byte_megabyte_difference
            sizeAsString = str(size) + SystemElementsBasicOperations.EMPTY_SPACE + SystemElementsBasicOperations.MEGABYTE
            return sizeAsString

        # Case of gigabytes
        elif (size > byte_gigabyte_difference):
            size = size / byte_gigabyte_difference
            sizeAsString = str(size) + SystemElementsBasicOperations.EMPTY_SPACE + SystemElementsBasicOperations.GIGABYTE
            return sizeAsString

        # Case of bytes
        else:
            sizeAsString = str(size) + SystemElementsBasicOperations.EMPTY_SPACE + SystemElementsBasicOperations.BYTE
            return sizeAsString
            
    # Method which gets the extension of a system element
    # It returns an empty string if the element is a directory
    @staticmethod
    def getElementExtension(path):
        if os.path.isfile(path):
            fileName, extension = os.path.splitext(path)
            return extension

        else:
            return SystemElementsBasicOperations.DIRECTORY_EXTENSION

    @staticmethod
    def getNameWithoutExtension(name):
        fileName, extension = os.path.splitext(name)

        return name


