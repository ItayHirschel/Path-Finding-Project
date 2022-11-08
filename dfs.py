from Igraph import IGraph
from abstractnode import AbstractNode

class DFS_scanner():

    class LIFO():

        def __init__(self):
            self.queue : list[AbstractNode] = []

        def push(self, node : AbstractNode):
            self.queue.append(node)
        
        def pop(self):
            return self.queue.pop()
        
        def clear(self):
            self.queue.clear()

    def __init__(self, graph : IGraph):
        self.graph = graph
        self.fifo = DFS_scanner.LIFO()

    def update_fifo(self):
        self.fifo.clear()
        for node in self.graph.get_starters():
            self.graph.touch(node)
            self.fifo.push(node)
    
    def step(self):
        node = self.fifo.pop()
        if None != node:
            for neighbor in self.graph.get_neighbors(node):
                self.graph.touch(neighbor)
                self.fifo.push(neighbor)
            self.graph.finish(node)
            return (not self.graph.goal_reached())
        return False

    def is_success(self):
        return self.graph.goal_reached()

    def draw_solution(self):
        self.graph.draw_solution()