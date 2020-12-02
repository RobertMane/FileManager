from PySide2.QtCore import QObject, Slot

class OperationsWidgetController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(str)
    def change_combo_box_selection(self, index):
        self._model.combo_box_selection = index