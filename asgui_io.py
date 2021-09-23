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
    events.wait = False
    window.change_button_gfx(window.buttons[0], res.btn_input)
    while events.value == "":
        time.sleep(1/60)
    window.change_button_gfx(window.buttons[0], res.btn_grey)
    events.wait = True

# io = default.as_io(default.show, default.wait, default.query, default.load_file)