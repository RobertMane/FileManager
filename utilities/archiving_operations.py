from zipfile import ZipFile
import os
import shutil

class ArchivingOperations:

    # CONSTANTS
    READ_MODE = "r"
    WRITE_MODE = "w"
    ZIP_FILE_TYPE = "zip"


    # FILE ZIPPING / UNZIPPING OPERATIONS

    @staticmethod
    def zipFile(filePath, resultedZipPath):

        zip_file = ZipFile(resultedZipPath, ArchivingOperations.WRITE_MODE)
        zip_file.write(filePath, basename(filePath))
        zip_file.close()


    @staticmethod
    def unzipFile(zipFilePath, targetDirectory):

        with ZipFile(zipFilePath, ArchivingOperations.READ_MODE) as zip_file:
            zip_file.extractall(targetDirectory)


    # DIRECTORY ZIPPING / UNZIPPING OPERATIONS

    @staticmethod 
    def zipDirectory(directoryPath, resultedZipPath):

        currentDirectory = os.path.basename(os.path.normpath(directoryPath))
        path = os.path.dirname(directoryPath)
        shutil.make_archive(resultedZipPath, ArchivingOperations.ZIP_FILE_TYPE, path, currentDirectory)


    @staticmethod
    def unzipDirectory(zipFilePath, targetDirectory):

        with ZipFile(zipFilePath, ArchivingOperations.READ_MODE) as zip_file:
            zip_file.extractall(targetDirectory)
