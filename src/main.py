import sys
import random

from PyQt5 import QtCore, QtWidgets
from ghost import load_images
from chatgpt import NewChatGPTWindow


ANIMATION_DELAY = 150
WINDOW_SIZE = 100

DEFAULT_ANIMATION = 1
WALK_RIGHT_ANIMATION = 2
WALK_LEFT_ANIMATION = 3

PET_SIZE = 100

# Chooses a random animation to start with
current_state = random.randrange(1, 4, 1)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.default, self.walk_right, self.walk_left, self.angry = load_images()
        self.default.setScaledSize(QtCore.QSize(PET_SIZE, PET_SIZE))
        self.walk_right.setScaledSize(QtCore.QSize(PET_SIZE, PET_SIZE))
        self.walk_left.setScaledSize(QtCore.QSize(PET_SIZE, PET_SIZE))
        self.angry.setScaledSize(QtCore.QSize(PET_SIZE, PET_SIZE))

        self.w = QtWidgets.QWidget()
        self.w.resize(250, 200)
        self.w.move(300, 300)

        self.label = QtWidgets.QLabel(self.w)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.resize(PET_SIZE, PET_SIZE)

        self.w.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                              QtCore.Qt.FramelessWindowHint)
        self.w.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.w.mousePressEvent = self.new_window
        self.w.show()

        self.label.setMovie(self.default)
        self.default.start()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.update_animation())
        self.timer.start()

    def new_window(self, _):
        self.ws = NewChatGPTWindow()
        self.ws.show()

    def update_animation(self):
        current_state = random.randrange(1, 4, 1)

        if (current_state == DEFAULT_ANIMATION):
            gif = self.default
        elif (current_state == WALK_RIGHT_ANIMATION):
            gif = self.walk_right
        elif (current_state == WALK_LEFT_ANIMATION):
            gif = self.walk_left

        self.label.setMovie(gif)
        gif.start()


GHOST_IDLE = 'assets/idle.gif'


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
