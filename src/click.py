from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QLabel
from chatgpt import NewChatGPTWindow
from freemovement import MovementHandler


class ClickHandler:
    def __init__(self, main_window, widget, default_gif, angry_gif):
        self.main_window = main_window
        self.widget = widget
        self.offset = QPointF()

        self.default_gif = default_gif
        self.angry_gif = angry_gif

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

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)
            self.update_dragging_state()

    def end_drag(self, event):
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()

    click_handler = ClickHandler(main_window, main_window.w, 
                        main_window.default, main_window.angry)
    main_window.w.mousePressEvent = click_handler.handle_mouse_press
    main_window.w.mouseMoveEvent = click_handler.drag_pet
    main_window.w.mouseReleaseEvent = click_handler.end_drag
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

