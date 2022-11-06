
from enum import Enum
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
    "radio button size": 10
}

MatrixGlobals = {
    "rows" : 20,
    "columns" : 20
}

class MOUSE_KEYS():
        LEFT_KEY = 0
        WHEEL_KEY = 1
        RIGHT_KEY = 2

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (150, 150, 150)

SHADE_FACTOR = 0.8

HOVERED_COLOR = LIGHT_GREY
UNTOUCHED_COLOR = WHITE
OFF_COLOR = DARK_GREY
TOUCHED_COLOR = GREEN
FINISHED_COLOR = RED