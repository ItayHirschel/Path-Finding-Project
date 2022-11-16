from Igraph import IGraph
from abstractnode import AbstractNode

class BFS_scanner():

    class FIFO():

        def __init__(self):
            self.queue : list[AbstractNode] = []
            self.is_init = False

        def push(self, node : AbstractNode):
            self.queue.append(node)
        
        def pop(self):
            node = None
            if len(self.queue) > 0:
                node = self.queue[0]
                self.queue = self.queue[1:]
            return node
        
        def clear(self):
            self.queue.clear()
        

    def init_fifo(self):
        for node in self.fifo.queue:
            self.graph.touch(node)
        self.fifo.is_init = True

    def __init__(self, graph : IGraph):
        self.graph = graph
        self.fifo = BFS_scanner.FIFO()

    def update_queue(self):
        self.fifo.clear()
        for node in self.graph.get_starters():
            self.fifo.push(node)


    
    def step(self):

        if not self.fifo.is_init:
            self.init_fifo()
        
        if len(self.fifo.queue) :
            node = self.fifo.pop()
            for neighbor in self.graph.get_neighbors(node):
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    self.graph.touch(neighbor)
                    self.fifo.push(neighbor)
                    self.graph.attach_prev_to_node( node , neighbor) 
            self.graph.finish(node)
            
        return len(self.fifo.queue) and (not self.graph.goal_reached())

    def is_success(self):
        return self.graph.goal_reached()

    def draw_solution(self):
        self.graph.draw_solution()
    

    

        
        