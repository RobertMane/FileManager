from PySide2.QtWidgets import QMainWindow, QAction, QListWidget
from PySide2.QtGui import QIcon

from model.operations_widget_model import OperationsWidgetModel
from controllers.operations_widget_ctrl import OperationsWidgetController
from views.operations_widget import MainWidget

from utilities.system_elements_basic_operations import SystemElementsBasicOperations
from utilities.archiving_operations import ArchivingOperations



class Window(QMainWindow):
    
    # CONSTANTS

    # App name
    APP_NAME = "File Manager"

    # Menu names
    FILE_MENU_NAME = "File"

    # Actions names
    COPY_ACTION_NAME = "Copy"
    MOVE_ACTION_NAME = "Move"
    CREATE_FILE_ACTION_NAME = "Create new file"
    CREATE_DIRECTORY_ACTION_NAME = "Create new directory"
    ARCHIVE_ACTION_NAME = "Archive"
    UNARCHIVE_ACTION_NAME = "Unarchive"
    DELETE_ACTION_NAME = "Delete"
    RENAME_ACTION_NAME = "Rename"

    # Icons paths
    APP_ICON_PATH = 'resources/app_icon.png'

    COPY_ICON_PATH = 'resources/copy_icon.png'
    MOVE_ICON_PATH = 'resources/move_icon.png'
    CREATE_FILE_ICON_PATH = 'resources/create_file_icon.png'
    CREATE_DIRECTORY_ICON_PATH = 'resources/create_directory_icon.png'
    ARCHIVE_ICON_PATH = 'resources/archive_icon.png'
    UNARCHIVE_ICON_PATH = 'resources/unarchive_icon.png'
    DELETE_ICON_PATH = 'resources/delete_icon.png'
    RENAME_ICON_PATH = 'resources/rename_icon.png'

    # Styles file name
    STYLES_FILE_NAME = "style.qss"

    # Reading mode
    READING_MODE = "r"

    WIDTH = 1440
    HEIGHT = 900

    
    def __init__(self, model, controller, parent = None):
        
        super(Window, self).__init__(parent)

        self.setWindowTitle(self.APP_NAME)
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        self.setWindowIcon(QIcon(self.APP_ICON_PATH))
        
        # Open the file containing the styles for graphic elements
        stylesheetFile = self.STYLES_FILE_NAME
        with open(stylesheetFile,self.READING_MODE) as f:
            self.setStyleSheet(f.read())

        self.create_menus()

        # MAIN WIDGET CREATION
        self.main_widget = MainWidget(self, model, controller)
        self.main_widget.move(0,50)
        self.main_widget.setFixedSize(self.WIDTH,self.HEIGHT)


    # Method which creates all menus
    def create_menus(self):
        self.create_file_menu()

    # Method which creates the file menu with its submenus
    def create_file_menu(self):
        mainMenu = self.menuBar()

        # File menu
        fileMenu = mainMenu.addMenu(self.FILE_MENU_NAME)

        # Creating actions for the file management menu
        copyAction = QAction(QIcon(self.COPY_ICON_PATH),self.COPY_ACTION_NAME,self)
        moveAction = QAction(QIcon(self.MOVE_ICON_PATH),self.MOVE_ACTION_NAME,self)
        createNewFileAction = QAction(QIcon(self.CREATE_FILE_ICON_PATH),self.CREATE_FILE_ACTION_NAME,self)
        createNewDirectoryAction = QAction(QIcon(self.CREATE_DIRECTORY_ICON_PATH),self.CREATE_DIRECTORY_ACTION_NAME,self)
        archiveAction = QAction(QIcon(self.ARCHIVE_ICON_PATH),self.ARCHIVE_ACTION_NAME,self)
        unarchiveAction = QAction(QIcon(self.UNARCHIVE_ICON_PATH),self.UNARCHIVE_ACTION_NAME,self)
        deleteAction = QAction(QIcon(self.DELETE_ICON_PATH),self.DELETE_ACTION_NAME,self)
        renameAction = QAction(QIcon(self.RENAME_ICON_PATH),self.RENAME_ACTION_NAME,self)

        # Adding actions to the file management menu
        fileMenu.addAction(copyAction)
        fileMenu.addAction(moveAction)
        fileMenu.addAction(createNewFileAction)
        fileMenu.addAction(createNewDirectoryAction)
        fileMenu.addAction(archiveAction)
        fileMenu.addAction(unarchiveAction)
        fileMenu.addAction(deleteAction)
        fileMenu.addAction(renameAction)


        # Adding actions for the menu items
        copyAction.triggered.connect(self.copy)
        moveAction.triggered.connect(self.move)
        createNewFileAction.triggered.connect(self.createNewFile)
        createNewDirectoryAction.triggered.connect(self.createNewDirectory)
        archiveAction.triggered.connect(self.archive)
        unarchiveAction.triggered.connect(self.unarchive)
        deleteAction.triggered.connect(self.delete)
        renameAction.triggered.connect(self.rename)


    # ========================     FILE MENU METHODS     =================================

    # Method which is executed when we press Copy menu button
    def copy(self):

        self.main_widget.doCopy()
        """
        source = "C:\Robert\TEST_FILE_MANAGER\\textfile.txt"
        destinationFolder = "C:\Robert\TEST_FILE_MANAGER\\Directory"
        fileName  = "textfile.txt"

        SystemElementsBasicOperations.copyFile(source, destinationFolder, fileName)
        """

    # Method which is executed when we press Move menu button
    def move(self):

        self.main_widget.doMove()

        """
        source = "C:\Robert\TEST_FILE_MANAGER\\textfile.txt"
        destinationFolder = "C:\Robert\TEST_FILE_MANAGER\\Directory"
        fileName  = "textfile.txt"

        SystemElementsBasicOperations.moveFile(source, destinationFolder, fileName)
        """

    # Method which is executed when we press Create new file menu button
    def createNewFile(self):
        
        self.main_widget.doCreateFile()

        #SystemElementsBasicOperations.createFile("C:\Robert\TEST_FILE_MANAGER", "file.txt")

    # Method which is executed when we press Create new directory menu button
    def createNewDirectory(self):
        
        self.main_widget.doCreateFolder()
        # SystemElementsBasicOperations.createDirectory("C:\Robert\TEST_FILE_MANAGER", "Directory")

    # Method which is executed when we press Archive menu button
    def archive(self):
        
        self.main_widget.doArchive()
        # ArchivingOperations.zipFile("C:\Robert\TEST_FILE_MANAGER\\textfile.txt", "C:\Robert\TEST_FILE_MANAGER\\test.zip")

        # ArchivingOperations.zipDirectory("C:\Robert\TEST_FILE_MANAGER\Directory", "C:\Robert\TEST_FILE_MANAGER\\test")

    # Method which is executed when we press Unarchive menu button
    def unarchive(self):

        self.main_widget.doUnarchive()

        # ArchivingOperations.unzipFile("C:\Robert\TEST_FILE_MANAGER\\test.zip", "C:\Robert\TEST_FILE_MANAGER\Directory")

    # Method which is executed when we press Delete menu button
    def delete(self):

        self.main_widget.doDelete()

       # SystemElementsBasicOperations.removeFile("C:\Robert\TEST_FILE_MANAGER\\file.txt")
       # SystemElementsBasicOperations.removeDirectory("C:\Robert\TEST_FILE_MANAGER\Directory")

    def rename(self):

        self.main_widget.doRename()
       
