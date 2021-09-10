import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

import res

def hex_color(hex, alpha=0xff):
    red = (hex & 0xff0000) // 0x10000
    green = (hex & 0xff00) // 0x100
    blue = hex & 0xff
    print(red, green, blue)
    return red, green, blue, alpha

window = pyglet.window.Window(width=888, height=80, caption="AdventureGUI (currently just a control thing lmao)")

buttons = []
x = 8
for b in range(9):
    buttons.append(pyglet.sprite.Sprite(img=res.btn_grey, x=x, y=8))
    x += 72
print(x)
save_btn = pyglet.sprite.Sprite(img=res.btn_save, x=672, y=8)
x += 72
restore_btn = pyglet.sprite.Sprite(img=res.btn_restore, x=744, y=8)
x += 72
quit_btn = pyglet.sprite.Sprite(img=res.btn_quit, x=816, y=8)

buttons[0].image = res.btn_input

@window.event
def on_draw():
    window.clear()
    for button in buttons:
        button.draw()
    save_btn.draw()
    restore_btn.draw()
    quit_btn.draw()
pyglet.app.run()