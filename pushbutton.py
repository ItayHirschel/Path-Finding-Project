import pygame
from ProjectConstants import *
from textbox import TextBox
from clickable import Clickable
from workmode import WORK_MODE, WorkMode

class PushButton(TextBox, Clickable):
    def __init__(self, x_pos, y_pos, width, height, text, func, bg_color = WHITE, txt_color = BLACK, inact_modes = [WorkMode.STERILE]):
        super().__init__(x_pos, y_pos, width, height, text = text,  bg_color = bg_color, txt_color = txt_color)
        self.func = func
        Clickable.CLICKABLES.append(self)
        self.inactive = inact_modes
    
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
        if WORK_MODE.get_mode() not in self.inactive:
            x, y = pygame.mouse.get_pos()
            if self.is_in(x, y):
                return self.func()
