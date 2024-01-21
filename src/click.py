import random
from PyQt5.QtCore import Qt, QPointF, QEasingCurve, QPropertyAnimation, QTimer
from PyQt5.QtWidgets import QLabel
from freemovement import MovementHandler

class ClickHandler:
    def __init__(self, widget):
        self.widget = widget
        self.offset = QPointF()

        self.free_movement_handler = MovementHandler(self.widget)

        self.setup_drag_handling()

    def setup_drag_handling(self):
        self.widget.mousePressEvent = self.start_drag
        self.widget.mouseMoveEvent = self.drag_pet
        self.widget.mouseReleaseEvent = self.end_drag

    def start_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()
            self.free_movement_handler.animation.pause()  # Pause the animation when dragging starts

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)

    def end_drag(self, event):
        self.free_movement_handler.animation.resume()  # Resume the animation when dragging ends
