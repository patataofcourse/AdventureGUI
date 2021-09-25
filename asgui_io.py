import adventurescript.defaultio as default
import time

import events
import res
import window

show = default.show
load_file = default.load_file

def wait(info, **kwargs):
    events.value = ""
    events.wait = True
    window.change_button_gfx(window.buttons[0], res.btn_input)
    while events.value == "" and not window.closed:
        time.sleep(1/60)
    if window.closed:
        quit()
    window.change_button_gfx(window.buttons[0], res.btn_grey)
    events.wait = False

def query(info, text, choices, allow_save, **kwargs):
    if text != "":
        info.showfunc(info, "> " + text)
    c = 1
    for ch in choices:
        info.showfunc(info, f"> {c}. {ch}")
        c += 1
    
    events.value = ""
    events.choice = True
    events.max_buttons = c-1
    for choice in range(c-1):
        window.change_button_gfx(window.buttons[choice], res.number_buttons[choice])
    while events.value == "" and not window.closed:
        time.sleep(1/60)
    if window.closed:
        quit()
    for choice in range(c-1):
        window.change_button_gfx(window.buttons[choice], res.btn_grey)
    events.choice = False
    if events.value == "q":
        info.status = "quit"
        print(">> Quit")
        return 0
    else:
        print(">> " + events.value)
        return int(events.value)

# io = default.as_io(default.show, default.wait, default.query, default.load_file)