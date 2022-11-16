
class Printable:

    PRINTABLES = []
    activated = False
    surface = None
    font = None

    def blit(self):
        if not self.activated:
            print("ERROR : Printable class of type ", type(self), " has no blit implementation")
            self.activated = True
    
    def attach(screen, font):
        Printable.surface = screen
        Printable.font = font
        