from printable import Printable
import pygame
from colorpallete import *

class TextBox(Printable):

    def __init__(self, x_pos, y_pos ,width , height , text  = "", bg_color = WHITE, txt_color = BLACK):
        self.text = text
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x_pos, y_pos)
        self.bg_color = bg_color
        self.txt_color = txt_color
        Printable.PRINTABLES.append(self)
    
    def set_text(self, new_text : str):
        self.text = new_text
    
    def blit(self):
        pygame.draw.rect(Printable.surface, self.bg_color, self.rect)
        txt = Printable.font.render(str(self.text), True, self.txt_color, self.bg_color)
        text_rect = txt.get_rect()
        text_rect.center = self.rect.center
        Printable.surface.blit(txt, text_rect)
