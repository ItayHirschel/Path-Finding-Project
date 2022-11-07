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