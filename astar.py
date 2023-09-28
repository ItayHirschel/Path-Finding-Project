from Igraph import IGraph
from abstractnode import AbstractNode
from MinHeap import MinHeap

class ASTAR_scanner():

    def init_heap(self):
        for node in self.heap.collection:
            self.graph.touch(node)
        self.heapInit = True

    def __init__(self, graph : IGraph):
        self.graph = graph
        self.distanceDict = {}
        self.heap = MinHeap()
        self.heapInit = False

    def update_queue(self):
        self.heap.clear()
        self.distanceDict.clear()
        for node in self.graph.get_starters():
            self.heap.push(node, self.graph.distanceHeuristic(node, self.graph.destination))
            self.distanceDict[node] = 0


    
    def step(self):
        
        if not self.heapInit:
            self.init_heap()

        
        if not self.heap.isEmpty() :
            node, value = self.heap.pop()
            dist = self.distanceDict[node]
            for neighbor in self.graph.get_neighbors(node):
                H = self.graph.distanceHeuristic(neighbor, self.graph.destination)

                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    self.graph.touch(neighbor)
                    self.distanceDict[neighbor] = dist + 1
                    self.heap.push(neighbor, dist + 1 + H)
                    self.graph.attach_prev_to_node( node , neighbor) 

                elif neighbor.state == AbstractNode.Mode.WORKED:
                    if (dist + 1) < self.distanceDict[neighbor]:
                        self.distanceDict[neighbor] = dist + 1
                    
                    if self.heap.decrease(neighbor, self.distanceDict[neighbor] + H):
                        self.graph.attach_prev_to_node( node , neighbor) 
                    


            self.graph.finish(node)
            
        return (not self.heap.isEmpty()) and (not self.graph.goal_reached())

    def is_success(self):
        return self.graph.goal_reached()

    def draw_solution(self):
        self.graph.draw_solution()
    