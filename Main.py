import pygame
from ProjectConstants import *
from matrixgraph import MatrixGraph


class WorkMode():
    ON_OFF_MODE = 1



WIN = pygame.display.set_mode((PygameConstants["WIDTH"], PygameConstants["HEIGHT"]))
pygame.display.set_caption(PygameConstants["SCREEN_TITLE"])

def handel_mouse_left_key(work_mode, node : MatrixGraph.InnerNode):
    if work_mode == WorkMode.ON_OFF_MODE:
        if None != node:
            node.flip()


    


def blit_graph(graph):
    for node in graph.get_vertices():
        color = node.color
        if (node.is_hovered) : 
            color = (int(node.color[0] * SHADE_FACTOR), int(node.color[1] * SHADE_FACTOR),int(node.color[2] * SHADE_FACTOR))
        pygame.draw.rect(WIN, color, (node.x_coor, node.y_coor, VisGlobals["vertex size"], VisGlobals["vertex size"]))

def draw_screen(graph):
    WIN.fill(BLACK)

    blit_graph(graph)
    pygame.display.update()

# MAINLOOP

def mainloop(graph):
    WORK_MODE = WorkMode.ON_OFF_MODE
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
                    

        draw_screen(graph)
        

    pygame.quit()


if __name__ == "__main__":

    graph = MatrixGraph()

    mainloop(graph)

