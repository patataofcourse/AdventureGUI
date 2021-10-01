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
buttons.add_button("button1", button.Button.from_object(8, 8, res.btn_input))

def run():
    # The main game loop
    global closed
    while not closed:
        # events
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                closed = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                buttons.check_pressed(x,y)
        
        # rendering
        window.fill(color("333"))
        buttons.draw()

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()