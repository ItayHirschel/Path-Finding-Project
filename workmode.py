from ProjectConstants import *
import pygame
from clickable import Clickable
from absradiooption import AbstractRadio
from printable import Printable

class WorkModeButton(Clickable, Printable, AbstractRadio):  

    def __init__(self, surface : pygame.Surface, font, option_list = [], def_choice = -1):
        super().__init__(surface, font, option_list, def_choice)
    
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
            
            pygame.draw.circle(self.surface, color,(opt.x_pos,opt.y_pos), opt.size)

            text = self.font.render(opt.opt_name, True, WHITE, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (opt.x_pos , opt.y_pos)
            text_rect.left = opt.x_pos + opt.size * 1.5
            self.surface.blit(text, text_rect)
        
        pygame.draw.circle(self.surface, BLACK, (self.choice.x_pos, self.choice.y_pos), self.choice.size * radio_inner_circle_factor)

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


WORK_MODE = WorkModeButton(None, None, work_modes, 0)

