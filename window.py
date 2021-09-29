import sys

import pygame
import pygame.locals as l

closed = False

fps = 60
clock = pygame.time.Clock()

window = pygame.display.set_mode((888, 80))
pygame.display.set_caption('My Game!')

def run():
  # The main game loop
  while True:
    global closed
    if closed:
        pygame.quit()
        return
    # Get inputs
    for event in pygame.event.get() :
      if event.type == l.QUIT :
        pygame.quit()
        closed = True
        return
    
    # Processing
    # This section will be built out later
 
    # Render elements of the game
    window.fill((0,0,0))
    pygame.display.update()
    clock.tick(fps)