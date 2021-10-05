import sys

import pygame
window = pygame.display.set_mode((888, 480))
pygame.display.set_caption('AdventureGUI v0.2.1')

import pygame_menu

import button
import res
import misc

closed = False

fps = 60
clock = pygame.time.Clock()

buttons = button.ButtonSet(window)

for n in range(9):
    n += 1
    buttons.add_button(f"b{n}", button.Button.from_object(8+72*(n-1), 408, res.btn_grey))

def test_event():
    print("button 1 was clicked")

buttons["b1"].event = test_event

extras = ("save", "restore", "quit")
for b in extras:
    n = extras.index(b)+1
    buttons.add_button(f"{b}", button.Button.from_object(600+72*n, 408, res.btn_grey))

scroll_world = pygame.Surface((856, 600))
scroll_area = pygame_menu._scrollarea.ScrollArea(872, 384, area_color=(200,200,200), world = scroll_world, scrollbar_thick=16)
scroll_surface = pygame.Surface((872, 384))

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                buttons.check_pressed(x,y)
                buttons()
            if event.type == pygame.MOUSEBUTTONUP:
                buttons.release()
        scroll_area.update(events)

        # closes loop if pygame has been quit through an event
        if closed:
            break
        
        # rendering
        window.fill(misc.color("333")) # background color, to be changed
        buttons.draw()
        scroll_area.draw(scroll_surface)
        window.blit(scroll_surface, (8,8))

        #update frame
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()