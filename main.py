import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

def hex_color(hex, alpha=0xff):
    red = (hex & 0xff0000) // 0x10000
    green = (hex & 0xff00) // 0x100
    blue = hex & 0xff
    print(red, green, blue)
    return red, green, blue, alpha

#import res
btn_input = pyglet.resource.image("button_input.png")
btn_greyed = pyglet.resource.image("button_grey.png")

window = pyglet.window.Window(width=888, height=80, caption="AdventureGUI (currently just a control thing lmao)")

buttons = []
x = 8
for b in range(9):
    buttons.append(pyglet.sprite.Sprite(img=btn_greyed, x=x, y=8))
    x += 72

special_buttons = []
x += 16
for b in range(3):
    special_buttons.append(pyglet.sprite.Sprite(img=btn_greyed, x=x, y=8))
    x += 72

@window.event
def on_draw():
    window.clear()
    for button in buttons:
        button.draw()
    for button in special_buttons:
        button.draw()
pyglet.app.run()