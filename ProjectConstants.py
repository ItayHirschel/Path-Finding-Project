import pygame
from colorpallete import *

# Constants

PygameConstants = {
    "WIDTH" : 800,
    "HEIGHT" : 600,
    "GRAPH WIDTH" : 600,
    "GRAPH HEIGHT" : 600,
    "SCREEN_TITLE" : "Lorem Ipsum",
    "FPS" : 60
}

VisGlobals = {
    "vertex size" : 25,
    "edge size" : 7,
    
}

MatrixGlobals = {
    "rows" : 20,
    "columns" : 20
}

class MOUSE_KEYS():
        LEFT_KEY = 0
        WHEEL_KEY = 1
        RIGHT_KEY = 2


HOVERED_COLOR = LIGHT_GREY
UNTOUCHED_COLOR = WHITE
OFF_COLOR = DARK_GREY
TOUCHED_COLOR = GREEN
FINISHED_COLOR = RED

#constants

radio_button_size = 10.0
radio_inner_circle_factor = 0.2

FONT_SIZE = 13