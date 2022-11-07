from ProjectConstants import *
from Main import WorkMode
import pygame
from radiobutton import RadioButton
from matrixgraph import MatrixGraph



def handel_mouse_left_key(work_mode : RadioButton, node : MatrixGraph.InnerNode, clickables):
    work_mode.handel_click()
    if work_mode.get_mode() == WorkMode.ON_OFF_MODE:
        if None != node:
            node.flip()
        
        for clickable in clickables:
            clickable.handle_click()

def mouse_motion_handler(work_mode : RadioButton, node : MatrixGraph.InnerNode):
    if work_mode.get_mode() == WorkMode.ON_OFF_MODE:
        if None != node and pygame.mouse.get_pressed()[MOUSE_KEYS.LEFT_KEY]:
            node.flip()


def dec_size():
    if MatrixGlobals["graph size"][0] > MIN_GRAPH_SIZE:
        MatrixGlobals["graph size"][0] -= 1
        print(MatrixGlobals["graph size"][0]) 
        adjust_node_size()


def inc_size():
    if MatrixGlobals["graph size"][0] < MAX_GRAPH_SIZE:
        MatrixGlobals["graph size"][0] += 1
        print(MatrixGlobals["graph size"][0]) 
        adjust_node_size()