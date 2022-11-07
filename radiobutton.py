from absradiooption import AbstractRadio
from workmode import WORK_MODE, WorkMode
from ProjectConstants import *

class RadioButton(AbstractRadio):

    def __init__(self, surface : pygame.Surface, font, option_list = [], def_choice = -1):
        super().__init__(surface, font, option_list, def_choice)
    
    def handle_click(self):
        if WORK_MODE.get_mode() != WorkMode.STERILE:
            x, y = pygame.mouse.get_pos()
            for opt in self.options:
                if opt.is_in(x, y):
                    self.choice = opt


