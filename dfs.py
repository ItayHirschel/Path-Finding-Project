from Igraph import IGraph
from abstractnode import AbstractNode

class DFS_scanner():

    class LIFO():

        def __init__(self):
            self.queue : list[AbstractNode] = []
            self.is_init = False

        def push(self, node : AbstractNode):
            self.queue.append(node)
        
        def pop(self):
            return self.queue.pop()
        
        def clear(self):
            self.queue.clear()
        
        def init_lifo(self):
            for node in self.queue:
                node.touch()
            self.is_init = True

    def __init__(self, graph : IGraph):
        self.graph = graph
        self.lifo = DFS_scanner.LIFO()

    def update_queue(self):
        self.lifo.clear()
        for node in self.graph.get_starters():
            self.graph.touch(node)
            self.lifo.push(node)
    

    
    def step(self):

        if not self.lifo.is_init:
            self.lifo.init_lifo()

        

        if len(self.lifo.queue) :
            node = self.lifo.pop()
            for neighbor in self.graph.get_neighbors(node):
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    self.graph.touch(neighbor)
                    self.lifo.push(neighbor)

            self.graph.finish(node)
            return (not self.graph.goal_reached())
            
        return False

    def is_success(self):
        return self.graph.goal_reached()

    def draw_solution(self):
        self.graph.draw_solution()