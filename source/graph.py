from constants import *

import pygame

EMPTY = ""
X = "X"
O = "O"


class Graph:
    def __init__(self, size) -> None:
        self.size = size
        self.node_size = GAME_SIZE // self.size
        self.grid: list[list[GraphNode]] = [[GraphNode(row, col, self.node_size) for col in range(size)]
                                            for row in range(size)]

    def draw(self, window):
        for row in self.grid:
            for node in row:
                node.draw(window)

    def get_grid_pos(self, pos):
        """
            Turns (x,y) position on the screen to its respective (row, col) coords on the grid.
        """
        x, y = pos
        col = (y - TOP_MARGIN) // self.node_size
        row = (x - LEFT_MARGIN) // self.node_size

        return row, col

    def is_valid_node(self, row, col, offset=0):
        return offset <= row < (self.size - offset) and offset <= col < (self.size - offset)


class GraphNode:
    def __init__(self, row: int, col: int, size: int) -> None:
        self.row = row
        self.col = col
        self.color = BACKGROUND_COLOR
        self.value = EMPTY
        self.size = size

    def draw(self, window) -> None:
        x = LEFT_MARGIN + self.col * self.size
        y = TOP_MARGIN + self.row * self.size

        node_rect = pygame.Rect(x, y, self.size, self.size)

        pygame.draw.rect(window, self.color, node_rect)
        if self.value != EMPTY:
            font = pygame.font.Font(None, 100)

            if self.is_x():
                value_color = X_COLOR
            else:
                value_color = O_COLOR
            text_surface = font.render(self.value, True, value_color)
            text_rect = text_surface.get_rect(center=node_rect.center)
            window.blit(text_surface, text_rect)

        pygame.draw.line(window, GRID_COLOR, (x, y),
                         (x + self.size, y))

        pygame.draw.line(window, GRID_COLOR, (x, y),
                         (x, y + self.size))

        pygame.draw.line(window, GRID_COLOR, (x + self.size, y),
                         (x + self.size, y + self.size))

        pygame.draw.line(window, GRID_COLOR, (x, y + self.size),
                         (x + self.size, y + self.size))

    def set_empty(self):
        self.value = EMPTY

    def set_x(self):
        self.value = X

    def set_o(self):
        self.value = O

    def is_empty(self):
        return self.value == EMPTY

    def is_x(self):
        return self.value == X

    def is_o(self):
        return self.value == O
