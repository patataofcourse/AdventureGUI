import sys

import pygame
window = pygame.display.set_mode((888, 80))
pygame.display.set_caption('AdventureGUI v0.2-dev')

import button
import res
from func import *

closed = False

fps = 60
clock = pygame.time.Clock()

buttons = button.ButtonSet(window)

for n in range(9):
    n += 1
    buttons.add_button(f"b{n}", button.Button.from_object(8+72*(n-1), 8, res.btn_grey))

def test_event():
    print("button 1 was clicked")

buttons["b1"].event = test_event

extras = ("save", "restore", "quit")
for b in extras:
    n = extras.index(b)+1
    buttons.add_button(f"{b}", button.Button.from_object(600+72*n, 8, res.btn_grey))

def run():
    buttons["quit"].change_images(res.btn_quit)

    # main loop
    global closed
    while True:
        # events
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                closed = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                buttons.check_pressed(x,y)
                buttons()
            if event.type == pygame.MOUSEBUTTONUP:
                buttons.release()

        # closes loop if pygame has been quit through an event
        if closed:
            break
        
        # rendering
        window.fill(color("333")) # background color, to be changed
        buttons.draw()

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()