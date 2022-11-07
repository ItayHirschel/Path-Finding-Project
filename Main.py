import pygame
from ProjectConstants import *
from matrixgraph import MatrixGraph
from  radiobutton import RadioButton
from pushbutton import PushButton
from eventhandlers import *
from colorpallete import *

# WORK MODES

class WorkMode():
    STERILE = 0
    ON_OFF_MODE = 1
    



pygame.init()
DEFAULT_FONT = pygame.font.SysFont( "cambria", FONT_SIZE)


def draw_screen(screen, graph, Printables):
    screen.fill(BLACK)

    for printable in Printables:
        printable.blit()

    pygame.display.update()

# MAINLOOP

def mainloop(graph : MatrixGraph):
    screen = graph.surface
    work_modes = [
        RadioButton.Option("sterile mode", WorkMode.STERILE, 650, 530),
        RadioButton.Option("toggle button", WorkMode.ON_OFF_MODE, 650, 500),
    ]


    WORK_MODE = RadioButton(screen, DEFAULT_FONT, work_modes, 0)
    RESET_BUTTON = PushButton(screen, DEFAULT_FONT, 650, 750, 100, 150, "reset graph", lambda : graph.graph_boot())

    PRINTABLES = [WORK_MODE, RESET_BUTTON, graph]
    CLICKABLES = [RESET_BUTTON]

    clock = pygame.time.Clock()
    run = True
    node_hovered = None

    while run:
        clock.tick(PygameConstants["FPS"])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:                                           # QUIT
                run = False

            if event.type == pygame.MOUSEMOTION:                                    # MOUSE MOTION
                (x,y) = pygame.mouse.get_pos()
                on_node = graph.get_node_by_coor(x, y)
                if on_node != node_hovered:
                    node_hovered = on_node
                    mouse_motion_handler(WORK_MODE, node_hovered)
            
            if event.type == pygame.MOUSEBUTTONDOWN:                                # MOUSE BUTTON
                key_pressed = pygame.mouse.get_pressed()
                if (key_pressed[MOUSE_KEYS.LEFT_KEY]):
                    handel_mouse_left_key(WORK_MODE, node_hovered, CLICKABLES)
                
        draw_screen(screen, graph, PRINTABLES)
        
    pygame.quit()


if __name__ == "__main__":

    # SCREEN CREATION
    WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
    pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

    graph = MatrixGraph(WIN)

    mainloop(graph)

