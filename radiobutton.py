from absradiooption import AbstractRadio
from workmode import WORK_MODE, WorkMode
from ProjectConstants import *
from clickable import Clickable
from printable import Printable

class RadioButton(AbstractRadio, Clickable):

    class CircleOption(AbstractRadio.Option):

        def __init__(self, name : str, mode, x_pos : int, y_pos : int, button_size = radio_button_size):
            super().__init__(name, mode, x_pos, y_pos)
            self.button_size = button_size
        
        def is_in(self, x : int, y : int):
            return ((x - self.x_pos) ** 2 + (y - self.y_pos) ** 2) <= self.button_size ** 2

        def blit(self, chosen : bool, x : int, y : int):

            color = WHITE
            if self.is_in(x, y):
                color = darken(color)
            pygame.draw.circle(Printable.surface, color,(self.x_pos,self.y_pos), self.button_size)

            text = Printable.font.render(self.opt_name, True, WHITE, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (self.x_pos , self.y_pos)
            text_rect.left = self.x_pos + self.button_size * 1.5
            Printable.surface.blit(text, text_rect)

            if chosen:
                pygame.draw.circle(Printable.surface, BLACK,(self.x_pos,self.y_pos), self.button_size * radio_inner_circle_factor)


    class RectOption(AbstractRadio.Option):

        def __init__(self, name : str, mode, x_pos : int, y_pos : int, rect : pygame.Rect):
            super().__init__(name, mode, x_pos, y_pos)
            self.rect = rect
            
        def is_in(self, x : int, y : int):
            return self.rect.collidepoint(x, y)
        
        def blit(self, chosen : bool, x : int, y : int):
            color = WHITE
            
            if chosen:
                color = YELLOW

            if self.is_in(x, y):
                color = darken(color)

            pygame.draw.rect(Printable.surface, color, self.rect)

            txt = Printable.font.render(str(self.text), True, BLACK, color)
            text_rect = txt.get_rect()
            text_rect.center = self.rect.center
            Printable.surface.blit(txt, text_rect)


    def __init__(self, option_list = [], def_choice = -1, inactive_modes = [WorkMode.STERILE, WorkMode.PLAY]):
        super().__init__( option_list, def_choice)
        self.inactive_modes = inactive_modes
        Printable.PRINTABLES.append(self)
        Clickable.CLICKABLES.append(self)
    
    def handle_click(self):
        if WORK_MODE.get_mode() not in self.inactive_modes :
            x, y = pygame.mouse.get_pos()
            for opt in self.options:
                if opt.is_in(x, y):
                    self.choice = opt

    def blit(self):
        x,y = pygame.mouse.get_pos()
        for opt in self.options:
            opt.blit(self.choice == opt, x , y)
        

