import pyglet

def pyglet_color(hex, alpha=0xff):
    red = (hex & 0xff0000) // 0x10000
    green = (hex & 0xff00) // 0x100
    blue = hex & 0xff
    print(red, green, blue)
    return red, green, blue, alpha

window = pyglet.window.Window()
window.height = 200
label = pyglet.text.Label('Hello, world!',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center',
                          color=pyglet_color(0x00a0a0))

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()