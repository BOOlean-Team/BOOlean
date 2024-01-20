import tkinter as tk
import random

class ClickDrag:
    def __init__(self, parent, pet_widget, update_callback):
        self.parent = parent
        self.widget = pet_widget
        self.update_callback = update_callback
        self.dragging = False # to track dragging status

        self.drag_data = {"x": 0, "y": 0}

        self.parent.bind("<ButtonPress-1>", self.start_drag)
        self.parent.bind("<B1-Motion>", self.drag_pet)
        self.parent.bind("<ButtonRelease-1>", self.stop_drag)

    def start_drag(self, event):
        # Record the starting position of the drag
        self.click_position = (event.x, event.y)
        # Check for movement during the click
        if event.x != self.click_position[0] or event.y != self.click_position[1]:
            # If there was movement, update the dragging state
            self.dragging = True

    def end_drag(self, event):
        # Check if there was any movement during the click (drag)
        if self.dragging:
            self.dragging = False
        else:
            # If no movement, it's a button release event
            self.update_callback(event.x, event.y, 0, self.pet_widget)

    def drag_pet(self, event):
        x = self.parent.winfo_x() - self.drag_data["x"] + event.x
        y = self.parent.winfo_y() - self.drag_data["y"] + event.y
        self.parent.geometry(f"{self.parent.winfo_reqwidth()}x{self.parent.winfo_reqheight()}+{x}+{y}")

    def update_pet(self):
        # Optionally, you can include code to update the pet's position or perform other tasks
        pass

