import pygame

class ScrollBar:
    def __init__(self, width, height, scroll_surface, show_height):
        self.width = width
        self.height = height
        self.surface = scroll_surface
        self.show_height = show_height
        self.surface_height = self.surface.get_rect().height

        self.pos = 0
        self.pos_height = self.height - (self.surface_height - show_height)
        print(self.height, self.pos_height)

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, (0xe0,0xe0,0xe0), pygame.Rect(x, y, self.width, self.height))
        pygame.draw.rect(surface, (0xc0, 0xc0, 0xc0), pygame.Rect(x, y+self.pos, self.width, self.pos_height))
