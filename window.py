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
buttons.add_button("button1", button.Button.from_object(0, 0, res.btn_input))

def run():
    # The main game loop
    while True:
        global closed
        if closed:
            pygame.quit()
            return
        
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                closed = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                print(x,y)
    
        # Render elements of the game
        window.fill(color("fff"))
        pygame.display.update()
        clock.tick(fps)