import pyglet

btn_grey = pyglet.resource.image("button_grey.png")

btn_input = pyglet.resource.image("button_input.png")
btn_input_p = pyglet.resource.image("button_input_p.png")

btn_save = pyglet.resource.image("button_save.png")

btn_restore = pyglet.resource.image("button_restore.png")

btn_quit = pyglet.resource.image("button_quit.png")

pressed = {
    btn_input: btn_input_p,
    btn_grey: btn_grey
}