import tkinter as tk
import random

IDLE_PATH = "assets/idle.gif"
RIGHT_PATH = "assets/ghost_right_move.gif"
LEFT_PATH = "assets/ghost_left_move.gif"
ANGRY_PATH = "assets/ghost_angry.gif"


def load_images():
    default = [
        tk.PhotoImage(file=IDLE_PATH, format="gif -index %i" % (i)).zoom(2, 2)
        for i in range(16)
    ]

    walk_right = [
        tk.PhotoImage(file=RIGHT_PATH, format="gif -index %i" % (i)).zoom(2, 2)
        for i in range(16)
    ]

    walk_left = [
        tk.PhotoImage(file=LEFT_PATH, format="gif -index %i" % (i)).zoom(2, 2)
        for i in range(16)
    ]

    angry = [
        tk.PhotoImage(file=ANGRY_PATH, format="gif -index %i" % (i)).zoom(2, 2)
        for i in range(12)
    ]

    return default, walk_right, walk_left, angry

