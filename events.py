import pygame

import window

max_buttons = 1
choice = False
wait = False
value = ""
cansave = False

def save():
    if cansave:
        global value
        value = "s"

def restore():
    if cansave:
        global value
        value = "r"

def quit():
    if choice or wait:
        global value
        window.closed = True
        pygame.quit()

def button1():
    if choice or wait:
        global value
        value = "1"

def button2():
    if choice and max_buttons >= 2:
        global value
        value = "2"

def button3():
    if choice and max_buttons >= 3:
        global value
        value = "3"

def button4():
    if choice and max_buttons >= 4:
        global value
        value = "4"

def button5():
    if choice and max_buttons >= 5:
        global value
        value = "5"

def button6():
    if choice and max_buttons >= 6:
        global value
        value = "6"

def button7():
    if choice and max_buttons >= 7:
        global value
        value = "7"

def button8():
    if choice and max_buttons >= 8:
        global value
        value = "8"

def button9():
    if choice and max_buttons == 9:
        global value
        value = "9"

button_events = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

n = 1
while n < 10:
    window.buttons[f"b{n}"].set_event(button_events[n-1])
    n += 1

window.buttons["save"].set_event(save)
window.buttons["restore"].set_event(restore)
window.buttons["quit"].set_event(quit)