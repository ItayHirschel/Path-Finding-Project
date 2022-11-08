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
# WORK MODES



    

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
    
    WORK_MODE.surface = screen
    WORK_MODE.font = DEFAULT_FONT

    alg_options = [
        RadioButton.Option("BFS scan", BFS_scanner, 650,400),
        RadioButton.Option("DFS scan", DFS_scanner, 650, 370)
    ]

    ALGO_CHOICE = RadioButton(screen, DEFAULT_FONT, alg_options, 0)


    RESET_BUTTON = PushButton(screen, DEFAULT_FONT, 700, 25, 180, 30, "reset graph", lambda : graph.graph_boot())
    GRAPH_SIZE_TXT = TextBox(screen, 700, 100, DEFAULT_FONT, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], text = MatrixGlobals["graph size"])
    DECREASE_SIZE_BUTTON = PushButton(screen, DEFAULT_FONT, 650, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "-", dec_size)
    INCREASE_SIZE_BUTTON = PushButton(screen, DEFAULT_FONT, 750, 100, VisGlobals["graph size txt box"], VisGlobals["graph size txt box"], "+", inc_size)


    PRINTABLES : list[Printable] = [WORK_MODE, RESET_BUTTON, graph, GRAPH_SIZE_TXT, DECREASE_SIZE_BUTTON, INCREASE_SIZE_BUTTON, ALGO_CHOICE]
    CLICKABLES : list[Clickable]= [WORK_MODE, RESET_BUTTON, DECREASE_SIZE_BUTTON, INCREASE_SIZE_BUTTON, graph, ALGO_CHOICE]

    clock = pygame.time.Clock()
    run = True
    node_hovered = None

    algo_running = True
    steps = 0
    fifo_up = False

    algorithm = ALGO_CHOICE.get_mode()

    for node in graph.get_vertices():
        print(node.row, node.column)
    
    while run:
        clock.tick(PygameConstants["FPS"])

        if WORK_MODE.get_mode() == WorkMode.PLAY:

            if not fifo_up:
                algorithm.update_fifo()
                fifo_up = True
                print(algorithm.fifo.queue)
            algo_running = algorithm.step()
            #pygame.time.wait(100)
            if not algo_running:
                if algorithm.is_success():
                    algorithm.draw_solution()
                WORK_MODE.choose(0)
            steps += 1
            print(steps)

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
                    handel_mouse_left_key(CLICKABLES)
                    
                
                
                
        draw_screen(screen, graph, PRINTABLES)

        if type(algorithm) != ALGO_CHOICE.get_mode():
            algorithm = ALGO_CHOICE.get_mode()(graph)

        if not algo_running:
            algorithm.update_fifo()
        
        #print(steps)
    pygame.quit()


if __name__ == "__main__":

    adjust_node_size()
    # SCREEN CREATION

    WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
    pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

    graph = MatrixGraph(WIN)
    mainloop(graph)

