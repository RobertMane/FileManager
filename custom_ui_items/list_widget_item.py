from PySide2.QtWidgets import QListWidgetItem

class ListWidgetItem(QListWidgetItem):

    def __init__(self, item):

        super(ListWidgetItem, self).__init__(item.icon(), item.text())

        self._item = item