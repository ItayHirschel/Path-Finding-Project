from ProjectConstants import *

class AbstractRadio():

    class Option:
        def __init__(self, name : str, mode, x_pos : int, y_pos : int):
            self.opt_name = name
            self.mode = mode
            self.x_pos = x_pos
            self.y_pos = y_pos
        

    def __init__(self, option_list = [], def_choice = -1):
        self.none_chosen = AbstractRadio.Option("null", None, 0, 0)
        self.options = option_list
        self.choice = self.none_chosen
        if (0 <= def_choice < len(self.options)):
            self.choice = self.options[def_choice]
    
    def add_option(self, opt : Option):
        self.options.append(opt)

    def get_mode(self):
        return self.choice.mode
    
    def choose(self, index):
        self.choice = self.options[index]
        
    