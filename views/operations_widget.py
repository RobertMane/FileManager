from PySide2.QtWidgets import QWidget, QPushButton, QComboBox, QFrame, QGridLayout, QListWidget, QLabel, QListWidgetItem
from PySide2.QtGui import QIcon
from PySide2.QtCore import QDir, QSize, Slot, QPropertyAnimation, QRect
from PySide2 import QtCore

from custom_items.tree_view_model import TreeViewModelItem
from custom_items.tree_view import TreeView
from custom_items.files_view import FilesListView




class MainWidget(QWidget):

    # CONSTANTS
    EMPTY_STRING = ""
    SELECTED_ITEMS_TEXT = "Selected items:"
    
    BUTTON_CLOSED_ICON_PATH = 'resources/menu_closed_button_icon.png'
    BUTTON_OPENED_ICON_PATH = 'resources/menu_opened_button_icon.png'


    TOOGLE_BUTTON_CSS_PROPERTY = "QPushButton {background-color: rgb(1,150,250); border:  none ; qproperty-iconSize: 80px}"

    TOOGLE_CLOSED_COLOR = "background-color: rgb(1,150,250);"
    TOOGLE_OPENED_COLOR = "background-color: rgba(44, 53, 57, 0.2);"

    WHITE = "background-color: rgb(255, 255, 255);"


    WIDTH = 1440
    HEIGHT = 900

    FILES_LIST_VIEW_WIDTH = 820
    FILES_LIST_VIEW_HEIGHT = 680

    TOGGLE_BUTTON_ANIMATION_DURATION = 200
    RIGHT_MENU_ANIMATION_DURATION = 250




    def __init__(self, parent, model, controller):        
        super(MainWidget, self).__init__(parent)
        
        self._model = model
        self._controller = controller
        
        # FILES LIST VIEW
        
        self.filesListView = FilesListView(self.FILES_LIST_VIEW_WIDTH, self.FILES_LIST_VIEW_HEIGHT, self._model, self)
        self.filesListView.move(230,120)



        # TREE VIEW FOR SYSTEM DIRECTORY HIERARCHY
        self.treeView = TreeView(self)
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

        self.selectedItemsLabel = QLabel(self.SELECTED_ITEMS_TEXT, self.frameRightMenu)
        self.selectedItemsLabel.move(100, 20)
        self.selectedItemsLabel.setStyleSheet("QLabel { background-color : rgba(44, 53, 57, 0); }")
    
        self.selectedFilesListWidget = QListWidget(self.frameRightMenu)
        self.selectedFilesListWidget.setFixedSize(320,500)
        self.selectedFilesListWidget.move(23,60)
        self.selectedFilesListWidget.setStyleSheet(self.WHITE)

        item = QListWidgetItem("elem")
        self.selectedFilesListWidget.insertItem(0, item)



        
 
    @Slot(str)
    def on_combo_box_selection_changed(self, value):
        index = self.discSelectionComboBox.findText(value)
        self.discSelectionComboBox.setCurrentIndex(index)
        


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
        






