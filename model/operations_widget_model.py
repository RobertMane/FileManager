from PySide2.QtCore import QObject, Signal
from utilities.system_manager import SystemManager

class OperationsWidgetModel(QObject):
    combo_box_selection_changed = Signal(str)

    # COMBO BOX CURRENT SELECTION
    @property
    def combo_box_selection(self):
        return self._combo_box_selection

    @combo_box_selection.setter
    def combo_box_selection(self, value):
        self._combo_box_selection = value
        self.combo_box_selection_changed.emit(value)

    # COMBO BOX LIST REPRESENTED BY SYSTEM DRIVES
    @property
    def combo_box_list(self):
        return self._combo_box_list

    @combo_box_list.setter
    def combo_box_selection(self, value):
        self._combo_box_list = value

    def __init__(self):
        super().__init__()

        self._combo_box_list = SystemManager.get_drives()