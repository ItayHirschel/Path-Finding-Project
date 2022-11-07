import pygame
from ProjectConstants import *
from textbox import TextBox

class PushButton(TextBox):
    def __init__(self, surface : pygame.Surface, font, x_pos, y_pos, width, height, text, func, bg_color = WHITE, txt_color = BLACK):
        super().__init__(surface, x_pos, y_pos, font, width, height, text = text,  bg_color = bg_color, txt_color = txt_color)
        self.func = func
    
    def is_in(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def blit(self):
        x,y = pygame.mouse.get_pos()
        orig_color = self.bg_color
        if (self.is_in(x, y)):
            self.bg_color = darken(self.bg_color)
        super().blit()
        self.bg_color = orig_color
    
    def handle_click(self):
        x, y = pygame.mouse.get_pos()
        if self.is_in(x, y):
            return self.func()
