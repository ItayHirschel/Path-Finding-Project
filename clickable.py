
class Clickable:
    activated = False
    def handel_click(self):
        if not self.activated:
            print("WARNING : Clickable class of type ", type(self), " has no handel_click implementation")
            self.activated = True
        