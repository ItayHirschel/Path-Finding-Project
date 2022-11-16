from ProjectConstants import *
import pygame
from clickable import Clickable
from absradiooption import AbstractRadio
from printable import Printable


class WorkModeButton(Clickable, Printable, AbstractRadio):  

    class Option(AbstractRadio.Option):

        def __init__(self, name : str, mode, x_pos : int, y_pos : int, button_size = radio_button_size):
            super().__init__(name, mode, x_pos , y_pos )
            self.size = radio_button_size
        
        def is_in(self, x, y):
            return (x - self.x_pos) ** 2 + (y - self.y_pos) ** 2 <= self.size ** 2


    def __init__(self, option_list = [], def_choice = -1):
        super().__init__(option_list, def_choice)
        Clickable.CLICKABLES.append(self)
        Printable.PRINTABLES.append(self)
    
    def handle_click(self):
        x, y = pygame.mouse.get_pos()
        for opt in self.options:
            if opt.is_in(x, y):
                self.choice = opt
    
    def blit(self):
        x,y = pygame.mouse.get_pos()
        for opt in self.options:
            color = WHITE

            if opt.is_in(x, y):
                color = darken(color)
            
            pygame.draw.circle(Printable.surface, color,(opt.x_pos,opt.y_pos), opt.size)

            text = Printable.font.render(opt.opt_name, True, WHITE, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (opt.x_pos , opt.y_pos)
            text_rect.left = opt.x_pos + opt.size * 1.5
            Printable.surface.blit(text, text_rect)
        
        pygame.draw.circle(Printable.surface, BLACK, (self.choice.x_pos, self.choice.y_pos), self.choice.size * radio_inner_circle_factor)

class WorkMode():
    STERILE = 0
    ON_OFF_MODE = 1
    CHOOSE_START = 2
    CHOOSE_DEST = 3
    PLAY = 4

work_modes = [
    WorkModeButton.Option("sterile mode", WorkMode.STERILE, 650, 570),
    WorkModeButton.Option("toggle button on/off", WorkMode.ON_OFF_MODE, 650, 540),
    WorkModeButton.Option("choose stating point", WorkMode.CHOOSE_START, 650, 510),
    WorkModeButton.Option("choose destination", WorkMode.CHOOSE_DEST, 650, 480),
    WorkModeButton.Option("play", WorkMode.PLAY, 650, 450)
]


WORK_MODE = WorkModeButton( work_modes, 0)

