import adventurescript
import threading

import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

import res

def hex_color(hex, alpha=0xff):
    red = (hex & 0xff0000) // 0x10000
    green = (hex & 0xff00) // 0x100
    blue = hex & 0xff
    return red, green, blue, alpha

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
quit_btn = pyglet.gui.PushButton(816, 8, pressed=res.btn_quit_p, depressed=res.btn_quit, batch=batch)
frame.add_widget(quit_btn)

buttons[0]._depressed_img = res.btn_input
buttons[0]._hover_img = res.btn_input
buttons[0]._pressed_img = res.btn_input_p
buttons[0]._sprite.image = res.btn_input

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_show():
    pass

as_thread = threading.Thread(target=adventurescript.parse_sync, args=("test",))

#as_thread.start()
pyglet.app.run()