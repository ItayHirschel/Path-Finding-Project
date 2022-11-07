from abstractnode import AbstractNode
from ProjectConstants import *
from enum import Enum
from printable import Printable
import pygame
from colorpallete import *

class MatrixGraph(Printable):


    class InnerNode(AbstractNode, Printable):

        def __init__(self, surface : pygame.Surface, x_pos, y_pos, color_scheme = [UNTOUCHED_COLOR, TOUCHED_COLOR, FINISHED_COLOR, OFF_COLOR]):
            super().__init__(x_pos, y_pos)
            self.rect = pygame.Rect((x_pos, y_pos), (VisGlobals["vertex size"], VisGlobals["vertex size"]))
            self.color_scheme = color_scheme
            self.surface = surface
        
        def blit(self):
            x,y = pygame.mouse.get_pos()
            color = self.color_scheme[int(self.state)]
            if self.rect.collidepoint(x, y):
                color = darken(color)
            
            pygame.draw.rect(self.surface, color, self.rect)

        
    def __init__(self, surface : pygame.Surface, rows = MatrixGlobals["rows"], columns = MatrixGlobals["columns"]):
        self.rows = rows
        self.columns = columns
        self.surface = surface
        self.WidthSpread = (self.surface.get_height() - 10) / columns
        self.HeightSpread = (self.surface.get_width() - 10) / rows
        self.vertices = [[MatrixGraph.InnerNode(surface, 10 + x_ind * self.WidthSpread, 10 + y_ind * self.HeightSpread) for x_ind in range(columns)] for y_ind in range(rows)]

    def get_vertices(self):
        return [y for row in self.vertices for y in row]

    def locate(self, x_pos, y_pos):
        return (int((y_pos - 10) // self.HeightSpread), int((x_pos - 10) // self.WidthSpread))
    
    def get_node_by_coor(self, x, y):
        row, column = self.locate(x, y)
        if (0 <= row < self.rows) and (0 <= column < self.columns):
            return self.vertices[row][column]
        return None
    
    def graph_reset(self):
        self.rows = MatrixGlobals["rows"]
        self.columns = MatrixGlobals["columns"]
        self.WidthSpread = (PygameConstants["GRAPH WIDTH"] - 10) / self.columns
        self.HeightSpread = (PygameConstants["GRAPH HEIGHT"] - 10) / self.rows
        self.vertices = [[MatrixGraph.InnerNode(self.surface, 10 + x_ind * self.WidthSpread, 10 + y_ind * self.HeightSpread) for x_ind in range(self.columns)] for y_ind in range(self.rows)]

    def blit(self):
        for node in self.get_vertices():
            node.blit()

