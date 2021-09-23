import pyglet

max_buttons = 0
running = True
value = ""

window = pyglet.window.Window(width=888, height=80, caption="AdventureGUI (currently just a control thing lmao)")

def quit():
    if not running:
        pyglet.app.exit()
        window.close()
        value = "q"