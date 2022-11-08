from absradiooption import AbstractRadio
from workmode import WORK_MODE, WorkMode
from ProjectConstants import *
from clickable import Clickable

class RadioButton(AbstractRadio, Clickable):

    def __init__(self, surface : pygame.Surface, font, option_list = [], def_choice = -1):
        super().__init__(surface, font, option_list, def_choice)
    
    def handle_click(self):
        if WORK_MODE.get_mode() not in [WorkMode.STERILE, WorkMode.PLAY] :
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

    def handel_click(self):
        if WORK_MODE.get_mode() != WorkMode.STERILE:
            x, y = pygame.mouse.get_pos()
            for opt in self.options:
                if opt.is_in(x, y):
                    self.choice = opt

