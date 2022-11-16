from ProjectConstants import *
import pygame
from matrixgraph import MatrixGraph
from workmode import WORK_MODE, WorkMode
from clickable import Clickable


def handel_mouse_left_key():
    for clickable in Clickable.CLICKABLES:
        clickable.handle_click()

def mouse_motion_handler(node : MatrixGraph.InnerNode):
    if WORK_MODE.get_mode() == WorkMode.ON_OFF_MODE:
        if None != node and pygame.mouse.get_pressed()[MOUSE_KEYS.LEFT_KEY]:
            node.flip()


def dec_size():
    if MatrixGlobals["graph size"][0] > MIN_GRAPH_SIZE:
        MatrixGlobals["graph size"][0] -= 1
        adjust_node_size()


def inc_size():
    if MatrixGlobals["graph size"][0] < MAX_GRAPH_SIZE:
        MatrixGlobals["graph size"][0] += 1
        adjust_node_size()