from PySide2.QtWidgets import QWidget, QPushButton, QComboBox, QFrame, QListView
from PySide2.QtGui import QIcon
from PySide2.QtCore import QDir, QSize, Slot

from custom_items.tree_view_model import TreeViewModelItem
from custom_items.tree_view import TreeView


class MainWidget(QWidget):

    # CONSTANTS
    EMPTY_STRING = ""
    
    TOOGLE_BUTTON_ICON_PATH = 'resources/toogle_button_icon.png'

    TOOGLE_BUTTON_CSS_PROPERTY = "QPushButton {background-color: rgb(1,150,250); border:  none ; qproperty-iconSize: 80px}"

    WIDTH = 1440
    HEIGHT = 900

    def __init__(self, parent, model, controller):        
        super(MainWidget, self).__init__(parent)
        
        self._model = model
        self._controller = controller
        
        # SYSTEM ELEMENTS TREE VIEW
        
        self.systemElementsTreeView = QListView(self)
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
        self.discSelectionComboBox.addItems(self._model.combo_box_list)
        

        # BUTTON WHICH TOOGLE ON/OFF THE TREE VIEW CONTAINING THE SELECTED ITEMS TREE VIEW
        self.toogleButton = QPushButton(QIcon(self.TOOGLE_BUTTON_ICON_PATH), self.EMPTY_STRING, self)
        self.toogleButton.setFixedSize(100,70)
        self.toogleButton.move(1300,0)
        self.toogleButton.setStyleSheet(self.TOOGLE_BUTTON_CSS_PROPERTY)

        # CONNECT WIDGETS TO CONTROLLER
        self.discSelectionComboBox.currentTextChanged.connect(self._controller.change_combo_box_selection)


        # LISTEN FOR MODEL EVENT SIGNALS
        self._model.combo_box_selection_changed.connect(self.on_combo_box_selection_changed)

        """
        self.frameRightMenu = QFrame(self)
        self.frameRightMenu.setMinimumSize(QSize(150,self.HEIGHT))
        self.frameRightMenu.setFrameShape(QFrame.StyledPanel)
        self.frameRightMenu.setFrameShadow(QFrame.Raised)
        self.frameRightMenu.move(1100,15)
        self.frameRightMenu.setStyleSheet("background-color: rgb(85, 170, 255);")
        """
 
    @Slot(str)
    def on_combo_box_selection_changed(self, value):
        index = self.discSelectionComboBox.findText(value)
        self.discSelectionComboBox.setCurrentIndex(index)
        





