import pyglet

import res

closed = False

window = pyglet.window.Window(width=888, height=80, caption="AdventureGUI (currently just a control thing lmao)")
batch = pyglet.graphics.Batch()

frame = pyglet.gui.Frame(window, order=4)

buttons = []
x = 8
for b in range(9):
    b = pyglet.gui.PushButton(x, 8, res.btn_grey, res.btn_grey, batch=batch)
    frame.add_widget(b)
    buttons.append(b)
    x += 72

save_btn = pyglet.gui.PushButton(672, 8, res.btn_save_p, res.btn_save, batch=batch)
frame.add_widget(save_btn)

restore_btn = pyglet.gui.PushButton(744, 8, res.btn_restore_p, res.btn_restore, batch=batch)
frame.add_widget(restore_btn)

quit_btn = pyglet.gui.PushButton(816, 8, res.btn_quit_p, res.btn_quit, batch=batch)
frame.add_widget(quit_btn)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt): #update every frame
    pass
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