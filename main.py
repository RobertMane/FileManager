import sys
from PySide2.QtWidgets import QApplication

# VIEW IMPORT
from views.main_view import Window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Creating the main window
    window=Window()
    window.show()
    app.exec_()