import pygame
from ProjectConstants import *
from matrixgraph import MatrixGraph
from  radiobutton import RadioButton

# WORK MODES

class WorkMode():
    ON_OFF_MODE = 1
    STERILE = 2



pygame.init()





# FONTS

DEFAULT_FONT = pygame.font.SysFont( "cambria", FONT_SIZE)





def handel_mouse_left_key(work_mode : RadioButton, node : MatrixGraph.InnerNode):

    work_mode.handel_click()

    if work_mode.get_mode() == WorkMode.ON_OFF_MODE:
        if None != node:
            node.flip()


def blit_graph(screen, graph):
    for node in graph.get_vertices():
        color = node.color
        if (node.is_hovered) : 
            color = (int(node.color[0] * SHADE_FACTOR), int(node.color[1] * SHADE_FACTOR),int(node.color[2] * SHADE_FACTOR))
        pygame.draw.rect(screen, color, (node.x_coor, node.y_coor, VisGlobals["vertex size"], VisGlobals["vertex size"]))

def draw_screen(screen, graph, Printables):
    screen.fill(BLACK)

    blit_graph(screen, graph)

    for printable in Printables:
        printable.blit()

    pygame.display.update()

# MAINLOOP

def mainloop(graph, screen):

    work_modes = [
        RadioButton.Option("toggle button", WorkMode.ON_OFF_MODE, 650, 500),
        RadioButton.Option("sterile mode", WorkMode.STERILE, 650, 530),
    ]

    WORK_MODE = RadioButton(screen, DEFAULT_FONT, work_modes, 0)

    PRINTABLES = [WORK_MODE]

    clock = pygame.time.Clock()
    run = True
    node_hovered = None

    while run:
        clock.tick(PygameConstants["FPS"])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                (x,y) = pygame.mouse.get_pos()
                (ro, col) = graph.locate(x,y)
                node_hovered = graph.hover(ro, col, node_hovered)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                key_pressed = pygame.mouse.get_pressed()
                if (key_pressed[MOUSE_KEYS.LEFT_KEY]):
                    handel_mouse_left_key(WORK_MODE, node_hovered)
                    

        draw_screen(screen, graph, PRINTABLES)
        

    pygame.quit()


if __name__ == "__main__":

    # SCREEN CREATION
    WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
    pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

    graph = MatrixGraph()

    mainloop(graph, WIN)

