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

btn_orange = pyglet.resource.image("button_orange.png")
btn_orange_p = pyglet.resource.image("button_orange_p.png")

btn_yellow = pyglet.resource.image("button_yellow.png")
btn_yellow_p = pyglet.resource.image("button_yellow_p.png")

btn_green = pyglet.resource.image("button_green.png")
btn_green_p = pyglet.resource.image("button_green_p.png")

btn_blue = pyglet.resource.image("button_blue.png")
btn_blue_p = pyglet.resource.image("button_blue_p.png")

btn_purple = pyglet.resource.image("button_purple.png")
btn_purple_p = pyglet.resource.image("button_purple_p.png")

number_buttons = [btn_red, btn_orange, btn_yellow, btn_green, btn_blue, btn_purple, btn_input, btn_input, btn_input]

pressed = {
    btn_input: btn_input_p,
    btn_grey: btn_grey,
    btn_save: btn_save_p,
    btn_restore: btn_restore_p,
    btn_quit: btn_quit_p,
    btn_red: btn_red_p,
    btn_orange: btn_orange_p,
    btn_yellow: btn_yellow_p,
    btn_green: btn_green_p,
    btn_blue: btn_blue_p,
    btn_purple: btn_purple_p
}