import sys

import pygame

from func import *

closed = False

fps = 60
clock = pygame.time.Clock()

window = pygame.display.set_mode((888, 80))
pygame.display.set_caption('AdventureGUI v0.2-dev')

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
        
        # Processing
        # This section will be built out later
    
        # Render elements of the game
        window.fill(color("333"))
        pygame.display.update()
        clock.tick(fps)