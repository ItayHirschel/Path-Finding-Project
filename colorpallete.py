

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (150, 150, 150)

SHADE_FACTOR = 0.5

def darken(color):
    return (int(color[0] * SHADE_FACTOR), int(color[1] * SHADE_FACTOR),int(color[2] * SHADE_FACTOR))