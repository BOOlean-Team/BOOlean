import random
from PyQt5.QtCore import Qt, QPointF, QEasingCurve, QPropertyAnimation, QTimer, QTime
from PyQt5.QtWidgets import QLabel
from chatgpt import NewChatGPTWindow
from freemovement import MovementHandler
from audio import AudioManager, AUDIO_SQUEAK

class ClickHandler:
    def __init__(self, main_window, widget, default_gif, angry_gif):
        self.main_window = main_window
        self.widget = widget
        self.offset = QPointF()

        self.default_gif = default_gif
        self.angry_gif = angry_gif

        self.audio_manager = AudioManager()
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
            # Display angry GIF
            self.update_angry_state(True)
            self.click_start_time = QTime.currentTime()  # Record the time when the mouse is pressed
            self.free_movement_handler.animation.pause()  # Pause the animation when dragging starts

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)
            self.update_dragging_state()

    def end_drag(self, event):
        print("drag has ended")
        # Calculate the duration between press and release
        click_duration = self.click_start_time.elapsed()

        # Play the squeak sound only for quick clicks (e.g., less than 500 milliseconds)
        if click_duration < 500:
            print("playsound")
            self.audio_manager.play_sound(AUDIO_SQUEAK)

        # Resume the animation when dragging ends
        self.free_movement_handler.animation.resume()
        
        # Display default GIF
        self.update_angry_state(False)
    
    def update_dragging_state(self):
        self.main_window.label.setMovie(self.angry_gif)
        self.angry_gif.start()

    def update_angry_state(self, is_angry):
        gif =  self.angry_gif if is_angry else self.default_gif
        self.main_window.label.setMovie(gif)
        gif.start()
