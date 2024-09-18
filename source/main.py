from constants import *
from graph import *

import pygame
import random


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("TicTacToe AI")

    clock = pygame.time.Clock()
    graph = Graph(10)
    turn = random.choice([X, O])
    cooldown = CLICK_COOLDOWN

    while True:
        cooldown += 1
        clock.tick(FPS)
        window.fill(BACKGROUND_COLOR)
        graph.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col, row = graph.get_grid_pos(pos)

                if graph.is_valid_node(row, col) and cooldown >= CLICK_COOLDOWN:
                    cooldown = 0
                    node = graph.grid[row][col]
                    if node.is_empty():
                        if turn == X:
                            node.set_x()
                            turn = O
                        else:
                            node.set_o()
                            turn = X
                        node.draw(window)

        pygame.display.update()


if __name__ == "__main__":
    main()
