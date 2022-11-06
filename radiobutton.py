from ProjectConstants import *
import pygame

class RadioButton:

    class Option:
        def __init__(self, name : str, mode, x_pos : int, y_pos : int, button_size = radio_button_size):
            self.opt_name = name
            self.mode = mode
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.size = button_size

        def is_in(self, x, y):
            d = ((x - self.x_pos) ** 2 + (y - self.y_pos) ** 2) ** 0.5
            return d < self.size
        

    def __init__(self, surface : pygame.Surface, option_list = [], def_choice = -1):
        self.surface = surface
        self.none_chosen = RadioButton.Option("null", None, 0, 0)
        self.options = option_list
        self.choice = self.none_chosen
        if (0 <= def_choice < len(self.options)):
            self.choice = self.options[def_choice]
    
    def add_option(self, opt : Option):
        self.options.append(opt)
    
    def handel_click(self):
        x, y = pygame.mouse.get_pos()
        for opt in self.options:
            if opt.is_in(x, y):
                self.choice = opt

    def get_mode(self):
        return self.choice.mode
        
    def blit(self):
        
        for opt in self.options:
            pygame.draw.circle(self.surface, WHITE, (opt.x_pos,opt.y_pos), opt.size)
        
        pygame.draw.circle(self.surface, BLACK, (opt.x_pos,opt.y_pos), opt.size * radio_inner_circle_factor)

