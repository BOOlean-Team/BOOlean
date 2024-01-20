import random
import tkinter as tk
from tkinter import PhotoImage
import platform

from ghost import load_images
from chatgpt import openChatGPTWindow
import click

window = tk.Tk()

ANIMATION_DELAY = 150
WINDOW_SIZE = 1400

DEFAULT_ANIMATION = 1
WALK_RIGHT_ANIMATION = 2
WALK_LEFT_ANIMATION = 3

PET_WIDTH = 48
screen_width = window.winfo_screenwidth()

current_frame = 0
# Chooses a random animation to start with
current_state = random.randrange(1, 4, 1)

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
        pos += 30

    elif current_state == WALK_LEFT_ANIMATION: # move left
        frame = walk_left[current_frame]
        current_frame, current_state = next_frame(current_frame, walk_left, current_state)
        pos -= 30

    # window.geometry("100x100+" + str(pos) + "+300")
    # label.configure(image=frame)
    canvas.config(width=screen_width, height=window.winfo_screenheight())
    canvas.coords(pet_widget, pos, WINDOW_SIZE / 2)
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

def angry_change(pos, pet_widget, click_counter):
    CLICK_LIMIT = 5
    if click_counter > CLICK_LIMIT:
        open_subwindow()
        window.after(ANIMATION_DELAY, update, 0, 0, pos, pet_widget)
    elif click_counter > 0:
        canvas.itemconfig(pet_widget, image=angry[click_counter % 12])
        window.after(ANIMATION_DELAY, angry_change, pos, pet_widget, click_counter - 1)
    else:
        window.after(ANIMATION_DELAY, update, 0, 0, pos, pet_widget)

def open_subwindow():
    subwindow = tk.Toplevel(window)
    subwindow.title("Subwindow")
    subwindow.size
    
    subwindow.geometry("{0}x{1}+0+0".format(subwindow.winfo_screenwidth(), subwindow.winfo_screenheight()))

    img = PhotoImage(file="assets/img/jumpscare.png")

    # Add a label to display the image
    image_label = tk.Label(subwindow, image=img)
    image_label.image = img  # Keep a reference to the image to prevent it from being garbage collected
    image_label.pack(padx=20, pady=20)
    subwindow.lift()

canvas = tk.Canvas(window, width=WINDOW_SIZE, height=WINDOW_SIZE)

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
window.bind('<Button-3>', lambda event: click.on_click_event(pos, event, window, pet_widget, angry_change))


# label = tk.Label(window, bd=0)
# label.pack()

# For different OS systems
if platform.system() == "Darwin":
    window.config(bg="systemTransparent")
    window.wm_attributes('-transparent', True)
    window.overrideredirect(True)
    # window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{yPos}")
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")

    window.wm_attributes("-topmost", True)
elif platform.system() == "Windows":
    window.config(bg="white")
    window.attributes('-alpha', 1)
    window.overrideredirect(True)
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{yPos}")
    window.wm_attributes("-topmost", True)

def start_animation(canvas, pet_widget, frame):
    canvas.itemconfig(pet_widget, image=frame)
    

window.after(0, start_animation, canvas, pet_widget, default[0])
window.after(ANIMATION_DELAY, update, current_frame, current_state, pos, pet_widget)

window.mainloop()
