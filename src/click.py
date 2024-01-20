import random
from PyQt5.QtCore import Qt, QTimer, QPointF, QEasingCurve, QPropertyAnimation
class ClickHandler:
    def __init__(self, widget):
        self.widget = widget
        self.offset = QPointF()
        self.move_timer = QTimer(self.widget)
        self.move_timer.timeout.connect(self.move_pet_smoothly)
        self.move_timer.start(3000)  # Adjust the interval as needed (milliseconds)

        self.animation = QPropertyAnimation(self.widget, b'pos', self.widget)
        self.animation.setEasingCurve(QEasingCurve.Linear)

        self.widget.mousePressEvent = self.start_drag
        self.widget.mouseMoveEvent = self.drag_pet

    def move_pet_smoothly(self):
        screen_rect = self.widget.screen().availableGeometry()
        pet_rect = self.widget.geometry()

        target_x = random.randint(0, screen_rect.width() - pet_rect.width())
        target_y = random.randint(0, screen_rect.height() - pet_rect.height())

        self.animation.setStartValue(self.widget.pos())
        self.animation.setEndValue(QPointF(target_x, target_y))
        self.animation.setDuration(5000)  # Adjust the duration as needed (milliseconds)
        self.animation.start()

    def start_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def drag_pet(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(event.globalPos() - self.offset)


#ANIMATION_DELAY = 150

#click_counter = 0

#def on_click_event(pos, event, window, pet_widget, angry_change):

#    global click_counter

    #print(f"Click Count: {click_counter}")
#    window.after(ANIMATION_DELAY, angry_change, pos, pet_widget, click_counter)
#    click_counter += 1

