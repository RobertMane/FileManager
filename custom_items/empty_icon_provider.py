from PySide2.QtWidgets import QFileIconProvider
from PySide2.QtGui import QIcon

class EmptyIconProvider(QFileIconProvider):
    def icon(self, _):
        return QIcon()