import os

import pygame

path = os.path.join(os.curdir, "resources")

def get_image(name, alpha = True):
    name = os.path.join(path, name)
    if alpha:
        return pygame.image.load(name).convert_alpha()
    else:
        return pygame.image.load(name).convert()

class ButtonImages:
    def __init__(self, unpressed, pressed):
        self.unpressed = unpressed
        self.pressed = pressed
        
        #shortcuts
        self.up = unpressed
        self.p = pressed

def from_filenames(unpressed, pressed, alpha=True):
    return ButtonImages(get_image(unpressed, alpha), get_image(pressed, alpha))
ButtonImages.from_filenames = from_filenames
del from_filenames

btn_grey = ButtonImages.from_filenames("button_grey.png", "button_grey.png")

btn_input = ButtonImages.from_filenames("button_input.png", "button_input_p.png")

btn_save = ButtonImages.from_filenames("button_save.png", "button_save_p.png")

btn_restore = ButtonImages.from_filenames("button_restore.png", "button_restore_p.png")

btn_quit = ButtonImages.from_filenames("button_quit.png", "button_quit_p.png")

btn_red = ButtonImages.from_filenames("button_red.png", "button_red_p.png")

btn_orange = ButtonImages.from_filenames("button_orange.png", "button_orange_p.png")

btn_yellow = ButtonImages.from_filenames("button_yellow.png", "button_yellow_p.png")

btn_green = ButtonImages.from_filenames("button_green.png", "button_green_p.png")

btn_blue = ButtonImages.from_filenames("button_blue.png", "button_blue_p.png")

btn_purple = ButtonImages.from_filenames("button_purple.png", "button_purple_p.png")

btn_1 = ButtonImages.from_filenames("button_1.png", "button_1_p.png")

btn_2 = ButtonImages.from_filenames("button_2.png", "button_2_p.png")

btn_3 = ButtonImages.from_filenames("button_3.png", "button_3_p.png")

btn_4 = ButtonImages.from_filenames("button_4.png", "button_4_p.png")

btn_5 = ButtonImages.from_filenames("button_5.png", "button_5_p.png")

btn_6 = ButtonImages.from_filenames("button_6.png", "button_6_p.png")

btn_7 = ButtonImages.from_filenames("button_7.png", "button_7_p.png")

btn_8 = ButtonImages.from_filenames("button_8.png", "button_8_p.png")

btn_9 = ButtonImages.from_filenames("button_9.png", "button_9_p.png")

number_buttons = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
