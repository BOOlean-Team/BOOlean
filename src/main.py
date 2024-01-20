import random
import tkinter as tk
import platform

from ghost import load_images
from chatgpt import openChatGPTWindow
import click

ANIMATION_DELAY = 150
WINDOW_SIZE = 100

DEFAULT_ANIMATION = 1
WALK_RIGHT_ANIMATION = 2
WALK_LEFT_ANIMATION = 3

PET_WIDTH = 48

current_frame = 0
# Chooses a random animation to start with
current_state = random.randrange(1, 4, 1)

window = tk.Tk()
default, walk_right, walk_left, angry = load_images()

# position of virtual pet
def virtual_pet_position(pet_width):
    return (window.winfo_screenwidth() - pet_width) // 2
pos = virtual_pet_position(PET_WIDTH)

yPos = 300

def update(current_frame, current_state, pos, pet_widget):
    frame = None
    #print(f"Update function called: current cycle is {cycle}, current state is {current_state}")

    if current_state == DEFAULT_ANIMATION:  # default
        frame = default[current_frame]
        current_frame, current_state = next_frame(current_frame, default, current_state)

    elif current_state == WALK_RIGHT_ANIMATION: # move right
        frame = walk_right[current_frame]
        current_frame, current_state = next_frame(current_frame, walk_right, current_state)
        pos += 3

    elif current_state == WALK_LEFT_ANIMATION: # move left
        frame = walk_left[current_frame]
        current_frame, current_state = next_frame(current_frame, walk_left, current_state)
        pos -= 3

    # window.geometry("100x100+" + str(pos) + "+300")
    # label.configure(image=frame)
    canvas.itemconfig(pet_widget, image=frame)
    window.after(ANIMATION_DELAY, update, current_frame, current_state, pos, pet_widget)

# Movement of animation
def next_frame(current_frame, full_animation, current_state):
    # print(f"Next frame function called: current_frame is {current_frame}, current state is {current_state}")
    if current_frame < len(full_animation) - 1: # Animation is incomplete
        current_frame += 1
    else: # Animation is complete
        # print("Animation complete")
        current_frame = 0
        previous_state = current_state
        while (current_state == previous_state):
            current_state = random.randrange(1, 4, 1) # Choose new event randomly
    return current_frame, current_state

def angry_change(pos, pet_widget):
    canvas.itemconfig(pet_widget, image=angry[0])
    window.after(ANIMATION_DELAY, update, 0, 0, pos, pet_widget)

canvas = tk.Canvas(window, width=100, height=100)
canvas.bind(
    '<Button-1>', lambda event: openChatGPTWindow(event, window, pos, yPos))
canvas.pack()
canvas.focus_set()

pet_widget = canvas.create_image(
    WINDOW_SIZE / 2, WINDOW_SIZE / 2, image=default[0]
)

def exit_click(event):
    window.destroy()

# Right clicking on the button
window.bind('<Button-2>', exit_click)

# Right clicking on the button
window.bind('<Button-3>', lambda event: click.on_click_event(event, window, pet_widget, angry_change))


# label = tk.Label(window, bd=0)
# label.pack()

# For different OS systems
if platform.system() == "Darwin":
    window.config(bg="systemTransparent")
    window.wm_attributes("-transparent", True)
    window.overrideredirect(True)
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{yPos}")
    window.wm_attributes("-topmost", True)
elif platform.system() == "Windows":
    window.config(bg="white")
    window.attributes('-alpha', 1)
    window.overrideredirect(True)
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{yPos}")
    window.wm_attributes("-topmost", True)

def start_animation(canvas, pet_widget, frame):
    canvas.itemconfig(pet_widget, image=frame)
    

window.after(0, start_animation, canvas, pet_widget, angry[0])
window.after(ANIMATION_DELAY, update, current_frame, current_state, pos, pet_widget)

window.mainloop()
