from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QTreeView, QFileSystemModel, QComboBox, QPushButton, QFrame
from PySide2.QtGui import QIcon
from PySide2.QtCore import QDir, QSize

from custom_items.tree_view_model import TreeViewModelItem
from custom_items.tree_view import TreeView


class MainWidget(QWidget):

    # CONSTANTS
    EMPTY_STRING = ""
    
    TOOGLE_BUTTON_ICON_PATH = 'resources/toogle_button_icon.png'

    TOOGLE_BUTTON_CSS_PROPERTY = "QPushButton {background-color: rgb(1,150,250); border:  none ; qproperty-iconSize: 80px}"

    WIDTH = 1440
    HEIGHT = 900

    def __init__(self, parent):        
        super(MainWidget, self).__init__(parent)
        
        #self._model = QFileSystemModel(self)
        
        
        # SYSTEM ELEMENTS TREE VIEW
        
        self.systemElementsTreeView = QTreeView(self)
        self.systemElementsTreeView.setFixedSize(520,650)
        self.systemElementsTreeView.move(230,120)

       # self.systemElementsTreeView.setModel(self._model)

        # TREE VIEW FOR SYSTEM DIRECTORY HIERARCHY
        self.treeView = TreeView(self)
        self.treeView.setFixedSize(200,820)
        self.treeView.move(0,60)



        # DISC SELECTION COMBO BOX
        self.discSelectionComboBox = QComboBox(self)
        self.discSelectionComboBox.setFixedSize(100,30)
        self.discSelectionComboBox.move(230,60)

        # BUTTON WHICH TOOGLE ON/OFF THE TREE VIEW CONTAINING THE SELECTED ITEMS TREE VIEW
        self.toogleButton = QPushButton(QIcon(self.TOOGLE_BUTTON_ICON_PATH), self.EMPTY_STRING, self)
        self.toogleButton.setFixedSize(100,70)
        self.toogleButton.move(1300,0)
        self.toogleButton.setStyleSheet(self.TOOGLE_BUTTON_CSS_PROPERTY)

        self.frameRightMenu = QFrame(self)
        self.frameRightMenu.setMinimumSize(QSize(150,self.HEIGHT))
        self.frameRightMenu.setFrameShape(QFrame.StyledPanel)
        self.frameRightMenu.setFrameShadow(QFrame.Raised)
        self.frameRightMenu.move(1100,15)
        self.frameRightMenu.setStyleSheet("background-color: rgb(85, 170, 255);")



        # TREE VIEW 
        """
        self._model.setRootPath("C:/")
        self._model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.treeView.setModel(self._model)
        """
        """
        self.data = FileSystemData.init()
        self.treeViewModel=TreeViewModelItem(self.data)
        self.systemElementsTreeView = TreeView(self.treeViewModel)
        self.systemElementsTreeView.setFixedSize(520,650)
        self.systemElementsTreeView.move(230,120)
        """
        





