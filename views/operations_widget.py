from PySide2.QtWidgets import QWidget, QPushButton, QComboBox, QListWidget, QLabel, QListWidgetItem, QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtCore import QDir, QSize, Slot, QPropertyAnimation, QRect
from PySide2 import QtCore
import os


from model.tree_view_model import TreeViewModelItem
from views.tree_view import TreeView
from views.files_view import FilesListView

from custom_ui_items.operations_widget_button import OperationsWidgetButton
from custom_ui_items.toggle_menu_button import ToggleMenuButton
from custom_ui_items.list_widget_item import ListWidgetItem

from system_elements.directory import Directory



class MainWidget(QWidget):

    # CONSTANTS
    EMPTY_STRING = ""
    
    # TOGGLE BUTTON CONSTANTS
    BUTTON_CLOSED_ICON_PATH = 'resources/menu_closed_button_icon.png'
    BUTTON_OPENED_ICON_PATH = 'resources/menu_opened_button_icon.png'


    TOOGLE_BUTTON_CSS_PROPERTY = "QPushButton {background-color: rgb(1,150,250); border:  none ; qproperty-iconSize: 80px}"
    CURRENT_PATH_LINE_EDIT_PROPERTY = "QLineEdit {background-color: rgba(240, 240, 240, 1);}"


    TOOGLE_CLOSED_COLOR = "background-color: rgb(1,150,250);"
    TOOGLE_OPENED_COLOR = "background-color: rgba(44, 53, 57, 0.2);"

    WHITE = "background-color: rgb(255, 255, 255);"
    
    FRAME_BUTTON_STYLE = "background-color: rgb(0, 191, 255); color: rgb(255, 255, 255);"
    FRAME_LINE_EDIT_STYLE = "background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);"
    FRAME_LABEL_STYLE = "QLabel { background-color : rgba(44, 53, 57, 0); }"


    SEARCH_ICON_STYLE = "QPushButton {background-color: rgb(1,150,250);}"
    BACK_ICON_STYLE = "QPushButton {background-color: rgb(1,150,250);} QPushButton:pressed {background-color: rgb(40,170,250);}"


    WIDTH = 1440
    HEIGHT = 900

    # Size of the operations widget buttons
    OPERATION_BUTTON_WIDTH = 40
    OPERATION_BUTTON_HEIGHT = 40

    FILES_LIST_VIEW_WIDTH = 820
    FILES_LIST_VIEW_HEIGHT = 680

    TOGGLE_BUTTON_ANIMATION_DURATION = 200
    RIGHT_MENU_ANIMATION_DURATION = 250

    # ICONS PATHS

    # Actions icons
    ADD_FILE_ICON_PATH = "resources/add_file_icon.png"
    ADD_DIRECTORY_ICON_PATH = "resources/add_directory_icon.png"
    COPY_ELEMENT_ICON_PATH = "resources/copy_element_icon.png"
    MOVE_ELEMENT_ICON_PATH = "resources/move_element_icon.png"
    DELETE_ELEMENT_ICON_PATH = "resources/delete_element_icon.png"
    SEARCH_ICON_PATH = "resources/search_icon_white.png"
    CREATE_ARCHIVE_ICON_PATH = "resources/create_archive_icon.png"
    UNARCHIVE_FILE_ICON_PATH = "resources/unarchive_file_icon.png"
    RENAME_ELEMENT_ICON_PATH = "resources/rename_icon_white.png"
    BACK_ICON_PATH = "resources/back_icon.png"

    # Elements icons
    FILE_ICON_PATH = "resources/file_icon.png"
    FOLDER_ICON_PATH = "resources/folder_icon.png"
    ZIP_ICON_PATH = "resources/zip_icon.png"

    # Tooltips
    COPY_TOOLTIP = "Copy files / folders"
    MOVE_TOOLTIP = "Move files / folders"
    DELETE_TOOLTIP = "Delete files / folders"
    ARCHIVE_TOOLTIP = "Archive files / folders"
    UNARCHIVE_TOOLTIP = "Unarchive files / folders"
    CREATE_FILE_TOOLTIP = "Create a new text file"
    CREATE_DIRECTORY_TOOLTIP = "Create a new folder"
    RENAME_TOOLTIP = "Rename a file / folder"
    BACK_TOOLTIP = "Move up one directory"

    # Buttons name
    COPY = "Copy"
    MOVE = "Move"
    DELETE = "Delete"
    ARCHIVE = "Archive"
    UNARCHIVE = "Unarchive"
    RENAME = "Rename"
    CREATE_FILE = "Create file"
    CREATE_FOLDER = "Create folder"


    # Labels
    SELECTED_ITEMS_TEXT = "Selected items:"
    ARCHIVE_NAME_TEXT = "Archive name:"
    CREATE_FILE_NAME_TEXT = "File name:"
    CREATE_FOLDER_NAME_TEXT = "Folder name:"
    RENAME_ELEMENT_TEXT = "New name:"


    def __init__(self, parent, model, controller):        
        super(MainWidget, self).__init__(parent)
        
        self._model = model
        self._controller = controller
        
        # FILES LIST VIEW
        
        self.filesListView = FilesListView(self.FILES_LIST_VIEW_WIDTH, self.FILES_LIST_VIEW_HEIGHT, self._model, self._controller, self)
        self.filesListView.move(230,120)



        # TREE VIEW FOR SYSTEM DIRECTORY HIERARCHY
        self.treeView = TreeView(self._model, self._controller, self)
        self.treeView.setFixedSize(200,820)
        self.treeView.move(0,60)



        # DISC SELECTION COMBO BOX
        self.discSelectionComboBox = QComboBox(self)
        self.discSelectionComboBox.setFixedSize(100,30)
        self.discSelectionComboBox.move(230,60)
        self.discSelectionComboBox.addItems(self._model.combo_box_list)
        
        # CONNECT WIDGETS TO CONTROLLER
        self.discSelectionComboBox.currentTextChanged.connect(self._controller.change_combo_box_selection)


        # LISTEN FOR MODEL EVENT SIGNALS
        self._model.combo_box_selection_changed.connect(self.on_combo_box_selection_changed)

        
        self.frameRightMenu = QWidget(self)
        self.frameRightMenu.setFixedSize(360,self.HEIGHT)
        self.frameRightMenu.move(1450,15)
        self.frameRightMenu.setStyleSheet(self.TOOGLE_CLOSED_COLOR)


        # BUTTON WHICH TOOGLE ON/OFF THE TREE VIEW CONTAINING THE SELECTED ITEMS TREE VIEW
        self.toggleButton = QPushButton(QIcon(self.BUTTON_CLOSED_ICON_PATH), self.EMPTY_STRING, self)
        self.toggleButton.setFixedSize(100,70)
        self.toggleButton.move(1300,0)
        self.toggleButton.setStyleSheet(self.TOOGLE_BUTTON_CSS_PROPERTY)

        self._enable = True

        self.toggleButton.clicked.connect(lambda: Animations.toggleMenu(self, self._enable))

        # Label that shows "Selected items:"
        self.selectedItemsLabel = QLabel(self.SELECTED_ITEMS_TEXT, self.frameRightMenu)
        self.selectedItemsLabel.move(100, 20)
        self.selectedItemsLabel.setStyleSheet(self.FRAME_LABEL_STYLE)

        # The list with selected elements from FilesListView
        self.selectedFilesListWidget = QListWidget(self.frameRightMenu)
        self.selectedFilesListWidget.setFixedSize(320,500)
        self.selectedFilesListWidget.move(23,60)
        self.selectedFilesListWidget.setStyleSheet(self.WHITE)

        # ACTIONS BUTTONS

        # Copy button
        self.copyElementButton = OperationsWidgetButton(QIcon(self.COPY_ELEMENT_ICON_PATH), self.EMPTY_STRING, self)
        self.copyElementButton.clicked.connect(self.doCopy)
        self.copyElementButton.move(230,0)
        self.copyElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.copyElementButton.setToolTip(self.COPY_TOOLTIP)

        # Move button
        self.moveElementButton = OperationsWidgetButton(QIcon(self.MOVE_ELEMENT_ICON_PATH), self.EMPTY_STRING, self)
        self.moveElementButton.clicked.connect(self.doMove)
        self.moveElementButton.move(290,0)
        self.moveElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.moveElementButton.setToolTip(self.MOVE_TOOLTIP)

        # Delete button
        self.deleteElementButton = OperationsWidgetButton(QIcon(self.DELETE_ELEMENT_ICON_PATH), self.EMPTY_STRING, self)
        self.deleteElementButton.clicked.connect(self.doDelete)
        self.deleteElementButton.move(350,0)
        self.deleteElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.deleteElementButton.setToolTip(self.DELETE_TOOLTIP)

        # Archive button
        self.archiveElementButton = OperationsWidgetButton(QIcon(self.CREATE_ARCHIVE_ICON_PATH), self.EMPTY_STRING, self)
        self.archiveElementButton.clicked.connect(self.doArchive)
        self.archiveElementButton.move(410,0)
        self.archiveElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.archiveElementButton.setToolTip(self.ARCHIVE_TOOLTIP)


        # Unarchive button
        self.unarchiveElementButton = OperationsWidgetButton(QIcon(self.UNARCHIVE_FILE_ICON_PATH), self.EMPTY_STRING, self)
        self.unarchiveElementButton.clicked.connect(self.doUnarchive)
        self.unarchiveElementButton.move(470,0)
        self.unarchiveElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.unarchiveElementButton.setToolTip(self.UNARCHIVE_TOOLTIP)


        # Add file button
        self.addFileButton = OperationsWidgetButton(QIcon(self.ADD_FILE_ICON_PATH), self.EMPTY_STRING, self)
        self.addFileButton.clicked.connect(self.doCreateFile)
        self.addFileButton.move(530,0)
        self.addFileButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.addFileButton.setToolTip(self.CREATE_FILE_TOOLTIP)


        # Add directory button
        self.addDirectoryButton = OperationsWidgetButton(QIcon(self.ADD_DIRECTORY_ICON_PATH), self.EMPTY_STRING, self)
        self.addDirectoryButton.clicked.connect(self.doCreateFolder)
        self.addDirectoryButton.move(590,0)
        self.addDirectoryButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.addDirectoryButton.setToolTip(self.CREATE_DIRECTORY_TOOLTIP)

        # Move button
        self.renameElementButton = OperationsWidgetButton(QIcon(self.RENAME_ELEMENT_ICON_PATH), self.EMPTY_STRING, self)
        self.renameElementButton.clicked.connect(self.doRename)
        self.renameElementButton.move(650,0)
        self.renameElementButton.setFixedSize(self.OPERATION_BUTTON_WIDTH, self.OPERATION_BUTTON_HEIGHT)
        self.renameElementButton.setToolTip(self.RENAME_TOOLTIP)


        # Text field needed for displaying the current path
        self.currentPathLineEdit = QLineEdit(self.EMPTY_STRING, self)
        self.currentPathLineEdit.move(350,80)
        self.currentPathLineEdit.setFixedSize(400,27)
        self.currentPathLineEdit.setStyleSheet(self.CURRENT_PATH_LINE_EDIT_PROPERTY)
        self.currentPathLineEdit.setReadOnly(True)
        self.currentPathLineEdit.setText(self._model.current_path)
        self.currentPathLineEdit.textChanged.connect(self._controller.change_current_path_text)

        self._model.current_path_changed.connect(self.on_current_path_changed)

        # Text field needed for searching file / folder by the name
        self.searchLineEdit = QLineEdit(self.EMPTY_STRING, self)
        self.searchLineEdit.move(810,80)
        self.searchLineEdit.setFixedSize(200,27)
        self.searchLineEdit.textChanged.connect(self._controller.change_search_text)

        self._model.current_search_changed.connect(self.on_current_search_changed)

        self.searchIconButton = OperationsWidgetButton(QIcon(self.SEARCH_ICON_PATH), self.EMPTY_STRING, self)
        self.searchIconButton.move(1015,78)
        self.searchIconButton.setFixedSize(30,30)
        self.searchIconButton.setStyleSheet(self.SEARCH_ICON_STYLE)
        self.searchIconButton.setEnabled(False)

        self.backButton = OperationsWidgetButton(QIcon(self.BACK_ICON_PATH), self.EMPTY_STRING, self)
        self.backButton.clicked.connect(self.doBack)
        self.backButton.move(765,80)
        self.backButton.setFixedSize(25,25)
        self.backButton.setStyleSheet(self.BACK_ICON_STYLE)
        self.backButton.setToolTip(self.BACK_TOOLTIP)
        self.backButton.setEnabled(True)

        # ACTIONS LABELS
        self.archiveLabel = QLabel(self.ARCHIVE_NAME_TEXT, self.frameRightMenu)
        self.createFolderLabel = QLabel(self.CREATE_FOLDER_NAME_TEXT, self.frameRightMenu)
        self.createFileLabel = QLabel(self.CREATE_FILE_NAME_TEXT, self.frameRightMenu)
        self.renameElementLabel = QLabel(self.RENAME_ELEMENT_TEXT, self.frameRightMenu)

        # ACTIONS LINE EDITS
        self.archiveNameEditLine = QLineEdit(self.EMPTY_STRING, self.frameRightMenu)
        self.createFileEditLine = QLineEdit(self.EMPTY_STRING, self.frameRightMenu)
        self.createFolderEditLine = QLineEdit(self.EMPTY_STRING, self.frameRightMenu)
        self.renameElementEditLine = QLineEdit(self.EMPTY_STRING, self.frameRightMenu)

        # ACTIONS BUTTONS
        self.copyButton = ToggleMenuButton(self.COPY, self.frameRightMenu)
        self.moveButton = ToggleMenuButton(self.MOVE, self.frameRightMenu)
        self.deleteButton = ToggleMenuButton(self.DELETE, self.frameRightMenu)
        self.archiveButton = ToggleMenuButton(self.ARCHIVE, self.frameRightMenu)
        self.unarchiveButton = ToggleMenuButton(self.UNARCHIVE, self.frameRightMenu)
        self.createFileButton = ToggleMenuButton(self.CREATE_FILE, self.frameRightMenu)
        self.createFolderButton = ToggleMenuButton(self.CREATE_FOLDER, self.frameRightMenu)
        self.renameElementButton = ToggleMenuButton(self.RENAME, self.frameRightMenu)

        self.__createFrameLayoutElements()


    @Slot(str)
    def on_current_path_changed(self, path):
        self._model.elements_list.clear()
        self._model.selected_items.clear()
        self.selectedFilesListWidget.clear()
        self._model.elements_list = Directory.get_all_subelements(path)
        self.filesListView.model().populateList()

    @Slot(str)
    def on_current_search_changed(self, name):
        print(name)


    def removeFromSelectedItems(self, item):
        Animations.toggleMenu(self, True)
        count = self.selectedFilesListWidget.count()
        index = 0

        for i in range(count):
            if item.text() == self.selectedFilesListWidget.item(i).text():
                index = i
                break


        self.selectedFilesListWidget.takeItem(index)


    def appendToSelectedItems(self, item):
        Animations.toggleMenu(self, True)
        listItem = ListWidgetItem(item)
        self.selectedFilesListWidget.insertItem(0, listItem)

    def setCurrentPath(self, path):
        self.currentPathLineEdit.setText(path)
    


    @Slot(str)
    def on_combo_box_selection_changed(self, value):
        index = self.discSelectionComboBox.findText(value)
        self.discSelectionComboBox.setCurrentIndex(index)

    Slot()
    def doBack(self):
        path = self.currentPathLineEdit.text()
        parentPath = os.path.dirname(path)
        self.setCurrentPath(parentPath)

    @Slot()
    def doCopy(self):
        self.__setCopyLayout(True)
        Animations.toggleMenu(self, True)

    @Slot()
    def doMove(self):
        self.__setMoveLayout(True)
        Animations.toggleMenu(self, True)


    @Slot()
    def doDelete(self):
        self.__setDeleteLayout(True)
        Animations.toggleMenu(self, True)
    
    @Slot()
    def doArchive(self):
        self.__setArchiveLayout(True)
        Animations.toggleMenu(self, True)
    
    @Slot()
    def doUnarchive(self):
        self.__setUnarchiveLayout(True)
        Animations.toggleMenu(self, True)

    @Slot()
    def doCreateFile(self):
        self.__setCreateFileLayout(True)
        Animations.toggleMenu(self, True)

    @Slot()
    def doCreateFolder(self):
        self.__setCreateFolderLayout(True)
        Animations.toggleMenu(self, True)

    @Slot()
    def doRename(self):
        self.__setRenameLayout(True)
        Animations.toggleMenu(self, True)


    # Method that creates all layout object from the frame layout
    def __createFrameLayoutElements(self):

        # =================   COPY ACTION  =======================
        # Copy button on right frame       
        self.copyButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.copyButton.move(120, 600)
        self.copyButton.setFixedSize(120, 32)
        self.copyButton.setVisible(False)

        # =================   MOVE ACTION  =======================
        # Move button on right frame
        self.moveButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.moveButton.move(120, 600)
        self.moveButton.setFixedSize(120, 32)
        self.moveButton.setVisible(False)

        # =================   DELETE ACTION  =======================
        # Delete button on right frame
        self.deleteButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.deleteButton.move(120, 600)
        self.deleteButton.setFixedSize(120, 32)
        self.deleteButton.setVisible(False)

        # =================   UNARCHIVE ACTION  =======================
        # Unarchive button on right frame        
        self.unarchiveButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.unarchiveButton.move(120, 600)
        self.unarchiveButton.setFixedSize(120, 32)
        self.unarchiveButton.setVisible(False)

        # =================   ARCHIVE ACTION  =======================

        self.archiveLabel.move(100, 590)
        self.archiveLabel.setStyleSheet(self.FRAME_LABEL_STYLE)
        self.archiveLabel.setVisible(False)

        self.archiveNameEditLine.move(55, 620)
        self.archiveNameEditLine.setFixedSize(250,30)
        self.archiveNameEditLine.setStyleSheet(self.FRAME_LINE_EDIT_STYLE)
        self.archiveNameEditLine.setVisible(False)

        self.archiveButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.archiveButton.move(120, 700)
        self.archiveButton.setFixedSize(120, 32)
        self.archiveButton.setVisible(False)

        # =================   CREATE NEW FILE ACTION  =======================

        
        self.createFileLabel.move(120, 590)
        self.createFileLabel.setStyleSheet(self.FRAME_LABEL_STYLE)
        self.createFileLabel.setVisible(False)

        self.createFileEditLine.move(55, 620)
        self.createFileEditLine.setFixedSize(250,30)
        self.createFileEditLine.setStyleSheet(self.FRAME_LINE_EDIT_STYLE)
        self.createFileEditLine.setVisible(False)

        self.createFileButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.createFileButton.move(120, 700)
        self.createFileButton.setFixedSize(120, 32)
        self.createFileButton.setVisible(False)


        # =================   CREATE NEW FOLDER ACTION  =======================

        
        self.createFolderLabel.move(120, 590)
        self.createFolderLabel.setStyleSheet(self.FRAME_LABEL_STYLE)
        self.createFolderLabel.setVisible(False)

        
        self.createFolderEditLine.move(55, 620)
        self.createFolderEditLine.setFixedSize(250,30)
        self.createFolderEditLine.setStyleSheet(self.FRAME_LINE_EDIT_STYLE)
        self.createFolderEditLine.setVisible(False)

        self.createFolderButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.createFolderButton.move(120, 700)
        self.createFolderButton.setFixedSize(120, 32)
        self.createFolderButton.setVisible(False)

        # =================  RENAME ELEMENT ACTION  =======================

        self.renameElementLabel.move(120, 590)
        self.renameElementLabel.setStyleSheet(self.FRAME_LABEL_STYLE)
        self.renameElementLabel.setVisible(False)

        self.renameElementEditLine.move(55, 620)
        self.renameElementEditLine.setFixedSize(250,30)
        self.renameElementEditLine.setStyleSheet(self.FRAME_LINE_EDIT_STYLE)
        self.renameElementEditLine.setVisible(False)

        self.renameElementButton.setStyleSheet(self.FRAME_BUTTON_STYLE)
        self.renameElementButton.move(120, 700)
        self.renameElementButton.setFixedSize(120, 32)
        self.renameElementButton.setVisible(False)


    # Method that sets the frame layout for rename operation
    def __setRenameLayout(self, shown):

        if shown == True:
            self.renameElementLabel.setVisible(True)
            self.renameElementEditLine.setVisible(True)
            self.renameElementButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setDeleteLayout(False)
            self.__setMoveLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.renameElementLabel.setVisible(False)
            self.renameElementEditLine.setVisible(False)
            self.renameElementButton.setVisible(False)

    # Method that sets the frame layout for archive operation
    def __setCreateFileLayout(self, shown):

        if shown == True:
            self.createFileLabel.setVisible(True)
            self.createFileEditLine.setVisible(True)
            self.createFileButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setDeleteLayout(False)
            self.__setMoveLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.createFileLabel.setVisible(False)
            self.createFileEditLine.setVisible(False)
            self.createFileButton.setVisible(False)

    # Method that sets the frame layout for archive operation
    def __setCreateFolderLayout(self, shown):

        if shown == True:
            self.createFolderLabel.setVisible(True)
            self.createFolderEditLine.setVisible(True)
            self.createFolderButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setDeleteLayout(False)
            self.__setMoveLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.createFolderLabel.setVisible(False)
            self.createFolderEditLine.setVisible(False)
            self.createFolderButton.setVisible(False)

    # Method that sets the frame layout for archive operation
    def __setArchiveLayout(self, shown):

        if shown == True:
            self.archiveLabel.setVisible(True)
            self.archiveNameEditLine.setVisible(True)
            self.archiveButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setDeleteLayout(False)
            self.__setMoveLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.archiveLabel.setVisible(False)
            self.archiveNameEditLine.setVisible(False)
            self.archiveButton.setVisible(False)


    # Method that sets the frame layout for copy operation
    def __setCopyLayout(self, shown):

        if shown == True:
            self.copyButton.setVisible(True)
            self.__setMoveLayout(False)
            self.__setDeleteLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.copyButton.setVisible(False)

    # Method that sets the frame layout for move operation
    def __setMoveLayout(self, shown):

        if shown == True:
            self.moveButton.setVisible(True)

            self.__setDeleteLayout(False)
            self.__setCopyLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.moveButton.setVisible(False)

    # Method that sets the frame layout for delete operation
    def __setDeleteLayout(self, shown):

        if shown == True:
            self.deleteButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setMoveLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setUnarchiveLayout(False)

        else:
            self.deleteButton.setVisible(False)

    # Method that sets the frame layout for unarchive operation
    def __setUnarchiveLayout(self, shown):

        if shown == True:
            self.unarchiveButton.setVisible(True)

            self.__setCopyLayout(False)
            self.__setMoveLayout(False)
            self.__setRenameLayout(False)
            self.__setCreateFileLayout(False)
            self.__setCreateFolderLayout(False)
            self.__setArchiveLayout(False)
            self.__setDeleteLayout(False)

        else:
            self.unarchiveButton.setVisible(False)



