import pyglet

import window as w
window = w.window

max_buttons = 0
choice = False
wait = False
value = ""

def quit():
    if choice:
        global value
        value = "q"
        window.close()
        pyglet.app.exit()