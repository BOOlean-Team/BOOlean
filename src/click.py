import random
from PyQt5.QtCore import Qt, QPointF, QEasingCurve, QPropertyAnimation, QTimer, QTime
from PyQt5.QtWidgets import QLabel
from freemovement import MovementHandler
from audio import AudioManager, AUDIO_SQUEAK

class ClickHandler:
    def __init__(self, widget):
        self.widget = widget
        self.offset = QPointF()

        self.audio_manager = AudioManager()
        self.free_movement_handler = MovementHandler(self.widget)

        self.setup_drag_handling()

    def setup_drag_handling(self):
        self.widget.mousePressEvent = self.start_drag
        self.widget.mouseMoveEvent = self.drag_pet
        self.widget.mouseReleaseEvent = self.end_drag

    def start_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()
            self.click_start_time = QTime.currentTime()  # Record the time when the mouse is pressed
            self.free_movement_handler.animation.pause()  # Pause the animation when dragging starts

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)

    def end_drag(self, event):
        print("drag has ended")
        # Calculate the duration between press and release
        click_duration = self.click_start_time.elapsed()

        # Play the squeak sound only for quick clicks (e.g., less than 500 milliseconds)
        if click_duration < 500:
            print("playsound")
            self.audio_manager.play_sound(AUDIO_SQUEAK)

        self.free_movement_handler.animation.resume()  # Resume the animation when dragging ends
