import sys
from PySide2.QtWidgets import QApplication

from model.operations_widget_model import OperationsWidgetModel
from controllers.operations_widget_ctrl import OperationsWidgetController
from views.main_view import Window


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.operationsWidgetModel = OperationsWidgetModel()
        self.operationsWidgetController = OperationsWidgetController(self.operationsWidgetModel)
        self.main_view = Window(self.operationsWidgetModel, self.operationsWidgetController)
        self.main_view.show()

if __name__ == '__main__':
    
    # Creating the main window
    app = App(sys.argv)
    
    app.exec_()