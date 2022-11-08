from abstractnode import AbstractNode
from ProjectConstants import *
from enum import Enum
from printable import Printable
import pygame
from colorpallete import *
from Igraph import IGraph
from workmode import WORK_MODE, WorkMode
from clickable import Clickable


class MatrixGraph(Printable, IGraph, Clickable):


    class InnerNode(AbstractNode, Printable):

        def __init__(self, surface : pygame.Surface, x_pos, y_pos, row, column, color_scheme = [UNTOUCHED_COLOR, TOUCHED_COLOR, FINISHED_COLOR, SOL_COLOR, OFF_COLOR]):
            super().__init__(x_pos, y_pos)
            self.rect = pygame.Rect(x_pos, y_pos, VisGlobals["vertex size"], VisGlobals["vertex size"])
            self.color_scheme = color_scheme
            self.surface = surface
            self.row = row
            self.column = column

        def blit(self, is_starting, is_destination):
            x,y = pygame.mouse.get_pos()
            color = self.color_scheme[int(self.state)]

            if is_starting:
                color = BLUE
            if is_destination:
                color = DEST_COLOR

            if self.rect.collidepoint(x, y):
                color = darken(color)
            pygame.draw.rect(self.surface, color, self.rect)

        def click_handler(self):
            if WORK_MODE.get_mode() == WorkMode.ON_OFF_MODE:
                self.flip()
        

        
    def __init__(self, surface : pygame.Surface):
        self.surface = surface
        self.graph_boot()
        

    def get_vertices(self):
        return [y for row in self.vertices for y in row]

    def locate(self, x_pos, y_pos):
        return (int((y_pos - 10) // self.HeightSpread), int((x_pos - 10) // self.WidthSpread))
    
    def get_node_by_coor(self, x, y):
        row, column = self.locate(x, y)
        if (0 <= row < self.rows) and (0 <= column < self.columns):
            return self.vertices[row][column]
        return None
    
    def graph_boot(self):
        self.rows = MatrixGlobals["graph size"][0]
        self.columns = MatrixGlobals["graph size"][0]
        self.WidthSpread = (PygameConstants["GRAPH WIDTH"] - 10) / self.columns
        self.HeightSpread = (PygameConstants["GRAPH HEIGHT"] - 10) / self.rows
        self.vertices : list[list[MatrixGraph.InnerNode]] = [
            [MatrixGraph.InnerNode(self.surface, 10 + row * self.WidthSpread, 10 + col * self.HeightSpread, row, col) for row in range(self.columns)] for col in range(self.rows)]
        self.starting_points : list[MatrixGraph.InnerNode] = []
        self.destination : MatrixGraph.InnerNode = None

    def handle_click(self):
        x, y = pygame.mouse.get_pos()
        node = self.get_node_by_coor(x, y)

        if None != node:
            mode = WORK_MODE.get_mode()
            if mode == WorkMode.CHOOSE_START and node.state >= AbstractNode.Mode.NOT_TOUCHED:
                if node in self.starting_points:
                    self.starting_points.remove(node)
                else:
                    self.starting_points.append(node)

            elif mode == WorkMode.ON_OFF_MODE:
                if node not in self.starting_points and node != self.destination:
                    node.flip()
            
            elif mode == WorkMode.CHOOSE_DEST:
                if node not in self.starting_points and node.state == AbstractNode.Mode.NOT_TOUCHED:
                    self.destination = node

            

    def blit(self):
        for node in self.get_vertices():
            node.blit(node in self.starting_points, node == self.destination)
    
    def get_neighbors(self, node : AbstractNode) -> list[AbstractNode]:
        ls = []
        row = node.row
        col = node.column
        node = self.vertices[row][col]
        if node != None:

            if node.row < self.rows - 1:
                neighbor = self.vertices[node.row + 1][node.column]
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    neighbor.prev = (row, col)
                    ls.append(neighbor)

            if node.column > 0:
                neighbor = self.vertices[node.row][node.column - 1]
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    neighbor.prev = (row, col)
                    ls.append(neighbor)

            if node.row > 0:
                neighbor = self.vertices[node.row - 1][node.column]
                
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    neighbor.prev = (row, col)
                    ls.append(neighbor)

            if node.column < self.columns - 1:
                neighbor = self.vertices[node.row][node.column + 1]
                if neighbor.state == AbstractNode.Mode.NOT_TOUCHED:
                    neighbor.prev = (row, col)
                    ls.append(neighbor)
        
        return ls

    def printer(self):
        print(self.get_starters())
        print(self.destination)
    
    def touch(self, node : InnerNode):
        self.vertices[node.column][node.row].touch()
    
    def finish(self, node : InnerNode):
        self.vertices[node.column][node.row].finish()
    
    def goal_reached(self):
        return self.destination.state >= AbstractNode.Mode.WORKED
    
    def get_starters(self) -> list[AbstractNode]:
        return self.starting_points
    
    def draw_solution(self):
        node = self.destination

        while None != node:
            print("!", node.row, node.column)
            node.assign_to_sol()
            if node.prev != None:
                node = self.vertices[node.prev[1]][ node.prev[0]]
            else:
                node = None



    
    

    
    