class Animations(MainWidget):

    def toggleMenu(self, enable):

        # CASE WHEN THE RIGHT MENU SHOULD BE OPENED
        if enable == True:

            # RIGHT MENU ANIMATION
            self.toggleMenuAnimation = QPropertyAnimation(self.frameRightMenu, b"geometry")
            self.toggleMenuAnimation.setDuration(self.RIGHT_MENU_ANIMATION_DURATION)
            self.toggleMenuAnimation.setStartValue(self.frameRightMenu.geometry())

            width = self.frameRightMenu.width()
            height = self.frameRightMenu.height()
            x = self.frameRightMenu.x()
            y = self.frameRightMenu.y()

            self.toggleMenuAnimation.setEndValue(QRect(1080, y, width, height))
            self.toggleMenuAnimation.start()
            self.frameRightMenu.setStyleSheet(self.TOOGLE_OPENED_COLOR)
            
            # TOGGLE BUTTON ANIMATION
            self.toggleButtonAnimation = QPropertyAnimation(self.toggleButton, b"geometry")
            self.toggleButtonAnimation.setDuration(self.TOGGLE_BUTTON_ANIMATION_DURATION)
            width = self.toggleButton.width()
            height = self.toggleButton.height()
            y = self.toggleButton.y()
            self.toggleButtonAnimation.setStartValue(self.toggleButton.geometry())
            self.toggleButtonAnimation.setEndValue(QRect(980, y, width, height))
            self.toggleButtonAnimation.start()
            self.toggleButton.setIcon(QIcon(self.BUTTON_OPENED_ICON_PATH))

            self._enable = False

        else:
            
            # CASE WHEN THE RIGHT MENU SHOULD BE CLOSED

            # RIGHT MENU ANIMATION
            self.toggleMenuAnimation = QPropertyAnimation(self.frameRightMenu, b"geometry")
            self.toggleMenuAnimation.setDuration(self.RIGHT_MENU_ANIMATION_DURATION)
            self.toggleMenuAnimation.setStartValue(self.frameRightMenu.geometry())

            width = self.frameRightMenu.width()
            height = self.frameRightMenu.height()
            x = self.frameRightMenu.x()
            y = self.frameRightMenu.y()

            self.toggleMenuAnimation.setEndValue(QRect(1450, y, width, height))
            self.toggleMenuAnimation.start()
            self.frameRightMenu.setStyleSheet(self.TOOGLE_CLOSED_COLOR)
            
            # TOGGLE BUTTON ANIMATION
            self.toggleButtonAnimation = QPropertyAnimation(self.toggleButton, b"geometry")
            self.toggleButtonAnimation.setDuration(self.TOGGLE_BUTTON_ANIMATION_DURATION)
            width = self.toggleButton.width()
            height = self.toggleButton.height()
            y = self.toggleButton.y()
            self.toggleButtonAnimation.setStartValue(self.toggleButton.geometry())
            self.toggleButtonAnimation.setEndValue(QRect(1300, y, width, height))
            self.toggleButtonAnimation.start()
            self.toggleButton.setIcon(QIcon(self.BUTTON_CLOSED_ICON_PATH))

            self._enable = True
        