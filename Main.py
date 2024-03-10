import pygame
from ProjectConstants import *
from matrixgraph import MatrixGraph
from radiobutton import RadioButton
from pushbutton import PushButton
from eventhandlers import *
from colorpallete import *
from textbox import TextBox
from printable import Printable
from clickable import Clickable
from workmode import WORK_MODE, WorkMode
from bfs import BFS_scanner
from dfs import DFS_scanner
from astar import ASTAR_scanner
# WORK MODES



    




def draw_screen():
    Printable.surface.fill(BLACK)
    for printable in Printable.PRINTABLES:
        printable.blit()
    pygame.display.update()

# MAINLOOP

def mainloop(graph : MatrixGraph):

    

    alg_options = [
        RadioButton.CircleOption("BFS scan", BFS_scanner, 650, 400),
        RadioButton.CircleOption("DFS scan", DFS_scanner, 650, 370),
        RadioButton.CircleOption("A* scan", ASTAR_scanner, 650, 340)
    ]

    ALGO_CHOICE = RadioButton(alg_options, 0)


    RESET_BUTTON = PushButton(700, 25, 180, 30, "reset graph", lambda : graph.graph_boot(), inact_modes=[WorkMode.PLAY])
    GRAPH_SIZE_TXT = TextBox(700, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], text = MatrixGlobals["graph size"])
    DECREASE_SIZE_BUTTON = PushButton(650, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "-", dec_size)
    INCREASE_SIZE_BUTTON = PushButton(750, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "+", inc_size)


    clock = pygame.time.Clock()
    run = True
    node_hovered = None

    algo_running = True
    steps = 0
    queue_up = False

    algorithm = ALGO_CHOICE.get_mode()

    
    while run:
        clock.tick(PygameConstants["FPS"])

        if WORK_MODE.get_mode() == WorkMode.PLAY:

            if not queue_up:
                algorithm.update_queue()
                queue_up = True

            algo_running = algorithm.step()
            #pygame.time.wait(100)
            
            if not algo_running:
                if algorithm.is_success():
                    algorithm.draw_solution()
                WORK_MODE.choose(0)

            steps += 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:                                           # QUIT
                run = False

            if event.type == pygame.MOUSEMOTION:                                    # MOUSE MOTION
                (x,y) = pygame.mouse.get_pos()
                on_node = graph.get_node_by_coor(x, y)
                if on_node != node_hovered:
                    node_hovered = on_node
                    mouse_motion_handler(node_hovered)
            
            if event.type == pygame.MOUSEBUTTONDOWN:                                # MOUSE BUTTON
                key_pressed = pygame.mouse.get_pressed()
                if (key_pressed[MOUSE_KEYS.LEFT_KEY]):
                    handel_mouse_left_key()
                    
                
                
                
        draw_screen()

        if type(algorithm) != ALGO_CHOICE.get_mode():
            algorithm = ALGO_CHOICE.get_mode()(graph)
            #print(algorithm)

        if not algo_running:
           algorithm.update_queue()
        
        #print(steps)
    pygame.quit()


if __name__ == "__main__":

    adjust_node_size()
    # SCREEN CREATION
    pygame.init()
    DEFAULT_FONT = pygame.font.SysFont( "cambria", FONT_SIZE)
    WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
    pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

    Printable.attach(WIN, DEFAULT_FONT)

    graph = MatrixGraph()
    mainloop(graph)

