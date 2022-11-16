from abstractnode import AbstractNode

class IGraph():
    activated = [False , False, False, False, False, False]

    def __init__(self):
        self.starting_points = []
        self.destination = None
    
    def get_starters(self) -> list[AbstractNode]:
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no get_neighbors implementation")
            self.activated[5] = True

    def get_neighbors(self, node : AbstractNode) -> list[AbstractNode]:
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no get_neighbors implementation")
            self.activated[0] = True
    
    def touch(self, node : AbstractNode):
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no touch implementation")
            self.activated[1] = True
    
    def finish(self, node : AbstractNode):
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no finish implementation")
            self.activated[2] = True
    
    def goal_reached(self):
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no goal_reached implementation")
            self.activated[3] = True
    
    def get_destionation(self):
        pass
    
    def draw_solution(self):
        if not self.activated:
            print("ERROR : IGraph class of type ", type(self), " has no draw_solution implementation")
            self.activated[4] = True
    
    def attach_prev_to_node(self, previous, node):
        pass

    def get_key_for_node(self, node):
        pass
    
    