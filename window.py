import pyglet

import res
from func import *

LABEL_LINES = 20

closed = False

window = pyglet.window.Window(width=888, height=480, caption="AdventureGUI v0.2-dev")
batch = pyglet.graphics.Batch()

frame = pyglet.gui.Frame(window, order=4)

buttons = []
x = 8
for b in range(9):
    b = pyglet.gui.PushButton(x, 8, res.btn_grey, res.btn_grey, batch=batch)
    frame.add_widget(b)
    buttons.append(b)
    x += 72

save_btn = pyglet.gui.PushButton(672, 8, res.btn_grey, res.btn_grey, batch=batch)
frame.add_widget(save_btn)

restore_btn = pyglet.gui.PushButton(744, 8, res.btn_grey, res.btn_grey, batch=batch)
frame.add_widget(restore_btn)

quit_btn = pyglet.gui.PushButton(816, 8, res.btn_quit_p, res.btn_quit, batch=batch)
frame.add_widget(quit_btn)

label = pyglet.text.Label("",x=8,y=472-18, height=392, width=872, color=(255,255,255,255), batch=batch, multiline = True)
labeltext = []

@window.event
def on_draw():
    window.clear()
    label.text = "\n".join(labeltext)
    batch.draw()

def update(dt): #update every frame
    if closed:
        pyglet.app.exit()
        if hasattr(pyglet.window, "close"):
            window.close()
pyglet.clock.schedule_interval(update, 1/60)

@window.event
def on_close():
    global closed
    closed = True

def change_button_gfx(button, gfx):
    button._depressed_img = gfx
    button._hover_img = gfx
    button._pressed_img = res.pressed.get(gfx, gfx)
    button._sprite.image = gfx