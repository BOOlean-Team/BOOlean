import random
from PyQt5.QtCore import Qt, QPointF, QEasingCurve, QPropertyAnimation, QTimer
from PyQt5.QtWidgets import QLabel

class ClickHandler:
    def __init__(self, widget):
        self.widget = widget
        self.offset = QPointF()
        self.animation = QPropertyAnimation(self.widget, b'pos', self.widget)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.move_timer = QTimer(self.widget)
        self.move_timer.timeout.connect(self.move_pet_smoothly)
        self.move_timer.start(3500)  # Adjust the interval as needed (milliseconds)

        self.widget.mousePressEvent = self.start_drag
        self.widget.mouseMoveEvent = self.drag_pet
        self.widget.mouseReleaseEvent = self.end_drag  # Added mouse release event

    def move_pet_smoothly(self):
        screen_rect = self.widget.screen().availableGeometry()
        pet_rect = self.widget.geometry()

        target_x = random.randint(0, screen_rect.width() - pet_rect.width())
        target_y = random.randint(0, screen_rect.height() - pet_rect.height())

        self.animation.setStartValue(self.widget.pos())
        self.animation.setEndValue(QPointF(target_x, target_y))
        self.animation.setDuration(1300)  # Adjust the duration as needed (milliseconds)
        self.animation.start()

    def start_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()
            self.animation.pause()  # Pause the animation when dragging starts

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)

    def end_drag(self, event):
        self.animation.resume()  # Resume the animation when dragging ends
