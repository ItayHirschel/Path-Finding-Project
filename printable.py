
class Printable:
    activated = False
    def blit(self):
        if not self.activated:
            print("WARNING : Printable class of type ", type(self), " has no blit implementation")
            self.activated = True
        