import pygame
window = pygame.display.set_mode((888, 480))
pygame.display.set_caption('AdventureGUI v0.3-dev')

import button
import res
import misc
import scrollbar

closed = False

fps = 60
clock = pygame.time.Clock()

buttons = button.ButtonSet(window)

for n in range(9):
    n += 1
    buttons.add_button(f"b{n}", button.Button.from_object(8+72*(n-1), 408, res.btn_grey))

extras = ("save", "restore", "quit")
for b in extras:
    n = extras.index(b)+1
    buttons.add_button(f"{b}", button.Button.from_object(600+72*n, 408, res.btn_grey))

scroll_surface = pygame.Surface((856, 600))
scrollbar = scrollbar.ScrollBar(16, 384, scroll_surface, 384)

def run():
    buttons["quit"].change_images(res.btn_quit)

    # main loop
    global closed
    while True:
        # events
        events = list(pygame.event.get())
        for event in events:
            if event.type == pygame.QUIT :
                pygame.quit()
                closed = True
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                buttons.check_pressed(x,y)
            if event.type == pygame.MOUSEBUTTONUP:
                buttons()
                buttons.release()

        # closes loop if pygame has been quit through an event
        if closed:
            break
        
        # rendering
        window.fill(misc.color("333")) # background color, to be changed
        buttons.draw()
        window.blit(scroll_surface.subsurface(0,0,856,384), (8,8))
        scrollbar.draw(window, 864, 8)

        #update frame
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()