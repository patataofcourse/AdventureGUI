import pyglet

btn_grey = pyglet.resource.image("button_grey.png")

btn_input = pyglet.resource.image("button_input.png")
btn_input_p = pyglet.resource.image("button_input_p.png")

btn_save = pyglet.resource.image("button_save.png")
btn_save_p = pyglet.resource.image("button_save_p.png")

btn_restore = pyglet.resource.image("button_restore.png")
btn_restore_p = pyglet.resource.image("button_restore_p.png")

btn_quit = pyglet.resource.image("button_quit.png")
btn_quit_p = pyglet.resource.image("button_quit_p.png")

btn_red = pyglet.resource.image("button_red.png")
btn_red_p = pyglet.resource.image("button_red_p.png")

pressed = {
    btn_input: btn_input_p,
    btn_grey: btn_grey,
    btn_save: btn_save_p,
    btn_restore: btn_restore_p,
    btn_quit: btn_quit_p,
    btn_red: btn_red_p
}