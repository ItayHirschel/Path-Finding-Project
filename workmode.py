from ProjectConstants import *
import pygame
from clickable import Clickable
from absradiooption import AbstractRadio


class WorkModeButton(Clickable, AbstractRadio):  

    def __init__(self, surface : pygame.Surface, font, option_list = [], def_choice = -1):
        super().__init__(surface, font, option_list, def_choice)
    
    def handle_click(self):
        x, y = pygame.mouse.get_pos()
        for opt in self.options:
            if opt.is_in(x, y):
                self.choice = opt

class WorkMode():
    STERILE = 0
    ON_OFF_MODE = 1
    CHOOSE_START = 2

work_modes = [
    WorkModeButton.Option("sterile mode", WorkMode.STERILE, 650, 570),
    WorkModeButton.Option("toggle button", WorkMode.ON_OFF_MODE, 650, 540),
    WorkModeButton.Option("choose stating point", WorkMode.CHOOSE_START, 650, 510)
]


WORK_MODE = WorkModeButton(None, None, work_modes, 0)

