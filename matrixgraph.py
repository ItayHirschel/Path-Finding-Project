from abstractnode import AbstractNode
from ProjectConstants import *
from enum import Enum

class MatrixGraph:


    class InnerNode(AbstractNode):
        def __init__(self, x_pos, y_pos, color = UNTOUCHED_COLOR):
            super().__init__(x_pos, y_pos, "square", color)
        

        

    def __init__(self, rows = MatrixGlobals["rows"], columns = MatrixGlobals["columns"]):
        self.rows = rows
        self.columns = columns
        self.WidthSpread = (PygameConstants["GRAPH WIDTH"] - 10) / columns
        self.HeightSpread = (PygameConstants["GRAPH HEIGHT"] - 10) / rows
        self.vertices = [[MatrixGraph.InnerNode(10 + x_ind * self.WidthSpread, 10 + y_ind * self.HeightSpread) for x_ind in range(columns)] for y_ind in range(rows)]

    def get_vertices(self):
        return [y for row in self.vertices for y in row]

    def locate(self, x_pos, y_pos):
        return (int((y_pos - 10) // self.HeightSpread), int((x_pos - 10) // self.WidthSpread))
    
    def hover(self, row, col, prev):
        if (0 <= row < self.rows) and (0 <= col < self.columns):
            curr = self.vertices[row][col]
            curr.hov_flip()
        else:
            curr = None
        if (prev != None):
            prev.hov_flip()
        return curr