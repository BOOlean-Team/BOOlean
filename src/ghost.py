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

# gif movement
def move(cycle, frame, event_num, first, last, pet_widget):
    if cycle < len(frame) - 1:
        cycle += 1
    else:
        cycle = 0
        # FIX THIS FOR THE FREEZING ISSUE
        event_num = random.randrange(first, last + 1, 1)
    return cycle, event_num