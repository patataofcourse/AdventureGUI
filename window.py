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

extras = ("save", "restore", "quit")
for b in extras:
    n = extras.index(b)+1
    buttons.add_button(f"{b}", button.Button.from_object(600+72*n, 8, res.btn_grey))

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
            if event.type == pygame.MOUSEBUTTONUP:
                buttons.release()
        
        # rendering
        window.fill(color("333"))
        buttons.draw()

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()