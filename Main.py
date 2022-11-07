import pygame
from ProjectConstants import *
from matrixgraph import MatrixGraph
from  radiobutton import RadioButton
from pushbutton import PushButton
from eventhandlers import *
from colorpallete import *
from textbox import TextBox

# WORK MODES

class WorkMode():
    STERILE = 0
    ON_OFF_MODE = 1




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
    graph_size = MatrixGlobals["graph size"]
    
    work_modes = [
        RadioButton.Option("sterile mode", WorkMode.STERILE, 650, 530),
        RadioButton.Option("toggle button", WorkMode.ON_OFF_MODE, 650, 500),
    ]

    # declare on screen objects
    WORK_MODE = RadioButton(screen, DEFAULT_FONT, work_modes, 0)
    RESET_BUTTON = PushButton(screen, DEFAULT_FONT, 700, 25, 180, 30, "reset graph", lambda : graph.graph_boot())
    GRAPH_SIZE_TXT = TextBox(screen, 700, 100, DEFAULT_FONT, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], text = graph_size)
    DECREASE_SIZE_BUTTON = PushButton(screen, DEFAULT_FONT, 650, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "-", dec_size)
    INCREASE_SIZE_BUTTON = PushButton(screen, DEFAULT_FONT, 750, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "+", inc_size)

    PRINTABLES = [WORK_MODE, RESET_BUTTON, graph, GRAPH_SIZE_TXT, DECREASE_SIZE_BUTTON, INCREASE_SIZE_BUTTON]
    CLICKABLES = [RESET_BUTTON, DECREASE_SIZE_BUTTON, INCREASE_SIZE_BUTTON]

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
    adjust_node_size()
    # SCREEN CREATION
    WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
    pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

    graph = MatrixGraph(WIN)

    mainloop(graph)

