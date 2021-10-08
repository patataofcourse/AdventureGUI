import pygame

class ScrollBar:
    def __init__(self, width, height, scroll_surface, show_height):
        self.width = width
        self.height = height
        self.surface = scroll_surface
        self.show_height = show_height
        self.surface_height = self.surface.get_rect().height

        self.pos = 0
        if self.surface_height - show_height < height - 32:
            self.pos_height = height - (self.surface_height - show_height)
            self.equivalence = 1
        else:
            self.pos_height = 32
            self.equivalence = height - 32

        print(self.height, self.pos_height)

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, (0xe0,0xe0,0xe0), pygame.Rect(x, y, self.width, self.height))
        pygame.draw.rect(surface, (0xc0, 0xc0, 0xc0), pygame.Rect(x, y+self.pos, self.width, self.pos_height))

