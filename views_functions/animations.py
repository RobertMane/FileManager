from PySide2.QtCore import QPropertyAnimation

from views.operations_widget import MainWidget

class Animations(MainWidget):

    def toggleMenu(self, maxWidth, enable):

        if enable == True:

            # Get the width of right menu
            width = self.frame_right_menu.width()
            standard = 0

            # Set max width
            if width == standard:
                widthExtended = maxWidth
            else:
                widthExtended = standard

            
            # Displaying the animation
            self.animation = QPropertyAnimation(self.frame_right_menu, "minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.OutInQuart)
            self.animation.start()
