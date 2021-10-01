import pygame

class ButtonSet:
    def __init__(self, window):
        self.buttons = {}
        self.window = window
        self.hidden = False

    def add_button(self, name, button):
        self.buttons[name] = button
    
    def check_pressed(self, mouse_x, mouse_y):
        for button in self.buttons:
            self.buttons[button].check_pressed(mouse_x, mouse_y)
    
    def release(self):
        for button in self.buttons:
            self.buttons[button].is_pressed = False
    
    def draw(self):
        if self.hidden:
            return
        for button in self.buttons:
            button = self.buttons[button]
            self.window.blit(button.image(), (button.x, button.y))
    
    def remove_button(self, button):
        del self.buttons[button]

    def __getitem__(self, name):
        return self.buttons[name]
    
    def __call__(self):
        for button in self.buttons:
            self.buttons[button]()
    
    def hide(self):
        self.hidden = True
    
    def show(self):
        self.hidden = False


class Button:
    def __init__(self, x, y, unpressed, pressed):
        self.x = x
        self.y = y
        up_size = unpressed.get_size() 
        p_size = pressed.get_size()
        if p_size != up_size:
            raise Exception("Sizes of pressed and unpressed images for button don't match")
        self.size = up_size
        self.unpressed = unpressed
        self.pressed = pressed
        self.is_pressed = False
        def default_event():
            pass
        self.event = default_event

    def image(self):
        return self.pressed if self.is_pressed else self.unpressed

    def check_pressed(self, mouse_x, mouse_y):
        x = mouse_x >= self.x and mouse_x < (self.x+self.size[0]) 
        y = mouse_y >= self.y and mouse_y < (self.y+self.size[1])
        self.is_pressed = x and y
        return self.is_pressed

    def set_event(self, event):
        self.event = event

    def __call__(self):
        if self.is_pressed:
            self.event()

    def change_images(self, images):
        self.pressed = images.pressed
        self.unpressed = images.unpressed

def from_object(x, y, images):
    return Button(x, y, images.unpressed, images.pressed)

Button.from_object = from_object
del from_object