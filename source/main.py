from constants import *
from graph import *
from tictactoe import *

import pygame
import random


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("TicTacToe AI")

    clock = pygame.time.Clock()
    game = TicTacToe(GRID_SIZES["large"])
    turn = random.choice([X, O])
    cooldown = CLICK_COOLDOWN

    while True:
        turn = game.player()
        cooldown += 1
        clock.tick(FPS)
        window.fill(BACKGROUND_COLOR)
        game.graph.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col, row = game.graph.get_grid_pos(pos)

                if game.graph.is_valid_node(row, col) and cooldown >= CLICK_COOLDOWN:
                    cooldown = 0
                    if game.graph.is_empty(row, col):
                        if turn == X:
                            game.graph.set_x(row, col)
                        else:
                            game.graph.set_o(row, col)

        pygame.display.update()


if __name__ == "__main__":
    main()
