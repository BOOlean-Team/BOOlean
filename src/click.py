

CLICK_LIMIT = 5

click_counter = 0



def on_click_event(event, window, pet_widget, function):

    global click_counter
    # position of virtual pet
    screen_width = window.winfo_screenwidth()
    pet_width = 48
    pos = (screen_width - pet_width) // 2

    print(f"Click Count: {click_counter}")
    if click_counter > CLICK_LIMIT:
        print("ANGRY")
        window.after(0, function, pos, pet_widget)
    click_counter += 1

