import random
import tkinter as tk
import platform

from ghost import load_images, move
from clickdrag import ClickDrag
from chatgpt import openChatGPTInput

ANIMATION_DELAY = 150
WINDOW_SIZE = 100
OFFSET = 300

window = tk.Tk()

default, walk_right, walk_left, angry = load_images()

# position of virtual pet
screen_width = window.winfo_screenwidth()
pet_width = 48
pos = (screen_width - pet_width) // 2

cycle = 0
current_state = 0
default_num = [1, 2, 3, 4]
right_num = [5, 6, 7]
left_num = [8, 9, 10]
event_num = random.randrange(1, 3, 1)

# event number
def event(cycle, current_state, event_num, pos, pet_widget, click_drag_handler):
    if not click_drag_handler.dragging:
        # Only open chat if not dragging
        openChatGPTInput(event, window)

    if event_num in default_num:
        current_state = 0
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)

    elif event_num in right_num:
        current_state = 1
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)

    elif event_num in left_num:
        current_state = 2
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)


def update(cycle, current_state, event_num, pos, pet_widget):
    frame = None
    if current_state == 0:  # default
        frame = default[cycle]
        cycle, event_num = move(cycle, default, event_num, 1, 9, pet_widget)

    elif current_state == 1: # move right
        frame = walk_right[cycle]
        cycle, event_num = move(cycle, walk_right, event_num, 1, 9, pet_widget)
        pos += 3

    elif current_state == 2: # move left
        frame = walk_left[cycle]
        cycle, event_num = move(cycle, walk_left, event_num, 1, 9, pet_widget)
        pos -= 3

    # window.geometry("100x100+" + str(pos) + "+300")
    # label.configure(image=frame)
    canvas.itemconfig(pet_widget, image=frame)
    window.after(ANIMATION_DELAY, lambda: event(cycle, current_state, event_num, pos, pet_widget, click_drag_handler))

def openChatGPTInput(event, window):
    if not hasattr(window, "_chatbox_opened"):
        print('open')
        textInput = tk.Toplevel(window)
        textInput.geometry('200x200')

        # Mark the window as having an open chatbox to prevent further openings
        window._chatbox_opened = True

canvas = tk.Canvas(window, width=100, height=100)
canvas.bind('<Button-1>', lambda event: click_drag_handler.start_drag(event))
canvas.pack()
canvas.focus_set()

pet_widget = canvas.create_image(
    WINDOW_SIZE / 2, WINDOW_SIZE / 2, image=default[0]
)

click_drag_handler = ClickDrag(window, pet_widget, update, openChatGPTInput)

# label = tk.Label(window, bd=0)
# label.pack()

# For different OS systems
if platform.system() == "Darwin":
    window.config(bg="systemTransparent")
    window.wm_attributes("-transparent", True)
elif platform.system() == "Windows":
    window.config(bg="white")
    window.attributes('-alpha', 1)

window.overrideredirect(True)
window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{OFFSET}")
window.wm_attributes("-topmost", True)
window.after(0, update, cycle, current_state, event_num, pos, pet_widget)
window.mainloop()
