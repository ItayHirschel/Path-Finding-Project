import pygame
from ProjectConstants import *

class PushButton:
    def __init__(self, surface : pygame.Surface, font, left, right, top, bottom, text, func):
        self.rect = pygame.Rect(left, top, right - left, bottom - top)
        self.text = text
        self.surface = surface
        self.font = font
        self.func = func
    
    def is_in(self, x, y):
        return (self.rect.left <= x <= self.rect.right) and (self.rect.top <= y <= self.rect.bottom)
    
    def blit(self):
        x,y = pygame.mouse.get_pos()
        color = WHITE
        if (self.is_in(x, y)):
            color = (int(color[0] * SHADE_FACTOR), int(color[1] * SHADE_FACTOR),int(color[2] * SHADE_FACTOR))
        pygame.draw.rect(self.surface, color, self.rect)
        text = self.font.render(self.text, True, BLACK, color)
        text_rect = text.get_rect()
        text_rect.center =  self.rect.center
        self.surface.blit(text, text_rect)
    
    def handle_click(self):
        x, y = pygame.mouse.get_pos()
        if self.is_in(x, y):
            return self.func()
