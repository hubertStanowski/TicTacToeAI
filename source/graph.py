from constants import *

from copy import deepcopy
import pygame


EMPTY = ""
X = "X"
O = "O"


class Graph:
    def __init__(self, size) -> None:
        self.size = size
        self.node_size = GAME_SIZE // self.size
        self.grid: list[list[str]] = [
            [EMPTY for col in range(size)] for row in range(size)]

    def draw(self, window):
        for row in range(self.size):
            for col in range(self.size):
                value = self.grid[row][col]
                x = LEFT_MARGIN + col * self.node_size
                y = TOP_MARGIN + row * self.node_size

                node_rect = pygame.Rect(x, y, self.node_size, self.node_size)

                pygame.draw.rect(window, BACKGROUND_COLOR, node_rect)
                if value != EMPTY:
                    font = pygame.font.Font(None, self.node_size)

                    if self.is_x(row, col):
                        value_color = X_COLOR
                    else:
                        value_color = O_COLOR
                    text_surface = font.render(value, True, value_color)
                    text_rect = text_surface.get_rect(center=node_rect.center)
                    window.blit(text_surface, text_rect)

                pygame.draw.line(window, GRID_COLOR, (x, y),
                                 (x + self.node_size, y))

                pygame.draw.line(window, GRID_COLOR, (x, y),
                                 (x, y + self.node_size))

                pygame.draw.line(window, GRID_COLOR, (x + self.node_size, y),
                                 (x + self.node_size, y + self.node_size))

                pygame.draw.line(window, GRID_COLOR, (x, y + self.node_size),
                                 (x + self.node_size, y + self.node_size))

    def clone(self) -> 'Graph':
        clone = Graph(self.size)
        clone.grid = deepcopy(self.grid)
        return clone

    def get_grid_pos(self, pos):
        """
            Turns (x,y) position on the screen to its respective (row, col) coords on the grid.
        """
        x, y = pos
        col = (y - TOP_MARGIN) // self.node_size
        row = (x - LEFT_MARGIN) // self.node_size

        return row, col

    def is_full(self) -> bool:
        empty_count = sum([row.count(EMPTY) for row in self.grid])

        return empty_count == 0

    def is_valid_node(self, row, col, offset=0):
        return offset <= row < (self.size - offset) and offset <= col < (self.size - offset)

    def set_empty(self, row, col):
        self.grid[row][col] = EMPTY

    def set_x(self, row, col):
        self.grid[row][col] = X

    def set_o(self, row, col):
        self.grid[row][col] = O

    def is_empty(self, row, col):
        return self.grid[row][col] == EMPTY

    def is_x(self, row, col):
        return self.grid[row][col] == X

    def is_o(self, row, col):
        return self.grid[row][col] == O
