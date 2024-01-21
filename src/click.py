import random
from PyQt5.QtCore import Qt, QPointF, QEasingCurve, QPropertyAnimation, QTimer
from PyQt5.QtWidgets import QLabel
from chatgpt import NewChatGPTWindow
from freemovement import MovementHandler


class ClickHandler:
    def __init__(self, widget):
        self.widget = widget
        self.offset = QPointF()

        self.free_movement_handler = MovementHandler(self.widget)

        self.setup_drag_handling()

    def setup_drag_handling(self):
        self.widget.mousePressEvent = self.handle_mouse_press
        self.widget.mouseMoveEvent = self.drag_pet
        self.widget.mouseReleaseEvent = self.end_drag

    def handle_mouse_press(self, QMouseEvent):
        if (QMouseEvent.button() == Qt.LeftButton):
            self.start_drag(QMouseEvent)
        elif (QMouseEvent.button() == Qt.RightButton):
            self.ws = NewChatGPTWindow()
            self.ws.show()

    def start_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()
            # Pause the animation when dragging starts
            self.free_movement_handler.animation.pause()

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)

    def end_drag(self, event):
        # Resume the animation when dragging ends
        self.free_movement_handler.animation.resume()
