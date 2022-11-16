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
        self.dist_dict = {}

    def update_queue(self):
        self.lifo.clear()
        self.dist_dict.clear()
        for node in self.graph.get_starters():
            self.graph.touch(node)
            self.lifo.push(node)
            self.dist_dict[self.graph.get_key_for_node(node)] = 0
    

    
    def step(self):

        if not self.lifo.is_init:
            self.lifo.init_lifo()

        

        if len(self.lifo.queue) :
            node = self.lifo.pop()
            new_node = False
            for neighbor in self.graph.get_neighbors(node):
                
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED and not new_node:
                    self.lifo.push(node)
                    self.graph.touch(neighbor)
                    self.lifo.push(neighbor)
                    self.graph.attach_prev_to_node( node , neighbor)
                    self.dist_dict[self.graph.get_key_for_node(neighbor)] = self.dist_dict[self.graph.get_key_for_node(node)] + 1
                    new_node = True
                
            
            if not new_node:
                self.graph.finish(node)
            
        return len(self.lifo.queue) and not self.is_success()

    def is_success(self):
        return self.graph.goal_reached()

    def draw_solution(self):
        self.graph.draw_solution()