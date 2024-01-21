from PyQt5 import QtGui

IDLE_PATH = "assets/idle.gif"
RIGHT_PATH = "assets/ghost_right_move.gif"
LEFT_PATH = "assets/ghost_left_move.gif"
ANGRY_PATH = "assets/ghost_angry.gif"


def load_images():
    default = QtGui.QMovie(IDLE_PATH)
    walk_right = QtGui.QMovie(RIGHT_PATH)
    walk_left = QtGui.QMovie(LEFT_PATH)
    angry = QtGui.QMovie(ANGRY_PATH)

    return default, walk_right, walk_left, angry
