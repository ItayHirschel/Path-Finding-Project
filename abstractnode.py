from ProjectConstants import *
from enum import IntEnum


class AbstractNode:

    class Mode(IntEnum):
        OFF = -1
        NOT_TOUCHED = 0
        WORKED = 1
        FINISHED = 2
        PART_OF_SOL = 3
    
    def __init__(self, x_pos, y_pos):
        self.x_coor = x_pos
        self.y_coor = y_pos
        self.state = AbstractNode.Mode.NOT_TOUCHED
        self.prev = None

    
    def move_to(self, x_pos : int, y_pos : int) -> None:
        if (0 <= x_pos < PygameConstants["WIDTH"]) and (0 <= x_pos < PygameConstants["HEIGHT"]):
            self.x_coor = x_pos
            self.y_coor = y_pos
    
    
    
    def __raise_state(self, new_state : Mode) -> None:
        if new_state > self.state:
            self.state = new_state

    def touch(self) -> None:
        self.state = AbstractNode.Mode.WORKED

    
    def finish(self) -> None:
        self.state = AbstractNode.Mode.FINISHED
    
    def assign_to_sol(self) -> None:
        self.state = AbstractNode.Mode.PART_OF_SOL

    def flip(self) -> None:
        if self.state == AbstractNode.Mode.OFF:
            self.state = AbstractNode.Mode.NOT_TOUCHED
        else:
            self.state = AbstractNode.Mode.OFF
    
    