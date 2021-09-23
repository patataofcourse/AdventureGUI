import adventurescript.defaultio as default
import time

import events
import res
import window

show = default.show
query = default.query
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

# io = default.as_io(default.show, default.wait, default.query, default.load_file)