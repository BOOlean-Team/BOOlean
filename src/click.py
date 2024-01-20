


ANIMATION_DELAY = 150

click_counter = 0

def on_click_event(pos, event, window, pet_widget, angry_change):

    global click_counter

    #print(f"Click Count: {click_counter}")
    window.after(ANIMATION_DELAY, angry_change, pos, pet_widget, click_counter)
    click_counter += 1

